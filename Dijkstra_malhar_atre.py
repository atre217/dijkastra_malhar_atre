import numpy as np
import matplotlib as plt
import cv2 
import time
import heapq

# Timer
timer=time.time()

# Start node
St_n=input("Enter coordinates for Start Node: ")
ST_x,ST_y=St_n.split()
ST_x=int(ST_x)
ST_y=int(ST_y)
St_n=(ST_x,ST_y)

# Goal node
Gl_n=input("Enter coordinates for Goal Node: ")
GL_x,GL_y=Gl_n.split()
GL_x=int(GL_x)
GL_y=int(GL_y)
Gl_n=(GL_x,GL_y)