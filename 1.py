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
    glBegin(GL_POINTS)
    for i in range(50):
        glVertex2d(random.randint(0, 500), random.randint(0, 500))
    glEnd()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Lab Assignment 1 - Problem 1")
glutDisplayFunc(showScreen)

init()

glutMainLoop()