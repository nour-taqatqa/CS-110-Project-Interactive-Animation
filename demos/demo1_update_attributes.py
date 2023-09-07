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


helpers.make_creature(
    canvas,
    (200, 200),
    random.uniform(40, 150), # random width
    fill='white',
    tag='my_creature'
)
gui.update()

# wait three seconds and then turn the creature yellow:
time.sleep(3)
utilities.update_fill_by_tag(canvas, 'my_creature', color = 'yellow')
gui.update()
########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()