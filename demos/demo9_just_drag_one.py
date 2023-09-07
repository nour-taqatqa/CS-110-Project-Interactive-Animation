'''
This demo shows you how you can create a new image by clicking the screen.
Documentation: 
  * tkinter events: https://www.python-course.eu/tkinter_events_binds.php
  * Canvas: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas.html
  * Other Canvas methods: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas-methods.html
'''
from tkinter import Canvas, Tk
import helpers
import utilities
import time
import random

gui = Tk()
gui.title('Tour of options...')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width, height=window_height, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################
MOUSE_CLICK = '<Button-1>'
MOUSE_DRAG = '<B1-Motion>'
RIGHT_CLICK = '<Button-2>'
KEY_PRESS = '<Key>'
canvas.create_text(
    (window_width / 2, window_height / 2), 
    text='Click circle to select it. Drag selected circle to move it.', 
    font=("Purisa", 32)
)

# need a global variable to store which item should be clicked:
active_tag = None

def select_circle(event):
    global active_tag
    
    # if something is already active, deactivate it:
    if active_tag:
        utilities.update_fill_by_tag(canvas, active_tag, 'hotpink')
        active_tag = None
    
    # get new active tag:
    active_tag = utilities.get_tag_from_x_y_coordinate(canvas, event.x, event.y)
    if active_tag:
        utilities.update_fill_by_tag(canvas, active_tag, 'yellow')


def move_circle(event):
    if not active_tag:
        print('no tag selected')
        return
    
    # calculate the current position of the current shape:
    width = utilities.get_width(canvas, active_tag)
    height = utilities.get_height(canvas, active_tag)
    left = utilities.get_left(canvas, active_tag) 
    top = utilities.get_top(canvas, active_tag) 
    current_x = left + (width / 2)
    current_y = top + (height / 2)

    # calculate the delta of the current shape:
    delta_x = -1 * (current_x - event.x)
    delta_y = -1 * (current_y - event.y)

    # move the shape:
    utilities.update_position_by_tag(canvas, active_tag, x=delta_x, y=delta_y)

counter = 1
def make_circle(x, y):
    global counter
    utilities.make_circle(
        canvas,
        (x, y),
        20, 
        color='hotpink',
        tag='circle_' + str(counter)
    )
    counter += 1
    canvas.focus_set()


canvas.bind(MOUSE_CLICK, select_circle) 
canvas.bind(MOUSE_DRAG, move_circle)

for i in range(50):
    make_circle(random.randint(0, window_width), random.randint(0, window_height))


########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()