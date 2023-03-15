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
	# # Defining obstacle with clearance for point bot
# def totalobstacle():
    
#     # Hexagon
#     center = (300, 125)
#     side_length = 80
#     x_coords = center[0] + side_length*np.array([1, np.cos(np.pi/3), -np.cos(np.pi/3), -1, -np.cos(np.pi/3), np.cos(np.pi/3)])
#     y_coords = center[1] + side_length*np.array([0, np.sin(np.pi/3), np.sin(np.pi/3), 0, -np.sin(np.pi/3), -np.sin(np.pi/3)])
#     pts1= np.array([(x, y) for x, y in zip(x_coords, y_coords)], np.int32)
#     pts = pts1.reshape((-1,1,2))
#     cv2.polylines(work_space, [pts1], True, (0, 255, 0), thickness=1)
#     cv2.fillPoly(work_space, [pts1], color=(0, 0, 0))

#     # Rectangles
#     cv2.rectangle(work_space,(95,0),(155,105),0,-1)
#     cv2.rectangle(work_space,(94,145),(155,250),0,-1)
#     # Triangle
#     pts2= np.array([[405,10], [405, 240], [465, 125]], np.int32)
#     cv2.polylines(work_space, [pts2], True, (0,255,0), thickness=1)
#     cv2.fillPoly(work_space, [pts2], color=(0, 0, 0))
#     cv2.imshow('work_space',work_space)
#     cv2.waitKey(0)

# # Defining actualobstacle
# def actualobstacle():

#     # Hexagon
#     center = (300, 125)
#     side_length = 75
#     x_coords = center[0] + side_length*np.array([1, np.cos(np.pi/3), -np.cos(np.pi/3), -1, -np.cos(np.pi/3), np.cos(np.pi/3)])
#     y_coords = center[1] + side_length*np.array([0, np.sin(np.pi/3), np.sin(np.pi/3), 0, -np.sin(np.pi/3), -np.sin(np.pi/3)])
#     pts3= np.array([(x, y) for x, y in zip(x_coords, y_coords)], np.int32)
#     pts3 = pts3.reshape((-1,1,2))
#     cv2.fillPoly(work_space, [pts3], (127, 127, 127))
#     # Rectangles
#     cv2.rectangle(work_space,(100,0),(150,100),(127,127,127),-1)
#     cv2.rectangle(work_space,(100,150),(150,250),(127,127,127),-1)
#     # Triangle
#     pts4 = np.array([[410, 25], [410, 225], [460, 125]], np.int32)
#     cv2.polylines(work_space, [pts4], isClosed=True,color=(0,0,0), thickness=1)
#     cv2.fillPoly(work_space, [pts4], (127, 127, 127))

#     cv2.imshow('work_space',work_space)
#     cv2.waitKey(0)

def obstacle_space():

        # CLEARANCE FOR

        # Rectangles
        cv2.rectangle(work_space,(95,0),(155,105),0,-1)
        cv2.rectangle(work_space,(94,145),(155,250),0,-1)

        # Hexagon
        hex_centre = (300, 125)
        hex_side = 80
        x_cd = hex_centre[0] + hex_side*np.array([1, np.cos(np.pi/3), -np.cos(np.pi/3), -1, -np.cos(np.pi/3), np.cos(np.pi/3)])
        y_cd = hex_centre[1] + hex_side*np.array([0, np.sin(np.pi/3), np.sin(np.pi/3), 0, -np.sin(np.pi/3), -np.sin(np.pi/3)])
        hex_p1= np.array([(x, y) for x, y in zip(x_cd, y_cd)], np.int32)
        pts = hex_p1.reshape((-1,1,2))
        cv2.polylines(work_space, [hex_p1], True, (0, 255, 0), thickness=1)
        cv2.fillPoly(work_space, [hex_p1], color=(0, 0, 0))

        # Triangle
        pts2= np.array([[405,10], [405, 240], [465, 125]], np.int32)
        cv2.polylines(work_space, [pts2], True, (0,255,0), thickness=1)
        cv2.fillPoly(work_space, [pts2], color=(0, 0, 0))
        cv2.imshow('work_space',work_space)
        cv2.waitKey(0)

        # OBSTACLES FOR
        # Rectangles
        cv2.rectangle(work_space,(100,0),(150,100),(127,127,127),-1)
        cv2.rectangle(work_space,(100,150),(150,250),(127,127,127),-1)

        # Hexagon
        # hex_pts = np.array([[235.05, 87.5], [300, 68.09], [364.95, 87.5], [364.95, 162.5], [300, 181.91], [235.05, 1662.5]])
        # cv2.fillPoly(work_space, [hex_pts], True, (0, 255, 0), thickness=1)
        hex_centre = (300, 125)
        hex_side = 75
        x_cd = hex_centre[0] + hex_side*np.array([1, np.cos(np.pi/3), -np.cos(np.pi/3), -1, -np.cos(np.pi/3), np.cos(np.pi/3)])
        y_cd = hex_centre[1] + hex_side*np.array([0, np.sin(np.pi/3), np.sin(np.pi/3), 0, -np.sin(np.pi/3), -np.sin(np.pi/3)])
        pts3= np.array([(x, y) for x, y in zip(x_cd, y_cd)], np.int32)
        pts3 = pts3.reshape((-1,1,2))
        cv2.fillPoly(work_space, [pts3], (127, 127, 127))


        # Triangle
        pts4 = np.array([[410, 25], [410, 225], [460, 125]], np.int32)
        cv2.polylines(work_space, [pts4], isClosed=True,color=(0,0,0), thickness=1)
        cv2.fillPoly(work_space, [pts4], (127, 127, 127))

        cv2.imshow('work_space',work_space)
        cv2.waitKey(0)

