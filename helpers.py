import utilities
import random
import time
from tkinter import Canvas, Tk
gui = Tk()

def make_shape(canvas, center, size=100, tag='creature', fill='hotpink'):
    # just a demo of how you might think about making your creature:
    left_eye_pos = (center[0] - size / 4, center[1] - size / 5)
    right_eye_pos = (center[0] + size / 4, center[1] - size / 5)
    eye_width = eye_height = size / 10
    utilities.make_circle(canvas, center, size, color=fill, tag=tag)
    utilities.make_oval(canvas, left_eye_pos, eye_width, eye_height, color='black', tag=tag)
    utilities.make_oval(canvas, right_eye_pos, eye_width ,eye_height, color='black', tag=tag)
    utilities.make_line(canvas, [
        (center[0] - size / 2, center[1] + size / 3), 
        (center[0], center[1] + size / 1.2), 
        (center[0] + size / 2, center[1] + size / 3)
    ], curvy=True, tag=tag)
    
###########################################################################
    ########################################################################
    
def make_creature (canvas, center:tuple, size:float =100,
                   tag='creature', fill ='red'):
    tag='creature'
    top_left =(center[0]-size/2, center[1]-size/2)
    top_right =(center[0]+size/2, center[1]-size/2)
    left_eye = (center[0]-size/6, center[1]-size/8)
    right_eye = (center[0]+size/6, center[1]-size/8)
    
    utilities.make_line(canvas,[(top_left[0]+size/7,top_left[1]),
                                (top_left[0]+size/7,top_left[1]+size/3),
                                (top_left[0]+size/7,top_left[1]+size)],
                        tag='creature')
    
    utilities.make_line (canvas, [(top_right[0]-size/8,top_right[1]),
                                  (top_right[0]-size/8,top_right[1]+size/3),
                                  (top_right[0]-size/8,top_right[1]+size)],
                         tag='creature')
    
    utilities.make_oval(canvas, left_eye, size/8.5 ,size/8.5,color='black',
                        tag='creature')
    
    utilities.make_oval(canvas, right_eye, size/8.5 ,size/8.5,color='black',
                        tag='creature')
    utilities.make_rectangle (canvas, (top_left[0]+size/4.3,top_left[1]+size/1.6),
                              size/1.75, size/5, color='grey',
                              tag='creature')
    utilities.make_line(canvas,##horizontal bottom line 
    [ (top_left[0]+size/7, top_left[1]+size),  (top_left[0]+size/2, top_left[1]+size),
      (top_right[0]-size/8, top_left[1]+size) ],  # list of x-y pairs
    tag='creature')
    utilities.make_line(canvas,##legs starting from left to right
    [ (top_left[0]+size/3.9, top_left[1]+size),
      (top_left[0]+size/3.9, top_left[1]+size*1.2),
      (top_left[0]+size/3.9, top_left[1]+size*1.3),
      (top_left[0]+size/3.9, top_left[1]+size*1.4)],  
                        tag='creature')
    utilities.make_line(canvas,
                         [(top_left[0]+size/2.5, top_left[1]+size),
                          (top_left[0]+size/2.5, top_left[1]+size*1.2),
                          (top_left[0]+size/2.5, top_left[1]+size*1.3),
                          (top_left[0]+size/2.5, top_left[1]+size*1.4)],
                         tag='creature')
    utilities.make_line(canvas,
                         [(top_left[0]+size/1.65, top_left[1]+size),
                          (top_left[0]+size/1.65, top_left[1]+size*1.2),
                          (top_left[0]+size/1.65, top_left[1]+size*1.3),
                          (top_left[0]+size/1.65, top_left[1]+size*1.4)],  
                         tag='creature')
    utilities.make_line(canvas,
                         [(top_left[0]+size/1.35, top_left[1]+size),
                          (top_left[0]+size/1.35, top_left[1]+size*1.2),
                          (top_left[0]+size/1.35, top_left[1]+size*1.3),
                          (top_left[0]+size/1.35, top_left[1]+size*1.4)],  
                         tag='creature')

##############################################################################
    #########################################################################
    
def make_landscape_object(canvas, center:tuple,
                          size=450, tag='landscape_object', fill='#D96A9E'):
    object_center=(center[0], center[1])
    object_top_left = (object_center[0]-size/2,object_center[1]-size/1.5)
    window_width=size/10
    window_height=size/2.223
    utilities.make_rectangle (canvas, object_top_left, size, size/1.5,
                              color=fill,
                              tag=tag)
    utilities.make_rectangle(canvas,
                             (object_center[0]+size/3.2,object_center[1]-size/1.8),
                             window_width, window_height,color='#ADDEFF',
                              tag=tag)
    utilities.make_rectangle(canvas,
                             (object_center[0]+size/30,object_center[1]-size/1.8),
                              window_width, window_height,color='#ADDEFF',
                              tag=tag)
    utilities.make_rectangle(canvas,
                             (object_center[0]-size/8.5,object_center[1]-size/1.8),
                              window_width, window_height,color='#ADDEFF',
                              tag=tag)
    utilities.make_rectangle(canvas,
                             (object_center[0]-size/2.5,object_center[1]-size/1.8),
                              window_width, window_height,color='#ADDEFF',
                              tag=tag)
    
#################################################################################
    #################################################################
    
def make_tree (canvas, center:tuple, size=50,tag='tree', fill='#5CC47D'):
    size=size
    tree_stem_width=size/2.5
    tree_Stem_height=size*1.5
    utilities.make_rectangle(canvas,
                             (center[0]-size/6.2,center[1]+size),
                              tree_stem_width, tree_Stem_height,color='#764248',
                              tag=tag)
    utilities.make_poly_oval(canvas, (center[0],center[1]),##smallest oval
                             size/3, size/3.5, color=fill,
                             tag=[tag, "leaves"], stroke_width=1, outline=None)
    utilities.make_poly_oval(canvas, (center[0],center[1]+size/2.5),
                             size/1.9, size/3.5, color=fill,
                             tag=[tag, "leaves"], stroke_width=1, outline=None)
    utilities.make_poly_oval(canvas, (center[0],center[1]+size/1.3),##biggest
                             size/1.25, size/3.5, color=fill,
                             tag=[tag, "leaves"], stroke_width=1, outline=None)
    
#################################################################################
    ###############################################################################
    
def initiate_all_trees(canvas,center,size,tag='tree', fill='#5CC47D'):
    
    color_list =['#5CC47D','#38A059','#0A8969','#67890A','#968B09']
    fill_color=random.choice(color_list)
    size=random.randrange(30,45)
    counter=0
    number=0
    
    while counter<1300:
        if counter <350:
            
            make_tree(canvas,(center[0]+counter,center[1]),size=size,
                      fill=fill_color)
            make_tree(canvas,
                      (center[0]+center[0]/2+counter,center[1]+center[1]/7)
                      ,size=size,fill=fill_color)
            
        if counter > 750:
            make_tree(canvas,(center[0]+counter,center[1]),
                              size=size, fill=fill_color)
            make_tree(canvas,
                      (center[0]+center[0]/2+counter,center[1]+center[1]/7)
                      ,size=size,fill=fill_color)
        counter+=75
         
    while number <150:
        if number %2==0:
            time.sleep(0.3)
            utilities.update_fill_by_tag (canvas, 'leaves',color=fill_color)
            fill_color=random.choice(color_list)
            gui.update()
        number+=3
            
        

    
##############################################################################
    ########################################################################

def get_car (canvas, top_left=(140,520), color="#3D9970",tag='car'):
    
    utilities.make_car(canvas, top_left=(140,520), color="#3D9970", tag='car')
    counter=0
    while True:
        if utilities.get_right (canvas, 'car')== 1270 :
            utilities.update_position_by_tag(canvas, 'car', x=-1100)
    
        else:
            time.sleep(0.01+counter)
            utilities.update_position_by_tag (canvas, 'car',x=5, y=0)
            gui.update()
        counter+=0.0001
        














    
