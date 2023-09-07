'''
Documentation: 
  * tkinter events: https://www.python-course.eu/tkinter_events_binds.php
  * Canvas: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas.html
  * Other Canvas methods: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas-methods.html
'''
from tkinter import Canvas, Tk
from utilities import update_position_by_tag, make_circle
from helpers import make_creature
import math
import time

gui = Tk()
gui.title('Circle')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

center_x = 200
center_y = 200
distance_from_center = 120
center = (center_x, center_y)
center_creature = (center_x, center_y - distance_from_center)
make_creature(canvas, center_creature, 60, fill='hotpink', tag='creature')
make_circle(canvas, center, 10, color='black')
counter = 0
slow_factor = 250
while True:
    # calculate new position of x and y
    radians = counter / slow_factor
    dy = distance_from_center / slow_factor * math.sin(radians)
    dx = distance_from_center / slow_factor * math.cos(radians)
    update_position_by_tag(canvas, tag='creature', x=dx, y=dy)
    counter += 1
    gui.update()
    time.sleep(.01)


########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()