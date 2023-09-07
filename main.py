from tkinter import Canvas, Tk
import helpers
import utilities
import helpers
import time
import random 

gui = Tk()
gui.title('My Terrarium')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width, height=window_height, background='white')
canvas.pack()


########################## YOUR CODE BELOW THIS LINE ##############################

# initiating my object and creatures:

canvas.create_text(
    (500, 100), 
    text='Right click to create creature or drag to move trees', 
    font=("Purisa", 15)
)
helpers.make_creature(canvas, (200, 200))
helpers.make_creature(canvas, (300, 250))
helpers.make_creature(canvas, (1200, 220),50)
helpers.make_creature(canvas, (900, 110),124)
helpers.make_creature(canvas, (1000, 260),90)

helpers.make_landscape_object (canvas, (600,503))
helpers.initiate_all_trees(canvas, (30,350),30, tag='tree')


########################################################################

#moving landscape object (building) with keyboard (M,K,J,I)

KEY_PRESS='<Key>'
active_tag = 'landscape_object'
LEFT_CLICK='<Button-1>'

def select_creature(event):
    tag= utilities.get_tag_from_x_y_coordinate(canvas, event.x, event.y)
    global active_tag
    active_tag = tag
    print(active_tag)
canvas.bind(LEFT_CLICK,select_creature) 
    

def move_building(event):
    distance=10
    if event.keycode==73:#up
        utilities.update_position_by_tag(canvas,tag=active_tag,
                                          x=0,y=-distance)
    if event.keycode == 77:#down   
        utilities.update_position_by_tag(canvas, tag=active_tag,
                                         x=0, y=distance)
    elif event.keycode == 74: #left
        utilities.update_position_by_tag(canvas, tag=active_tag,
                                         x=-distance, y=0)
    elif event.keycode == 75:  
        utilities.update_position_by_tag(canvas, tag=active_tag,
                                         x=distance, y=0)
    else:
        print(event.keycode)
        utilities.update_position_by_tag(canvas, tag = active_tag,
                                         x=10, y=0)
canvas.bind(KEY_PRESS, move_building)
canvas.focus_set()

############################################################################
# Animation: make a creature when I right-click

RIGHT_CLICK = '<Button>'


def add_creature (event):
    helpers.make_creature(canvas,(event.x, event.y),
                          size=random.randrange(30,60),tag='creature')
    
canvas.bind(RIGHT_CLICK,add_creature)


########################################################################3
###########################################################################
#Animation: drag trees

MOUSE_DRAG = '<B1-Motion>'

def drag_tree(event):
    utilities.update_position_by_tag(canvas, 'tree', x=event.x/66,
                                     y=event.y/170)

canvas.bind(MOUSE_DRAG, drag_tree)

############################################################################
#Animation: moving the car

utilities.make_line(canvas,
                         [(180,600),(300, 600),(500,600),(700,600),(900,600),
                          (1100,600)])
helpers.get_car(canvas, top_left=(140,520), color="#3D9970", tag='car')


##the fifth animation is built into the initaite trees function in helpers



########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()
