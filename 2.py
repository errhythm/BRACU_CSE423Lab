from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random


def init():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    init()
    #call the draw methods here
    draw()
    glutSwapBuffers()

# put your drawing codes inside this 'draw' function
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(2)
    glLoadIdentity()

    glBegin(GL_LINES)
    glVertex2f(250, 350)
    glVertex2f(350, 250)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(350, 250)
    glVertex2f(150, 250)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(250, 350)
    glVertex2f(150, 250)
    glEnd()

    #Square
    glBegin(GL_LINES)
    glVertex2f(150,50)
    glVertex2f(150,250)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(350,250)
    glVertex2f(350,50)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(150,50)
    glVertex2f(350,50)
    glEnd()

    # Window 1
    glBegin(GL_LINES)
    glVertex2f(175, 225)
    glVertex2f(175, 175)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(175, 175)
    glVertex2f(225, 175)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(225, 175)
    glVertex2f(225, 225)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(175, 225)
    glVertex2f(225, 225)
    glEnd()

    # Window 2
    glBegin(GL_LINES)
    glVertex2f(275, 225)
    glVertex2f(275, 175)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(275, 175)
    glVertex2f(325, 175)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(325, 175)
    glVertex2f(325, 225)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(275, 225)
    glVertex2f(325, 225)
    glEnd()

    # Door
    glBegin(GL_LINES)
    glVertex2f(225, 50)
    glVertex2f(225, 125)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(275, 125)
    glVertex2f(225, 125)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(275, 125)
    glVertex2f(275, 50)
    glEnd()

    # Doorknob
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(262.5, 87.5)
    glEnd()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Lab Assignment 1 - Problem 2")
glutDisplayFunc(showScreen)

init()

glutMainLoop()