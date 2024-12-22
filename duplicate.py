from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

game_over_flag = False
play_button_flag = False
cross_button_flag = False
restart_button_flag = False
heart1_flag = False
heart2_flag = False
heart3_flag = False



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



def MidpointLine(zone,x0,y0,x1,y1):
    dx = x1-x0
    dy = y1-y0
    d = 2*dy-dx
    E = 2*dy
    NE = 2*(dy-dx)
    x = x0
    y = y0
    while x<x1:
        original_x,original_y = convert_to_originalzone(zone,x,y)
        drawpoints(original_x,original_y)
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




def Eight_way_symmetry(x0,y0,x1,y1):
    if x0==x1:
        for y in range(int(min(y0, y1)), int(max(y0, y1)) + 1):
            drawpoints(x0,y)
    elif y0==y1:
        for x in range(int(min(x0, x1)), int(max(x0, x1)) + 1):
            drawpoints(x,y0)
    else:
        zone = FindZone(x0,y0,x1,y1)
        coverted_x0,converted_y0 = convert_to_zone0(zone,x0,y0)
        coverted_x1,coverted_y1 = convert_to_zone0(zone,x1,y1)
        MidpointLine(zone,coverted_x0,converted_y0,coverted_x1,coverted_y1)



def draw_play_button():
    Eight_way_symmetry(-5, 240, 15, 230) 
    Eight_way_symmetry(-5, 240, -5, 220) 
    Eight_way_symmetry(-5, 220, 15, 230) 



def draw_pause_button():
    Eight_way_symmetry(-5, 240, -5, 220)
    Eight_way_symmetry(5, 240, 5, 220)


def draw_restart_button():
    Eight_way_symmetry(-240, 230, -210, 230)
    Eight_way_symmetry(-240, 230, -220, 240)
    Eight_way_symmetry(-240, 230, -220, 220)


def draw_cross_button():
    Eight_way_symmetry(240, 240, 220, 220)
    Eight_way_symmetry(220, 240, 240, 220)


def heart1():
    glColor3f(1.0, 0.0, 0.0)
    Eight_way_symmetry(220, 180, 232, 165) 
    Eight_way_symmetry(220, 180, 226, 187)
    Eight_way_symmetry(226, 187, 232, 180)
    Eight_way_symmetry(244, 180, 238, 187)
    Eight_way_symmetry(238, 187, 232, 180)
    Eight_way_symmetry(232, 165, 244, 180)
    Eight_way_symmetry(239, 187, 244, 180)

def heart2():
    glColor3f(1.0, 0.0, 0.0)
    Eight_way_symmetry(220, 140, 232, 125) 
    Eight_way_symmetry(220, 140, 226, 147)
    Eight_way_symmetry(226, 147, 232, 140)
    Eight_way_symmetry(244, 140, 238, 147)
    Eight_way_symmetry(238, 147, 232, 140)
    Eight_way_symmetry(232, 125, 244, 140)
    Eight_way_symmetry(239, 147, 244, 140)

def heart3():
    glColor3f(1.0, 0.0, 0.0)
    Eight_way_symmetry(220, 100, 232, 85) 
    Eight_way_symmetry(220, 100, 226, 107)
    Eight_way_symmetry(226, 107, 232, 100)
    Eight_way_symmetry(244, 100, 238, 107)
    Eight_way_symmetry(238, 107, 232, 100)
    Eight_way_symmetry(232, 85, 244, 100)
    Eight_way_symmetry(239, 107, 244, 100)



def GameOver():
    # G
    Eight_way_symmetry(-120, 50, -90, 50)  
    Eight_way_symmetry(-120, 50, -120, 10)  
    Eight_way_symmetry(-120, 10, -90, 10)  
    Eight_way_symmetry(-90, 10, -90, 30)  
    Eight_way_symmetry(-100, 30, -90, 30)  

    # A
    Eight_way_symmetry(-80, 10, -70, 50)  
    Eight_way_symmetry(-70, 50, -60, 10)  
    Eight_way_symmetry(-75, 30, -65, 30)  

    # M
    Eight_way_symmetry(-50, 10, -50, 50)  
    Eight_way_symmetry(-50, 50, -40, 30)  
    Eight_way_symmetry(-40, 30, -30, 50)  
    Eight_way_symmetry(-30, 50, -30, 10)  

    # E
    Eight_way_symmetry(-20, 10, -20, 50)  
    Eight_way_symmetry(-20, 50, -10, 50)  
    Eight_way_symmetry(-20, 30, -10, 30) 
    Eight_way_symmetry(-20, 10, -10, 10)  



    # O
    Eight_way_symmetry(0, 10, 0, 50)  
    Eight_way_symmetry(20, 10, 20, 50)  
    Eight_way_symmetry(0, 50, 20, 50)  
    Eight_way_symmetry(0, 10, 20, 10)  

    # V
    Eight_way_symmetry(30, 50, 40, 10)  
    Eight_way_symmetry(40, 10, 50, 50)  

    # E
    Eight_way_symmetry(60, 10, 60, 50)  
    Eight_way_symmetry(60, 50, 70, 50)  
    Eight_way_symmetry(60, 30, 70, 30)  
    Eight_way_symmetry(60, 10, 70, 10)  

    # R
    Eight_way_symmetry(80, 10, 80, 50)  
    Eight_way_symmetry(80, 50, 90, 50)  
    Eight_way_symmetry(90, 50, 90, 30)  
    Eight_way_symmetry(80, 30, 90, 30)  
    Eight_way_symmetry(80, 30, 91, 10)  



maze_walls = [
    # Outer boundary
    ("horizontal", -240, 240, 240, 240),
    ("horizontal", -240, -240, 240, -240),
    ("vertical", -240, -240, -240, 240),
    ("vertical", 240, -240, 240, 240),

    # Top-left section
    ("horizontal", -220, 200, -100, 200),
    ("vertical", -220, 200, -220, 100),
    ("horizontal", -220, 100, -160, 100),
    ("vertical", -160, 100, -160, 160),
    ("horizontal", -160, 160, -100, 160),
    ("vertical", -100, 200, -100, 160),
    ("horizontal", -200, 40, -160, 40),
    ("vertical", -160, 40, -160, 70),

    # Top-right section
    ("horizontal", 100, 200, 220, 200),
    ("vertical", 220, 200, 220, 100),
    ("horizontal", 160, 100, 200, 100),
    ("vertical", 160, 100, 160, 160),
    ("horizontal", 100, 160, 160, 160),
    ("vertical", 100, 200, 100, 160),
    ("horizontal", 160, 50, 200, 50),
    ("vertical", 200, 50, 200, 80),

    # Bottom-left section
    ("horizontal", -220, -200, -100, -200),
    ("vertical", -220, -200, -220, -100),
    ("horizontal", -220, -100, -160, -100),
    ("vertical", -160, -100, -160, -160),
    ("horizontal", -160, -160, -100, -160),
    ("vertical", -100, -200, -100, -160),
    ("horizontal", -200, -50, -160, -50),
    ("vertical", -180, -50, -180, -80),

    # Bottom-right section
    ("horizontal", 100, -200, 220, -200),
    ("vertical", 220, -200, 220, -100),
    ("horizontal", 160, -100, 220, -100),
    ("vertical", 160, -100, 160, -160),
    ("horizontal", 100, -160, 160, -160),
    ("vertical", 100, -200, 100, -160),
    ("horizontal", 160, -50, 200, -50),
    ("vertical", 200, -50, 200, -80),

    # Central region
    ("horizontal", -80, 20, 80, 20),
    ("vertical", -80, 20, -80, -20),
    ("horizontal", -20, -20, 20, -20),
    ("vertical", 80, 20, 80, -20),
    ("horizontal", -40, 49, 40, 49),
    ("horizontal", -65, -60, 65, -60),
    ("vertical", -40, 60, -40, 20),
    ("vertical", 40, 60, 40, 20),
    ("vertical", -65, -60, -65, -20),
    ("vertical", 65, -60, 65, -20),

    # Additional paths and dead ends
    ("horizontal", -200, 0, -140, 0),
    ("horizontal", 140, 0, 200, 0),
    # ("horizontal", -60, 120, 60, 120),
    ("horizontal", -60, -120, 60, -120),
    ("vertical",  0, -190,-5, -120),               #line isn't showing
    ("vertical", -120, 50, -120, -50),
    ("vertical", 120, 50, 120, -50),
    ("horizontal", -100, 80, 100, 80),
    ("vertical", -5, 80, -5, 160),
    # ("horizontal", 60, 80, 100, 80),
    ("horizontal", -100, -88, -55, -88),
    ("horizontal", 55, -88, 100, -88),
    ("vertical", -100, 80, -100, 40),
    ("vertical", 100, 80, 100, 40),
    ("vertical", -100, -88, -100, -45),
    ("vertical", 100, -88, 100, -45),
]





def draw_maze_from_list(wall_list, point_size=2):
    glColor3f(0.0, 0.0, 1.0)  # Set wall color to blue
    for wall in wall_list:
        wall_type, x_start, y_start, x_end, y_end = wall
        if wall_type == "horizontal":
            draw_horizontal_wall(x_start, x_end, y_start, point_size)
        elif wall_type == "vertical":
            draw_vertical_wall(y_start, y_end, x_start, point_size)


def draw_horizontal_wall(x_start, x_end, y, point_size=2):
    for x in range(x_start, x_end + 1):
        drawpoints(x, y, point_size)

def draw_vertical_wall(y_start, y_end, x, point_size=2):
    for y in range(y_start, y_end + 1):
        drawpoints(x, y, point_size)




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
    draw_maze_from_list(maze_walls)
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

    heart1()
    heart2()
    heart3()
    draw_cross_button()
    glColor3f(1,1,0)
    glColor3f(0,1,1)
    draw_restart_button()
    glutSwapBuffers()




glutInit()
glutInitDisplayMode(GLUT_RGBA)

glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)

window = glutCreateWindow(b"PacMan")
glutDisplayFunc(ShowScreen)
glutMouseFunc(MouseListerner)
glutMainLoop()
