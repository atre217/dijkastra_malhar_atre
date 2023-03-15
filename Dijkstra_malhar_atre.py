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

work_space = np.full((250, 600), 255, dtype=np.uint8)
   
# defining the action set 

def move_up(x,y,cost):
	x = x + 1
	cost = 1 + cost
	return x,y,cost

def move_down(x,y,cost):
	x = x - 1
	cost = 1 + cost
	return x,y,cost

def move_right(x,y,cost):
	y = y + 1
	cost = 1 + cost
	return x,y,cost

def move_left(x,y,cost):
	y = y - 1
	cost = 1 + cost
	return x,y,cost

def move_up_right(x,y,cost):
    x = x + 1
    y = y + 1
    cost = np.sqrt(2) + cost 
    return x,y,cost 

def move_up_left(x,y,cost):
    x = x + 1
    y = y - 1
    cost = np.sqrt(2) + cost 
    return x,y,cost 

def move_down_right(x,y,cost):
    x = x + 1
    y = y - 1
    cost = np.sqrt(2) + cost 
    return x,y,cost 

def move_down_left(x,y,cost):
    x = x - 1
    y = y - 1
    cost = np.sqrt(2) + cost 
    return x,y,cost 

# define action set t
def Action_set(move,x,y,cost):

	if move == 'UP':
		return move_up(x,y,cost)
	elif move == 'DOWN':
		return move_down(x,y,cost)
	elif move == 'RIGHT':
		return move_right(x,y,cost)
	elif move == 'LEFT':
		return move_left(x,y,cost)
	elif move == 'UP_RIGHT'
		return move_up_right(x,y,cost)
	elif move == 'UP_LEFT':
		return move_up_left(x,y,cost)
	elif move == 'DOWN_RIGHT':
		return move_down_right(x,y,cost)
	elif move == 'DOWN_LEFT':
		return move_down_left(x,y,cost)
	else:
		return None
