from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


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
    glColor3d(0,1,1)
    glBegin(GL_TRIANGLES)
    glVertex2d(250,300)
    glVertex2d(300,200)
    glVertex2d(200,200)
    glEnd()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"OpenGL Coding Practice")
glutDisplayFunc(showScreen)

init()

glutMainLoop()