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
canvas.create_text(
    (window_width / 2, window_height / 2), 
    text='Click anywhere add a creature', 
    font=("Purisa", 32)
)
def make_creature_from_click(event):
    helpers.make_creature(
        canvas,
        (event.x, event.y),
        random.uniform(40, 150), # random width
        fill='white'
    )

canvas.bind(MOUSE_CLICK, make_creature_from_click)  # add event handler

########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()