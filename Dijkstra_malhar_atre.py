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

# Generate the pathe
def generate_path(F_Dic,node):
    path=[]
    path.append(node)
    P_nd=F_Dic[node]
    while P_nd is not None and P_nd != St_n:
        path.append(P_nd)
        P_nd=F_Dic[P_nd]
    path.append(St_n)
    path.reverse()
    return path

# Dijkstra 
def dijkstra(St_n,Gl_n):

    obstacle_space()
    F_Dic={}
    IN_Lst=[]
    FN_Lst=set()
    crossed=set() 

    heapq.heappush(IN_Lst,(0,St_n))
   
    while IN_Lst:
        cost,node=heapq.heappop(IN_Lst)
       
        if node not in crossed:
            crossed.add(node)
        FN_Lst.add(node)
        if not poss_nd(node[0],node[1]):
            continue

        if node[1] == Gl_n[0] and node[0]==Gl_n[1]:
            print('total cost',cost)
            return generate_path(F_Dic,node),F_Dic

        for action in ['UP','DOWN','RIGHT','LEFT','UP_RIGHT','UP_LEFT','DOWN_RIGHT','DOWN_LEFT']:
            nodes_1,c2c=action(node[0],node[1],cost) 
            # print(nodes_1,'nn',action)
            if nodes_1 not in FN_Lst and nodes_1 is not None:
                if nodes_1 not in crossed:
                    heapq.heappush(IN_Lst,(c2c,nodes_1))
                    crossed.add(nodes_1)
                    F_Dic.update({nodes_1:node})
                else:
                    # print("repeated")
                    for i in range(len(IN_Lst)):
                        if IN_Lst[i][1]==nodes_1:
                            if IN_Lst[i][0]>c2c:
                                IN_Lst[i]=(c2c,nodes_1)
                                F_Dic.update({nodes_1:node})
    
def show_ws(F_Dic):
    for i in F_Dic.keys():
        cv2.circle(work_space,(i[1],250-i[0]),1,(79,79,79),-1)
        cv2.imshow('work_space',work_space)
        cv2.waitKey(1)

    for i in range(len(path)):
        cv2.circle(work_space,(path[i][1],250-path[i][0]),1,(255,255,255),-1)
        cv2.imshow('work_space',work_space)
        cv2.waitKey(1)
def Backtrack(goal_node):  
    print ("Entered backtracking")
    x_path = []
    y_path = []
    x_path.append(goal_node.x)
    y_path.append(goal_node.y)

    P_nd = goal_node.parent_id
    while P_nd != -1:
        x_path.append(P_nd.x)
        y_path.append(P_nd.y)
        P_nd = P_nd.parent_id
        
    x_path.reverse()
    y_path.reverse()
    
    return x_path,y_path
    
                        
def poss_nd(ST_x,ST_y):
    i=ST_x
    j=ST_y
    if work_space[i][j]==255:
        return True
    else:
        return False

print(work_space.shape)
path,F_Dic=dijkstra(St_n,Gl_n)
print(path)
show_ws(F_Dic)
cv2.imshow('work_space',work_space)

timer_stop = time.time()
comp_time = timer_stop - timer
print("The Total Runtime is:  ", comp_time) 
print('Time: ',comp_time)
