from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


def draw_points(x, y):
    glPointSize(1)
    glBegin(GL_POINTS)
    glColor3f(255, 255, 255)
    glVertex2f(x, y)
    glEnd()


# Starting from here

def zoneCircleConvert(x, y, x0, y0):
    draw_points(x + x0, y + y0)
    draw_points(y + x0, x + y0)
    draw_points(y + x0, -x + y0)
    draw_points(x + x0, -y + y0)
    draw_points(-x + x0, -y + y0)
    draw_points(-y + x0, -x + y0)
    draw_points(-y + x0, x + y0)
    draw_points(-x + x0, y + y0)


def midPoint(x0, y0, radius):
    d = 1 - radius
    x = 0
    y = radius
    zoneCircleConvert(x, y, x0, y0)
    while x < y:
        if d >= 0:
            d = d + 2 * x - 2 * y + 5
            x = x + 1
            y = y - 1
        else:
            d = d + 2 * x + 3
            x = x + 1
        zoneCircleConvert(x, y, x0, y0)


def eightWay(x, y, radius):
    midPoint(x, y, radius)

    midPoint(x + (radius / 2), y, radius / 2)
    midPoint(x, y + (radius / 2), radius / 2)
    midPoint(x, y - (radius / 2), radius / 2)
    midPoint(x - (radius / 2), y, radius / 2)

    x0 = x + (radius / 2) - 38
    y0 = y + (math.sin(45) * (radius / 2)) - 38
    midPoint(x0, y0, radius / 2)

    x0 = x + (radius / 2) - 38
    y0 = y - (math.sin(45) * (radius / 2)) + 38
    midPoint(x0, y0, radius / 2)

    x0 = x - (radius / 2) + 38
    y0 = y - (math.sin(45) * (radius / 2)) + 38
    midPoint(x0, y0, radius / 2)

    x0 = x - (radius / 2) + 38
    y0 = y + (math.sin(45) * (radius / 2)) - 38
    midPoint(x0, y0, radius / 2)


# Screen Files
def screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, -50.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    eightWay(475, 475, 350)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(768, 768)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Lab Assignment 3 - 20101298")
glutDisplayFunc(screen)
glutMainLoop()
