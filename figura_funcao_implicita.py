import OpenGL.GLUT as GLUT
import OpenGL.GLU as GLU
import OpenGL.GL as GL
from sys import argv
from math import sin, cos, pi

# titulo da tela
titulo_tela = "Figura com funcao implicita"

# rotacao
botao_esquerdo = False
alpha = 90.0
beta = 45.0
delta_alpha = 0.5

# translacao
botao_direito = False
delta_x, delta_y, delta_z = 0, 0, 0
down_x, down_y = 0, 0

background_color = (0.184, 0.211, 0.250, 1)

# variaveis
m, n = 100, 100
x0, y0 = -2, -2
xf, yf = 2, 2
dx, dy = (xf - x0)/m, (yf - y0)/n

# funcao implicita
def f(x, y):
    return x**2-y**2


def figure():
    GL.glPushMatrix()
    # translacao e zoom
    GL.glTranslatef(delta_x, delta_y, delta_z)

    # rotacao
    GL.glRotatef(alpha, 0.0, 1.0, 0.0)  # eixo x
    GL.glRotatef(beta, 0.0, 0.0, 1.0)  # eixo y

    # Figura
    for i in range(0, n):
        y = y0 + i*dy
        GL.glColor3f(1-(i/n), 0, i/n)
        GL.glBegin(GL.GL_QUAD_STRIP)
        for j in range(0, m):
            x = x0 + j*dx
            GL.glVertex3f(x, y, f(x, y))
            GL.glVertex3f(x, y+dy, f(x, y+dy))

        GL.glEnd()

    GL.glPopMatrix()


def draw():
    global alpha, botao_esquerdo, botao_direito

    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    figure()
    # rotacao propria
    alpha = alpha + delta_alpha
    GLUT.glutSwapBuffers()


def timer(i):
    GLUT.glutPostRedisplay()
    GLUT.glutTimerFunc(10, timer, 1)


def special_key_pressed(key, x, y):
    """
    Template.
    Use for Up, Down, Left and Right arrows.
    """
    pass


def key_pressed(key, x, y):
    global delta_alpha

    if key == b"\033":
        GLUT.glutLeaveMainLoop()

    # rotacao
    elif key == b" ":
        if delta_alpha == 0:
            delta_alpha = 0.5
        else:
            delta_alpha = 0


def mouse_click(button, state, x, y):
    global down_x, down_y, botao_esquerdo, botao_direito, delta_z
    down_x, down_y = x, y
    botao_esquerdo = button == GLUT.GLUT_LEFT_BUTTON and state == GLUT.GLUT_DOWN
    botao_direito = button == GLUT.GLUT_RIGHT_BUTTON and state == GLUT.GLUT_DOWN

    # zoom
    if button == 3 and state == GLUT.GLUT_DOWN:
        delta_z += 1
    elif button == 4 and state == GLUT.GLUT_DOWN:
        delta_z -= 1


def mouse_move(x, y):
    global alpha, beta, down_x, down_y, delta_x, delta_y, delta_alpha

    # girando
    if botao_esquerdo:
        delta_alpha = 0
        # alpha
        alpha += ((x - down_x) / 4.0) * -1

        if alpha >= 360:
            alpha -= 360

        if alpha <= 0:
            alpha += 360

        # beta
        if alpha >= 180:
            beta -= (y - down_y) / 4.0 * -1
        else:
            beta += (y - down_y) / 4.0 * -1

        if beta >= 360:
            beta -= 360

        if beta <= 0:
            beta += 360

    # virando
    if botao_direito:
        delta_x += -1 * (x - down_x) / 100.0
        delta_y += (y - down_y) / 100.0

    down_x, down_y = x, y

    GLUT.glutPostRedisplay()


def main():
    GLUT.glutInit(argv)
    GLUT.glutInitDisplayMode(
        GLUT.GLUT_DOUBLE | GLUT.GLUT_RGBA | GLUT.GLUT_DEPTH | GLUT.GLUT_MULTISAMPLE
    )

    # formatando a tela
    screen_width = GLUT.glutGet(GLUT.GLUT_SCREEN_WIDTH)
    screen_height = GLUT.glutGet(GLUT.GLUT_SCREEN_HEIGHT)
    window_width = round(2 * screen_width / 3)
    window_height = round(2 * screen_height / 3)

    GLUT.glutInitWindowSize(window_width, window_height)
    GLUT.glutInitWindowPosition(
        round((screen_width - window_width) /
              2), round((screen_height - window_height) / 2)
    )
    GLUT.glutCreateWindow(titulo_tela)
    GLUT.glutDisplayFunc(draw)
    # funcoes acessorias
    GLUT.glutSpecialFunc(special_key_pressed)
    GLUT.glutKeyboardFunc(key_pressed)
    GLUT.glutMouseFunc(mouse_click)
    GLUT.glutMotionFunc(mouse_move)
    # GL.glEnable(GL.GL_MULTISAMPLE)
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glClearColor(*background_color)
    # movimentando a camera
    GLU.gluPerspective(-45, window_width / window_height, 0.1, 100.0)
    GL.glTranslatef(0.0, 0.0, -10)
    GLUT.glutTimerFunc(10, timer, 1)
    GLUT.glutMainLoop()


if(__name__ == '__main__'):
    main()
