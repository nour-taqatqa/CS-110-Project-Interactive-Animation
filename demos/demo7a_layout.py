'''
Documentation: 
  * tkinter events: https://www.python-course.eu/tkinter_events_binds.php
  * Canvas: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas.html
  * Other Canvas methods: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas-methods.html
'''
# If you want to have text-based user input:
from tkinter import Canvas, Tk, Frame, Button, N, W, E, S, messagebox, Entry, StringVar
import utilities
import time


def add_message_to_canvas():
   canvas.create_text(
        (100, 50), 
        text=my_name.get(),
        font=("Purisa", 32)
    )

# 1. Initialize window:
gui = Tk()
gui.title('Tour of options...')
gui.configure(background='hotpink')

# 2. Configure layout:
mainframe = Frame(gui, bg='#EEEEEE', padx=5, pady=5)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
gui.rowconfigure(0, weight=1) # row 0 takes up 10% of screen
gui.rowconfigure(1, weight=9) # row 1 takes up 90% of screen

# 3. Initialize close button:
# read about buttons:
# https://www.labspoint.com/python3/tk_button.htm
my_name = StringVar()
Entry(
    mainframe,
    textvariable=my_name
).grid(column=0, row=0, sticky=E)

Button(
    mainframe,
    padx=5, 
    pady=5,
    text='ADD MESSAGE',
    command=add_message_to_canvas
).grid(column=1, row=0, sticky=E)


# 4. initialize canvas:
canvas_width = gui.winfo_screenwidth()
canvas_height = gui.winfo_screenheight() - 100
canvas = Canvas(
    gui, 
    width=canvas_width,
    height=canvas_height,
    background='white')
canvas.grid(column=0, row=1, sticky=W)

utilities.make_circle(canvas, (200, 200), 20, color='hotpink', tag='my_circle')

while True:
    utilities.update_position_by_tag(canvas, 'my_circle', 2, 0)
    time.sleep(0.01)
    gui.update()

########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()