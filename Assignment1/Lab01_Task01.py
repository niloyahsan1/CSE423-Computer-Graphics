from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


# =============================== #
'''
A House and Rain Day & Night by pressing D/N.  
Raindrops cannot be bent.
'''
# =============================== #


raindrops = []
W_Width, W_Height = 750, 750
background_Flag = False


def generateRains():
    arr = []
    global raindrops
    glutPostRedisplay()

    if random.random() < 100:
        raindrops.append([random.randint(-1000, 1000), 1000])

    for i in raindrops:
        i[1] -= 0.75
        if i[1] > -250:
            arr.append(i)
    raindrops = arr
    return raindrops

# ==========================================


def keyboardListener(key, x, y):
    global background_Flag

    if key == b'n':
        background_Flag = True
        print("It's Night!")
    elif key == b'd':
        background_Flag = False
        print("It's Day!")

    glutPostRedisplay()


def ghor():
    glLineWidth(4)

    glBegin(GL_QUADS)

    if background_Flag:
        glColor3f(1, 1, 1)  # house color
    else:
        glColor3f(0, 0, 0)  # house color

    # roof
    glVertex2d(-200, 60)
    glVertex2d(200, 60)
    glVertex2d(-200, 90)
    glVertex2d(200, 90)

    glVertex2d(-200, 60)
    glVertex2d(-200, 90)
    glVertex2d(200, 90)
    glVertex2d(200, 60)

    glEnd()

    glBegin(GL_LINES)

    # left wall
    glVertex2d(-170, 60)
    glVertex2d(-170, -100)
    # right wall
    glVertex2d(170, 60)
    glVertex2d(170, -100)
    # ground
    glVertex2d(170, -100)
    glVertex2d(-170, -100)

    # door left
    glVertex2d(-20, -10)
    glVertex2d(-20, -100)
    # door right
    glVertex2d(20, -10)
    glVertex2d(20, -100)
    # door top
    glVertex2d(-20, -10)
    glVertex2d(20, -10)

    # left janala
    # left part
    glVertex2d(-80, 20)
    glVertex2d(-80, -40)
    # right part
    glVertex2d(-110, 20)
    glVertex2d(-110, -40)
    # upper part
    glVertex2d(-80, 20)
    glVertex2d(-110, 20)
    # lower part
    glVertex2d(-80, -40)
    glVertex2d(-110, -40)

    # right janala
    # left part
    glVertex2d(80, 20)
    glVertex2d(80, -40)
    # right part
    glVertex2d(110, 20)
    glVertex2d(110, -40)
    # upper part
    glVertex2d(80, 20)
    glVertex2d(110, 20)
    # lower part
    glVertex2d(80, -40)
    glVertex2d(110, -40)

    glEnd()

    glLineWidth(1)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    if background_Flag:
        glClearColor(0, 0, 0, 0)
    else:
        glClearColor(1, 1, 1, 1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    glMatrixMode(GL_MODELVIEW)

    # ghor calling
    ghor()

    # rains
    raindrops = generateRains()
    glBegin(GL_LINES)
    glColor3f(0, 0, 1)

    for x, y in raindrops:
        glVertex2f(x, y)
        glVertex2f(x, y - 15)
    glEnd()

    glutSwapBuffers()


def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104, 1, 1, 1000.0)


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(1000, 100)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)

wind = glutCreateWindow(b"House in Rainning")
init()

glutDisplayFunc(display)

glutKeyboardFunc(keyboardListener)

glutMainLoop()
