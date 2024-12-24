pacman_x = 0
pacman_y = 0
pacman_radius = 9
pacman_speed = 3
pacman_up_flag = False
pacman_down_flag = False
pacman_left_flag = False
pacman_right_flag = False


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import time

game_over_flag = False
play_button_flag = False
cross_button_flag = False
restart_button_flag = False
heart1_flag = False
heart2_flag = False
heart3_flag = False
score = 0


def drawpoints(x,y,size = 2):
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()



def FindZone(x0,y0,x1,y1):
    dx = x1-x0
    dy = y1-y0
    zone = -1

    if abs(dx)>abs(dy):
        if dx>0 and dy>0:
            zone = 0
        elif dx<0 and dy>0:
            zone=3
        elif dx<0 and dy<0:
            zone=4
        else:
            zone=7
    else:
        if dx>0 and dy>0:
            zone=1
        elif dx<0 and dy>0:
            zone=2
        elif dx<0 and dy<0:
            zone=5 
        else:
            zone=6
    return zone




def convert_to_zone0(original_zone,x,y) :


    if (original_zone == 0) :
        return x,y
    elif (original_zone == 1) :
        return y,x
    elif (original_zone == 2) :
        return -y,x
    elif (original_zone == 3) :
        return -x,y
    elif (original_zone == 4) :
        return -x,-y
    elif (original_zone == 5) :
        return -y,-x
    elif (original_zone == 6) :
        return -y,x
    elif (original_zone == 7) :
        return x,-y
    


def convert_to_originalzone(originalzone,x,y):
    if originalzone == 0:
        return x,y
    elif originalzone == 1:
        return y,x
    elif originalzone == 2:
        return -y,-x
    elif originalzone == 3:
        return -x,y
    elif originalzone == 4:
        return -x,-y
    elif originalzone == 5:
        return -y,-x
    elif originalzone == 6:
        return y,-x
    elif originalzone == 7:
        return x,-y



def MidpointLine(zone,x0,y0,x1,y1,size):
    dx = x1-x0
    dy = y1-y0
    d = 2*dy-dx
    E = 2*dy
    NE = 2*(dy-dx)
    x = x0
    y = y0
    while x<x1:
        original_x,original_y = convert_to_originalzone(zone,x,y)
        drawpoints(original_x,original_y,size)
        if d<=0:
            d = d+E
            x = x+1
        else:
            d = d+NE
            x = x+1
            y = y+1



def PlotCirclePoints(xc, yc, x, y):
    drawpoints(xc + x, yc + y)  
    drawpoints(xc - x, yc + y) 
    drawpoints(xc + x, yc - y)  
    drawpoints(xc - x, yc - y)  
    drawpoints(xc + y, yc + x)  
    drawpoints(xc - y, yc + x)  
    drawpoints(xc + y, yc - x)  
    drawpoints(xc - y, yc - x) 



def MidpointCircle(r,xc,yc):
    d = 1-r
    x = 0
    y = r
    PlotCirclePoints(xc,yc,x,y)
    while x<y:
        if d<0:
            d = d+2*x+3
        else:
            d = d+2*x-2*y+5
            y = int(y-1)
        x+=1
        PlotCirclePoints(xc,yc,int(x),int(y))




def Eight_way_symmetry(x0,y0,x1,y1,size):
    if x0==x1:
        for y in range(int(min(y0, y1)), int(max(y0, y1)) + 1):
            drawpoints(x0,y,size)
    elif y0==y1:
        for x in range(int(min(x0, x1)), int(max(x0, x1)) + 1):
            drawpoints(x,y0,size)
    else:
        zone = FindZone(x0,y0,x1,y1)
        coverted_x0,converted_y0 = convert_to_zone0(zone,x0,y0)
        coverted_x1,coverted_y1 = convert_to_zone0(zone,x1,y1)
        MidpointLine(zone,coverted_x0,converted_y0,coverted_x1,coverted_y1,size)



def draw_play_button():
    Eight_way_symmetry(-5, 240, 15, 230,2) 
    Eight_way_symmetry(-5, 240, -5, 220,2) 
    Eight_way_symmetry(-5, 220, 15, 230,2) 



def draw_pause_button():
    Eight_way_symmetry(-5, 240, -5, 220,2)
    Eight_way_symmetry(5, 240, 5, 220,2)


def draw_restart_button():
    Eight_way_symmetry(-240, 230, -210, 230,2)
    Eight_way_symmetry(-240, 230, -220, 240,2)
    Eight_way_symmetry(-240, 230, -220, 220,2)


def draw_cross_button():
    Eight_way_symmetry(240, 240, 220, 220,2)
    Eight_way_symmetry(220, 240, 240, 220,2)


def heart1():
    glColor3f(1.0, 0.0, 0.0)
    Eight_way_symmetry(220, 180, 232, 165,2) 
    Eight_way_symmetry(220, 180, 226, 187,2)
    Eight_way_symmetry(226, 187, 232, 180,2)
    Eight_way_symmetry(244, 180, 238, 187,2)
    Eight_way_symmetry(238, 187, 232, 180,2)
    Eight_way_symmetry(232, 165, 244, 180,2)
    Eight_way_symmetry(239, 187, 244, 180,2)

def heart2():
    glColor3f(1.0, 0.0, 0.0)
    Eight_way_symmetry(220, 140, 232, 125,2) 
    Eight_way_symmetry(220, 140, 226, 147,2)
    Eight_way_symmetry(226, 147, 232, 140,2)
    Eight_way_symmetry(244, 140, 238, 147,2)
    Eight_way_symmetry(238, 147, 232, 140,2)
    Eight_way_symmetry(232, 125, 244, 140,2)
    Eight_way_symmetry(239, 147, 244, 140,2)

def heart3():
    glColor3f(1.0, 0.0, 0.0)
    Eight_way_symmetry(220, 100, 232, 85,2) 
    Eight_way_symmetry(220, 100, 226, 107,2)
    Eight_way_symmetry(226, 107, 232, 100,2)
    Eight_way_symmetry(244, 100, 238, 107,2)
    Eight_way_symmetry(238, 107, 232, 100,2)
    Eight_way_symmetry(232, 85, 244, 100,2)
    Eight_way_symmetry(239, 107, 244, 100,2)



def GameOver():
    # G
    Eight_way_symmetry(-120, 50, -90, 50,2)  
    Eight_way_symmetry(-120, 50, -120, 10,2)  
    Eight_way_symmetry(-120, 10, -90, 10,2)  
    Eight_way_symmetry(-90, 10, -90, 30,2)  
    Eight_way_symmetry(-100, 30, -90, 30,2)  

    # A
    Eight_way_symmetry(-80, 10, -70, 50,2)  
    Eight_way_symmetry(-70, 50, -60, 10,2)  
    Eight_way_symmetry(-75, 30, -65, 30,2)  

    # M
    Eight_way_symmetry(-50, 10, -50, 50,2)  
    Eight_way_symmetry(-50, 50, -40, 30,2)  
    Eight_way_symmetry(-40, 30, -30, 50,2)  
    Eight_way_symmetry(-30, 50, -30, 10,2)  

    # E
    Eight_way_symmetry(-20, 10, -20, 50,2)  
    Eight_way_symmetry(-20, 50, -10, 50,2)  
    Eight_way_symmetry(-20, 30, -10, 30,2) 
    Eight_way_symmetry(-20, 10, -10, 10,2)  



    # O
    Eight_way_symmetry(0, 10, 0, 50,2)  
    Eight_way_symmetry(20, 10, 20, 50,2)  
    Eight_way_symmetry(0, 50, 20, 50,2)  
    Eight_way_symmetry(0, 10, 20, 10,2)  

    # V
    Eight_way_symmetry(30, 50, 40, 10,2)  
    Eight_way_symmetry(40, 10, 50, 50,2)  

    # E
    Eight_way_symmetry(60, 10, 60, 50,2)  
    Eight_way_symmetry(60, 50, 70, 50,2)  
    Eight_way_symmetry(60, 30, 70, 30,2)  
    Eight_way_symmetry(60, 10, 70, 10,2)  

    # R
    Eight_way_symmetry(80, 10, 80, 50,2)  
    Eight_way_symmetry(80, 50, 90, 50,2)  
    Eight_way_symmetry(90, 50, 90, 30,2)  
    Eight_way_symmetry(80, 30, 90, 30,2)  
    Eight_way_symmetry(80, 30, 91, 10,2)  



maze_walls = [

    #Boundary
    ("horizontal", -220, -220, 220, -220), #Bottom
    ("horizontal", -220, 220, 220, 220), #top
   
   
    #Left Boundary
    ("horizontal", -220, 100, -139, 100),
    ("vertical", -139, 43, -139, 100),
    ("horizontal", -220, 44, -139, 44),
    ("horizontal", -220, -12, -140, -10),
    ("vertical", -140, -70, -140, -12),
    ("horizontal", -220, -70, -140, -70),
    ("vertical", -220, 100, -220, 220),
    ("vertical", -220, -10, -220, 43),
    ("vertical", -220, -220, -220, -70),



    #Right Boundary
    ("horizontal", 139, 100, 220, 100),
    ("vertical", 139, 43, 139, 100),
    ("horizontal", 139, 43, 220, 47),
    ("horizontal", 140, -12, 220, -10),
    ("vertical", 140, -70, 140, -12),
    ("horizontal", 140, -70, 220, -70),
    ("vertical", 220, 100, 220, 220),
    ("vertical", 220, -10, 220, 43),
    ("vertical", 220, -220, 220, -70),



    ('horizontal',-180,173,-148,173),
    ('horizontal',148,173,180,173),
    ('horizontal',-111,173,-47,173),
    ('horizontal',47,173,111,173),
    ('horizontal',-167,140,-89,140),
    ('horizontal',89,140,167,140),
    ('vertical',0,135,0,155),
    ('horizontal',-24,135,0,135),

    ('vertical',0,185,0,220),
    ('horizontal',-220,-145,-175,-145),
    ('horizontal',175,-145,220,-145),
    ('horizontal',-174,-110,-139,-110),
    ('vertical',-139,-145,-139,-110),

    ('horizontal',139,-110,174,-110),
    ('vertical',139,-145,139,-110),

    #Middel box
    ('horizontal',-42,-20,42,-20),
    ('vertical',-44,-20,-45,26),
    ('vertical',44,-20,45,26),
    ('horizontal',-44,26,-20,26),
    ('horizontal',20,26,44,26),

    ('horizontal',-182,-182,-70,-182),
    ('vertical',-106,-180,-106,-136),
    ('horizontal',70,-182,182,-182),
    ('vertical',106,-180,106,-136),
    
    ('horizontal',-67,-144,67,-144),
    ('vertical',0,-190,0,-144),

    ('horizontal',-108,-100,-70,-100),
    ('horizontal',70,-100,108,-100),

    ('vertical',-106,-63,-106,-21),
    ('vertical',106,-63,106,-21),

    ('horizontal',-68,-59,68,-59),
    ('vertical',0,-104,0,-59),

    ('vertical',-106,21,-106,97),
    ('vertical',106,21,106,97),
    ('horizontal',-106,58,-54,58),
    ('horizontal',54,58,106,58),

    ('horizontal',-68,100,68,100),
    ('vertical',0,70,0,100)

]




food = [(-200,-200),(-180,-200),(-160,-200),(-140,-200),(-120,-200),(-100,-200),
        (-80,-200),(-60,-200),(-40,-200),(-20,-200),(0,-200),(20,-200),(40,-200),
        (60,-200),(80,-200),(100,-200),(120,-200),(140,-200),(160,-200),(180,-200),(200,-200),

        (-200,-180),(-200,-160),(-180,-160),(-160,-160),(-140,-160),(-120,-160),(-120,-140),
        (-120,-120),(-120,-100),(-120,-80),(-120,-60),(-120,-40),(-120,-20),(-120,0),(-120,20),
        (-120,40),(-120,60),(-120,80),(-120,100),(-120,120),(-140,120),(-160,120),(-180,120),(-200,120),
        (-200,140),(-200,160),(-200,180),(-200,200),(-180,200),(-160,200),(-140,200),(-120,200),(-100,200),(-80,200),(-60,200),(-40,200),(-20,200),
        (-20,180),(-20,160),(-20,120),(-40,120),(-60,120),(-80,120),(-100,120),(0,120),
        (-40,160),(-60,160),(-80,160),(-100,160),(-120,160),(-140,160),(-160,160),(-180,160),(-130,180),(-70,140),(-50,140),
        (-140,15),(-160,15),(-180,15),(-200,15),
        (-100,15),(-80,15),(-60,15),(-80,-5),(-80,-25),(-80,-45),(-80,-65),(-80,-85),
        (-80,40),(-60,40),(-40,40),(-20,40),(20,40),(40,40),(60,40),
        (-20,60),(-20,80),(-40,80),(-60,80),(-80,80),
        (-60,-40),(-40,-40),(-20,-40),(0,-40),(20,-40),(40,-40),(60,-40),
        (-60,-85),(-40,-85),(-20,-85),(20,-85),(40,-85),(60,-85),
        (-40,-105),(-40,-125),(40,-105),(40,-125),(-60,-125),(-80,-125),(-100,-125),
        (-20,-125),(0,-125),(20,-125),(60,-125),(80,-125),(100,-125),
        (-140,-90),(-160,-90),(-180,-90),(-200,-90),(-200,-110),(-200,-130),(-180,-130),(-160,-130),
        (140,-90),(160,-90),(180,-90),(200,-90),(200,-110),(200,-130),(180,-130),(160,-130),
        (-80,-145),(-80,-165),(-60,-165),(-40,-165),(-20,-165),
        (80,-145),(80,-165),(60,-165),(40,-165),(20,-165),


        (200,-180),(200,-160),(180,-160),(160,-160),(140,-160),(120,-160),(120,-140),
        (120,-120),(120,-100),(120,-80),(120,-60),(120,-40),(120,-20),(120,0),(120,20),
        (120,40),(120,60),(120,80),(120,100),(120,120),(140,120),(160,120),(180,120),(200,120),
        (200,140),(200,160),(200,180),(200,200),(180,200),(160,200),(140,200),(120,200),(100,200),(80,200),(60,200),(40,200),(20,200),
        (20,180),(20,160),(20,140),(20,120),(40,120),(60,120),(80,120),(100,120),
        (40,160),(60,160),(80,160),(100,160),(120,160),(140,160),(160,160),(180,160),(130,180),(70,140),(50,140),
        (140,15),(160,15),(180,15),(200,15),
        (100,15),(80,15),(60,15),(80,-5),(80,-25),(80,-45),(80,-65),(80,-85),
        (80,40),(20,60),(20,80),(40,80),(60,80),(80,80)



]





def eat_food(pacman_x, pacman_y, pacman_radius, food, food_radius=2):
    global score,game_over_flag
    for i in food[:]:  # Loop over a copy of the list to avoid issues when modifying the list
        x, y = i
        distance = math.sqrt((pacman_x - x) ** 2 + (pacman_y - y) ** 2)
        if distance < food_radius + pacman_radius:
            food.remove(i)  # Remove the eaten food by value
            score += 1
            if score==227:
                game_over_flag=True
            return True
    return False




def check_wall_collision(x, y, maze_walls, pacman_radius):
    for wall in maze_walls:
        wall_type, x_start, y_start, x_end, y_end = wall
        if wall_type == "horizontal":
            if y_start - pacman_radius <= y <= y_start + pacman_radius and x_start <= x <= x_end:
                return True
        elif wall_type == "vertical":
            if x_start - pacman_radius <= x <= x_start + pacman_radius and y_start <= y <= y_end:
                return True
    return False




def draw_food(food,size):
    for i in food:
        x,y=i
        glColor3f(1,0.647,0)
        MidpointCircle(size,x,y)
        drawpoints(x,y,size)



def draw_maze(wall_list, size):
    glColor3f(0.0, 0.0, 1.0)  # Set wall color to blue
    for wall in wall_list:
        wall_type, x_start, y_start, x_end, y_end = wall
        if wall_type == "horizontal":
            draw_horizontal_wall(x_start, x_end, y_start, size)
        elif wall_type == "vertical":
            draw_vertical_wall(y_start, y_end, x_start, size)

def draw_horizontal_wall(x_start, x_end, y, size):
    Eight_way_symmetry(x_start, y, x_end, y,size)

def draw_vertical_wall(y_start, y_end, x, size):
    Eight_way_symmetry(x, y_start, x, y_end,size)




def pacman_move():
    global pacman_x, pacman_y,pacman_radius,score,food,play_button_flag

    new_x = pacman_x
    new_y = pacman_y
    if not play_button_flag:
        if pacman_up_flag:
            new_y += pacman_speed
        if pacman_down_flag:
            new_y -= pacman_speed
        if pacman_left_flag:
            new_x -= pacman_speed
        if pacman_right_flag:
            new_x += pacman_speed

    # Check for collision before updating position
    if not check_wall_collision(new_x, new_y, maze_walls, pacman_radius):
        pacman_x = new_x
        pacman_y = new_y

    eat_food(pacman_x,pacman_y,pacman_radius,food)

 




def keyBoardListerner(key,x,y):
    global game_over_flag,pacman_up_flag,pacman_down_flag,pacman_left_flag,pacman_right_flag

    if not game_over_flag:
        if key == b'a':
                pacman_left_flag = True
                
        elif key == b'd':
                pacman_right_flag = True
        elif key==b'w':
            pacman_up_flag = True
        elif key==b's':
            pacman_down_flag = True


def pacman_key_released(key, x, y):
    global pacman_up_flag,pacman_down_flag,pacman_left_flag,pacman_right_flag

    if key == b'a':
        pacman_left_flag = False
                
    if key == b'd':
        pacman_right_flag = False
    if key==b'w':
        pacman_up_flag = False
    if key==b's':
        pacman_down_flag = False




def MouseListerner(button,state,x,y):

    global restart_button_flag, cross_button_flag, play_button_flag

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        clicked_x = x - 250
        clicked_y = 250 - y
        print(f"Mouse clicked at OpenGL coordinates: ({clicked_x}, {clicked_y})")

        if (-240 <= clicked_x <= -210) and (220 <= clicked_y <= 240):
            restart_button_flag = True
            print('Restart!!')
        elif (220 <= clicked_x <= 240) and (220 <= clicked_y <= 240):
            cross_button_flag = True
        elif (-5 <= clicked_x <= 15) and (220 <= clicked_y <= 240):
            play_button_flag = not play_button_flag




def draw_pacman(x,y,radius):
    glColor3f(1,1,0)
    MidpointCircle(radius,x,y)
    for i in range(-radius, radius + 1):  # x-offset
        for j in range(-radius, radius + 1):  # y-offset
            # Check if the point lies inside the circle
            if i**2 + j**2 <= radius**2:
                glBegin(GL_POINTS)
                glVertex2f(x + i, y + j)
                glEnd()


def draw_score(score):
   
    glColor3f(0.0, 1.0, 0.0) 
    glRasterPos2f(100, 230) 
    
    score_str = f"Score: {score}"
    for char in score_str:
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(char))  

def timer(value):
    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()



def ShowScreen():
    global heart1_flag, heart2_flag, heart3_flag
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    draw_maze(maze_walls,size=5)
    draw_food(food,2)
    draw_pacman(pacman_x, pacman_y, pacman_radius)
    if game_over_flag:
        GameOver()
    if play_button_flag:
        glColor3f(0.95, 0.96, 0.03)
        draw_play_button()
    else:
        glColor3f(0.95, 0.96, 0.03)
        draw_pause_button()
    
    if cross_button_flag:
        draw_cross_button()
        print("GOODBYE..")
        glutLeaveMainLoop()
    draw_score(score)
    heart1()
    heart2()
    heart3()
    draw_cross_button()
    glColor3f(1,1,0)
    glColor3f(0,1,1)
    draw_restart_button()
    glutSwapBuffers()
    glutPostRedisplay()


glutInit()
glutInitDisplayMode(GLUT_RGBA)

glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)

window = glutCreateWindow(b"PacMan")
glutTimerFunc(0, timer, 0)
glutDisplayFunc(ShowScreen)
glutIdleFunc(pacman_move)
glutMouseFunc(MouseListerner)
glutKeyboardFunc(keyBoardListerner)
glutKeyboardUpFunc(pacman_key_released)
glutMainLoop()
