from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def find_zone(dx, dy):
    if abs(dx) <= abs(dy):
        if dx >= 0 and dy >= 0:
            return 1
        elif dx <= 0 and dy >= 0:
            return 2
        elif dx >= 0 and dy <= 0:
            return 6
        elif dx <= 0 and dy <= 0:
            return 5
    else:
        if dx >= 0 and dy >= 0:
            return 0
        elif dx <= 0 and dy >= 0:
            return 3
        elif dx >= 0 and dy <= 0:
            return 7
        elif dx <= 0 and dy <= 0:
            return 4


def convert_to_zone0(z, x, y):
    match z:
        case 0:
            return x, y
        case 1:
            return y, x
        case 2:
            return y, -x
        case 3:
            return -x, y
        case 4:
            return -x, -y
        case 5:
            return -y, -x
        case 6:
            return -y, x
        case 7:
            return x, -y


def convert_original(z, x, y):
    match z:
        case 0:
            return x, y
        case 1:
            return y, x
        case 2:
            return -y, x
        case 3:
            return -x, y
        case 4:
            return -x, -y
        case 5:
            return -y, -x
        case 6:
            return y, -x
        case 7:
            return x, -y


def midpointline(x1, y1, x2, y2, z):
    dx = x2 - x1
    dy = y2 - y1

    d = (2 * dy) - dx
    e = 2 * dy
    ne = 2 * (dy - dx)

    x = x1
    y = y1

    while x < x2:
        px, py = convert_original(z, x, y)
        draw_points(px, py)
        if d < 0:
            x += 1
            d += e
        else:
            x += 1
            y += 1
            d += ne


def draw_lines(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    zone = find_zone(dx, dy)

    px1, py1 = convert_to_zone0(zone, x1, y1)
    px2, py2 = convert_to_zone0(zone, x2, y2)

    midpointline(px1, py1, px2, py2, zone)


def draw_eight():
    draw_lines(300, 350, 400, 350)
    draw_lines(300, 150, 400, 150)
    draw_lines(300, 350, 300, 150)
    draw_lines(400, 150, 400, 350)
    draw_lines(300, 250, 400, 250)


def draw_nine():
    draw_lines(100, 350, 200, 350)
    draw_lines(100, 150, 200, 150)
    draw_lines(200, 350, 200, 150)
    draw_lines(100, 250, 100, 350)
    draw_lines(100, 250, 200, 250)


def draw_points(x, y):
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(255.0, 255.0, 255.0)
    draw_nine()
    draw_eight()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Student ID: 20101298 | Let's Draw: 98")
glutDisplayFunc(showScreen)

glutMainLoop()
