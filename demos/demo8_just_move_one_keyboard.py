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
import keycodes

gui = Tk()
gui.title('Tour of options...')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width, height=window_height, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################
MOUSE_CLICK = '<Button-1>'
# DOUBLE_CLICK = '<Double-Button-1>'  # couldn't get it to work
RIGHT_CLICK = '<Button-2>'
KEY_PRESS = '<Key>'
canvas.create_text(
    (window_width / 2, window_height / 2), 
    text='Click to add a circle. Right-click to select circle. Press arrow keys to move circle', 
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



counter = 1
def make_circle(event):
    global counter
    utilities.make_circle(
        canvas,
        (event.x, event.y),
        20, 
        color='hotpink',
        tag='circle_' + str(counter)
    )
    counter += 1

def move_circle(event):
    distance = 10
    if event.keycode == keycodes.get_up_keycode():
        utilities.update_position_by_tag(canvas, tag=active_tag, x=0, y=-distance)
    elif event.keycode == keycodes.get_down_keycode():
        utilities.update_position_by_tag(canvas, tag=active_tag, x=0, y=distance)
    elif event.keycode == keycodes.get_left_keycode():
        utilities.update_position_by_tag(canvas, tag=active_tag, x=-distance, y=0)
    elif event.keycode == keycodes.get_right_keycode():
        utilities.update_position_by_tag(canvas, tag=active_tag, x=distance, y=0)
    else:
        print(event.keycode)

canvas.bind(MOUSE_CLICK, make_circle) 
canvas.bind(KEY_PRESS, move_circle)
canvas.bind(RIGHT_CLICK, select_circle)


# NOTE: canvas.focus_set() is critical to making the keyboard functions work:
canvas.focus_set()

########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()