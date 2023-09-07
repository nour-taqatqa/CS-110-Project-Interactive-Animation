'''
This demo shows you how you can create a new image by clicking the screen.
From your command line, type: pip3 install pillow
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

utilities.make_image(
    canvas, 
    'images/landscape2.jpg', 
    position=(0, 0), 
    scale=0.7, # 70% of original
    anchor="nw",
    tag="bgimage"
)

########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()