from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


'''
"Group Members":                
Niloy Ahsan (21101255)        
Abid Mashrafi (21101075)      
Chaity Rani Ghosh (21101191   
'''

# ================================================================================= #
'''
Save the Ball from Obstacles. Ball Runner Game.
A Diamond was a Power Up for slow down the speed. But the Diamond is not falling.
'''
# ================================================================================= #


WINDOW_WIDTH = 400
WINDOW_HEIGHT = 900
WIN_POS_X = 1400
WIN_POS_Y = 50


obs_flag = 0
diamond_flag = 0
pause_flag = False
game_over_flag = 3
print("Lives Left = ", game_over_flag)

reset_flag = False
cross_flag = False

gameScore = 0

life_circle = 3

circle_init_radus = 200
circle_bound_X = 185
circle_bound_Y = 25

diamond_Y = WINDOW_HEIGHT + 400
diamond_speed = 5

obs_Y = WINDOW_HEIGHT + 400
right_obs_Y = WINDOW_HEIGHT

obs_fall_speed = 5


# MAIN MID POINT ALGORITHM
def MidPointLine(zone, x1, y1, x2, y2):
    dx = (x2-x1)
    dy = (y2-y1)
    x = x1
    y = y1

    dInitial = 2*dy - dx

    Del_E = 2*dy
    Del_NE = 2*(dy-dx)

    while x <= x2:
        a, b = ConvertToOriginal(zone, x, y)
        drawpoints(a, b)

        if dInitial <= 0:
            x = x + 1
            dInitial = dInitial + Del_E
        else:
            x = x + 1
            y = y + 1
            dInitial = dInitial + Del_NE


def FindZone(x1, y1, x2, y2):
    dx = (x2-x1)
    dy = (y2-y1)

    if abs(dx) > abs(dy):
        if dx > 0 and dy > 0:
            return 0
        elif dx < 0 and dy > 0:
            return 3
        elif dx < 0 and dy < 0:
            return 4
        else:
            return 7
    else:
        if dx > 0 and dy > 0:
            return 1
        elif dx < 0 and dy > 0:
            return 2
        elif dx < 0 and dy < 0:
            return 5
        else:
            return 6


def ConvertToZoneZero(zone, x, y):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y


def ConvertToOriginal(zone, x, y):
    if zone == 0:
        return x, y
    if zone == 1:
        return y, x
    if zone == 2:
        return -y, x
    if zone == 3:
        return -x, y
    if zone == 4:
        return -x, -y
    if zone == 5:
        return -y, -x
    if zone == 6:
        return y, -x
    if zone == 7:
        return x, -y


def DrawLine(x1, y1, x2, y2):
    zone = FindZone(x1, y1, x2, y2)
    x1, y1 = ConvertToZoneZero(zone, x1, y1)
    x2, y2 = ConvertToZoneZero(zone, x2, y2)
    MidPointLine(zone, x1, y1, x2, y2)


# midpoint circle algorithm
def MidPointCircle(cx, cy, radius):
    d = (1 - radius)
    x = 0
    y = radius

    CirclePoints(x, y, cx, cy)

    while x < y:
        if d < 0:
            d = d + 2 * x + 3
            x = x + 1
        else:
            d = d + 2 * x - 2 * y + 5
            x = x + 1
            y = y - 1

        CirclePoints(x, y, cx, cy)


# circle at x,y coordinate and cx,cy center
def CirclePoints(x, y, cx, cy):

    glVertex2f(x + cx, y + cy)
    glVertex2f(y + cx, x + cy)

    glVertex2f(y + cx, -x + cy)
    glVertex2f(x + cx, -y + cy)

    glVertex2f(-x + cx, -y + cy)
    glVertex2f(-y + cx, -x + cy)

    glVertex2f(-y + cx, x + cy)
    glVertex2f(-x + cx, y + cy)


# THE CONTROLLING BUTTONS
def back_button():
    DrawLine(10, 90, 20, 100)
    DrawLine(10, 90, 20, 80)
    DrawLine(10, 90, 40, 90)


def cross_button():
    DrawLine(350, 80, 370, 100)
    DrawLine(350, 100, 370, 80)


# KEYBOARD CONTROL
def KeyboardListener(key, x, y):
    global pause_flag

    if key == b" ":
        pause_flag = not pause_flag
    print("Pause/Play", pause_flag)


def specialKeyboardListener(key, x, y):
    global catcherX, circle_init_radus, circle_bound_X

    if not pause_flag:
        if key == GLUT_KEY_LEFT:
            circle_init_radus = circle_init_radus - 28
            circle_bound_X = circle_bound_X - 28
        elif key == GLUT_KEY_RIGHT:
            circle_init_radus = circle_init_radus + 28
            circle_bound_X = circle_bound_X + 28

    circle_init_radus = max(115, min(285, circle_init_radus))
    circle_bound_X = max(100, min(270, circle_bound_X))


# MOUSE CONTROL
def mouseListener(button, state, x, y):
    global reset_flag, cross_flag, gameScore

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if 10 <= x <= 40 and (WINDOW_HEIGHT-100) <= y <= (WINDOW_HEIGHT-80):
            reset_flag = True
            print("Clicked Reset Button")
        elif 350 <= x <= 370 and (WINDOW_HEIGHT-100) <= y <= (WINDOW_HEIGHT-80):
            cross_flag = True
            print("Clicked Exit Button")


# TIMER FOR 60 FPS
def timer(value):
    glutPostRedisplay()
    glutTimerFunc(13, timer, 0)
    glutPostRedisplay()

# ===============================================================================================

# circle boundary BOX


def crl_boundary():
    glColor3f(0, 0, 0)
    global circle_bound_X, circle_bound_Y
    DrawLine(circle_bound_X, circle_bound_Y, circle_bound_X+30, circle_bound_Y)
    # uypper line
    DrawLine(circle_bound_X, circle_bound_Y+30,
             circle_bound_X+30, circle_bound_Y+30)
    DrawLine(circle_bound_X, circle_bound_Y,
             circle_bound_X+0.1, circle_bound_Y+30)
    DrawLine(circle_bound_X+30, circle_bound_Y,
             circle_bound_X+30.1, circle_bound_Y+30)


# road
def road():
    glColor3f(1, 1, 0)
    DrawLine(98, 0, 98.1, WINDOW_HEIGHT)
    DrawLine(302, 0, 302.1, WINDOW_HEIGHT)

# diamond fall for power


def diamond_power():
    glColor3f(0, 1, 0)
    global diamond_Y, diamond_speed
    DrawLine(190, diamond_Y + 45, 200, diamond_Y + 30)
    DrawLine(200, diamond_Y + 30, 210, diamond_Y + 45)
    DrawLine(210, diamond_Y + 45, 200, diamond_Y + 60)
    DrawLine(200, diamond_Y + 60, 190, diamond_Y + 45)

    if gameScore == 7:
        diamond_flag == True
    if gameScore == 14:
        diamond_flag == True

    if game_over_flag != 0 and diamond_flag == True:
        diamond_Y = (diamond_Y - diamond_speed)
        print(diamond_speed)
    else:
        diamond_Y = diamond_Y

    if (190 < circle_bound_X < 210 and diamond_Y+45 < circle_bound_Y < diamond_Y+60):

        obs_fall_speed = obs_fall_speed - 1
        diamond_speed = diamond_speed + 0.5
        diamond_Y = WINDOW_HEIGHT + 400
        diamond_flag == False
        print("Speed Slow Down!")

        if game_over_flag == 0:
            diamond_flag == False
            diamond_speed = 0
            diamond_Y = WINDOW_HEIGHT + 400

    elif diamond_Y+1000 < 0:
        diamond_flag == False
        diamond_Y = WINDOW_HEIGHT + 400

    # print(diamond_Y)


# RoadSide Obstacles
def block_1():
    global obs_Y, obs_fall_speed, obs_flag, gameScore, game_over_flag
    glColor3f(1, 0, 0)
    DrawLine(100, obs_Y+100, 200, obs_Y+100)
    DrawLine(200, obs_Y+100, 200, obs_Y)
    DrawLine(100, obs_Y, 200, obs_Y)
    DrawLine(100, obs_Y+100, 100, obs_Y)

    if game_over_flag != 0 and not pause_flag:
        obs_Y = obs_Y - obs_fall_speed
    else:
        obs_Y = obs_Y

    if (200 > circle_bound_X and
            100 < circle_bound_X+30 and
            obs_Y < circle_bound_Y and
            obs_Y+100 > circle_bound_Y+30
        ):

        game_over_flag = game_over_flag - 1
        print("Lives Left = ", game_over_flag)
        obs_flag = 1
        obs_Y = WINDOW_HEIGHT + 400

        if game_over_flag == 0:
            obs_fall_speed = 0
            totalScore = gameScore
            gameScore = 0
            print("=============================")
            print("Game Over!")
            print("Total Score: ", totalScore)

    elif obs_Y + 100 < 0:
        obs_flag = 1
        obs_Y = WINDOW_HEIGHT + 400
        gameScore = gameScore + 1
        obs_fall_speed = obs_fall_speed + 0.5
        print("gameScore = ", gameScore)


def block_2():
    global obs_Y, obs_fall_speed, obs_flag, gameScore, game_over_flag
    glColor3f(1, 0, 0)
    DrawLine(200, obs_Y+100, 300, obs_Y+100)
    DrawLine(300, obs_Y+100, 300, obs_Y)
    DrawLine(200, obs_Y, 300, obs_Y)
    DrawLine(200, obs_Y+100, 200, obs_Y)

    if game_over_flag != 0 and not pause_flag:
        obs_Y = obs_Y - obs_fall_speed
    else:
        obs_Y = obs_Y

    if (200 < circle_bound_X < 300 and obs_Y < circle_bound_Y < obs_Y+100):

        game_over_flag = game_over_flag - 1
        print("Lives Left = ", game_over_flag)
        obs_flag = 2
        obs_Y = WINDOW_HEIGHT + 400

        if game_over_flag == 0:
            obs_fall_speed = 0
            totalScore = gameScore
            gameScore = 0
            print("=============================")
            print("Game Over!")
            print("Total Score: ", totalScore)

    elif obs_Y + 100 < 0:
        obs_flag = 2
        obs_Y = WINDOW_HEIGHT + 400
        gameScore = gameScore + 1
        obs_fall_speed = obs_fall_speed + 0.5
        print("gameScore = ", gameScore)


def block_3():
    glColor3f(1, 0, 0)
    global obs_Y, obs_fall_speed, obs_flag, gameScore, game_over_flag
    DrawLine(250, obs_Y+100, 300, obs_Y+100)
    DrawLine(300, obs_Y+100, 300, obs_Y)
    DrawLine(250, obs_Y, 300, obs_Y)
    DrawLine(250, obs_Y+100, 250, obs_Y)

    if game_over_flag != 0 and not pause_flag:
        obs_Y = obs_Y - obs_fall_speed
    else:
        obs_Y = obs_Y

    if 250 < circle_bound_X < 300 and obs_Y < circle_bound_Y < obs_Y+100:

        game_over_flag = game_over_flag - 1
        print("Lives Left = ", game_over_flag)
        obs_flag = 3
        obs_Y = WINDOW_HEIGHT + 400

        if game_over_flag == 0:
            obs_fall_speed = 0
            totalScore = gameScore
            gameScore = 0
            print("=============================")
            print("Game Over!")
            print("Total Score: ", totalScore)

    elif obs_Y + 100 < 0:
        obs_flag = 3
        obs_Y = WINDOW_HEIGHT + 400
        gameScore = gameScore + 1
        obs_fall_speed = obs_fall_speed + 0.5
        print("gameScore = ", gameScore)


def block_4():
    glColor3f(1, 0, 0)
    global obs_Y, obs_fall_speed, obs_flag, gameScore, game_over_flag
    DrawLine(100, obs_Y + 100, 200, obs_Y + 100)
    DrawLine(200, obs_Y + 100, 200, obs_Y)
    DrawLine(100, obs_Y, 200, obs_Y)
    DrawLine(100, obs_Y + 100, 100, obs_Y)

    if game_over_flag != 0 and not pause_flag:
        obs_Y = obs_Y - obs_fall_speed
    else:
        obs_Y = obs_Y

    if 100 < circle_bound_X < 200 and obs_Y < circle_bound_Y < obs_Y+100:

        game_over_flag = game_over_flag - 1
        print("Lives Left = ", game_over_flag)
        obs_flag = 4
        obs_Y = WINDOW_HEIGHT + 400

        if game_over_flag == 0:
            totalScore = gameScore
            gameScore = 0
            print("=============================")
            print("Game Over!")
            print("Total Score: ", totalScore)

    elif obs_Y + 100 < 0:
        obs_flag = 4
        obs_Y = WINDOW_HEIGHT + 400
        gameScore = gameScore + 1
        obs_fall_speed = obs_fall_speed + 0.5
        print("gameScore = ", gameScore)


def block_5():
    glColor3f(1, 0, 0)
    global obs_Y, obs_fall_speed, obs_flag, gameScore, game_over_flag
    DrawLine(250, obs_Y+100, 300, obs_Y+100)
    DrawLine(300, obs_Y+100, 300, obs_Y)
    DrawLine(250, obs_Y, 300, obs_Y)
    DrawLine(250, obs_Y+100, 250, obs_Y)

    if game_over_flag != 0 and not pause_flag:
        obs_Y = obs_Y - obs_fall_speed
    else:
        obs_Y = obs_Y

    if 250 < circle_bound_X < 300 and obs_Y < circle_bound_Y < obs_Y+100:

        game_over_flag = game_over_flag - 1
        print("Lives Left = ", game_over_flag)
        obs_flag = 0
        obs_Y = WINDOW_HEIGHT + 400

        if game_over_flag == 0:
            totalScore = gameScore
            gameScore = 0
            print("=============================")
            print("Game Over!")
            print("Total Score: ", totalScore)

    elif obs_Y + 100 < 0:
        obs_flag = 0
        obs_Y = WINDOW_HEIGHT + 400
        gameScore = gameScore + 1
        obs_fall_speed = obs_fall_speed + 0.5
        print("gameScore = ", gameScore)


# ===============================================================================================


# creating the point (pixel)
def point_create():
    glColor3f(0.447, 1.0, 0.973)
    glPointSize(2)
    glBegin(GL_POINTS)
    #  circle should be between 125 and 275
    # MidPointCircle(125, 40, 20)
    # MidPointCircle(275, 40, 20)
    MidPointCircle(circle_init_radus, 40, 10)

    if game_over_flag == 3:
        glColor3f(0, 1, 0)
        MidPointCircle(350, 300, life_circle)
        MidPointCircle(360, 300, life_circle)
        MidPointCircle(370, 300, life_circle)
    elif game_over_flag == 2:
        glColor3f(1, 0.5, 0)
        MidPointCircle(350, 300, life_circle)
        MidPointCircle(360, 300, life_circle)
    elif game_over_flag == 1:
        glColor3f(1, 0, 0)
        MidPointCircle(350, 300, life_circle)
    elif game_over_flag == 0:
        MidPointCircle(0, 0, life_circle)
    glEnd()
# ===============================================================================


def drawpoints(x, y):
    glPointSize(1)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def iterate():
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    glOrtho(0.0, WINDOW_WIDTH, 0.0, WINDOW_HEIGHT, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    global diamondY, gameScore, obs_fall_speed
    if reset_flag:
        glColor3f(0, 0, 1)
        back_button()
        diamondY = WINDOW_HEIGHT
        gameScore = 0
    else:
        glColor3f(0, 0, 1)
        back_button()

    if cross_flag:
        cross_button()
        glutLeaveMainLoop()
    else:
        glColor3f(1, 0, 0)
        cross_button()

    # diamond
    # if gameScore == 5:
    #     glColor3f(0, 1, 0)
    #     diamond_power()
    # elif gameScore == 10:
    #     glColor3f(0, 1, 0)
    #     diamond_power()
    # elif gameScore == 20:
    #     glColor3f(0, 1, 0)
    #     diamond_power()
# ====================================================================
    glColor3f(1, 1, 1)
    road()
    crl_boundary()
    point_create()
    # global obs_flag, pause_flag
    # if not pause_flag:
    if obs_flag == 0:
        block_2()
    elif obs_flag == 1:
        block_1()
    elif obs_flag == 2:
        block_3()
    elif obs_flag == 3:
        block_4()
    elif obs_flag == 4:
        block_5()

    # if not pause_flag:
    #     if gameScore == 7 or gameScore == 14 or gameScore == 21:
    glColor3f(0, 1, 0)
    diamond_power()

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)

glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
glutInitWindowPosition(WIN_POS_X, WIN_POS_Y)

wind = glutCreateWindow(b"Project: Ball Runner")
glutTimerFunc(0, timer, 0)

glutMouseFunc(mouseListener)
glutKeyboardFunc(KeyboardListener)
glutSpecialFunc(specialKeyboardListener)
glutDisplayFunc(display)

glutMainLoop()
