import OpenGL.GLUT as GLUT
import OpenGL.GLU as GLU
import OpenGL.GL as GL
from sys import argv
from math import sin, cos, pi

# titulo da janela
titulo_tela = "Prisma de N lados"

# rotacao
botao_esquerdo = False
alpha = 0
beta = 0
delta_alpha = 0.7

# Translation vars
botao_direito = False
delta_x, delta_y, delta_z = 0, 0, 0
down_x, down_y = 0, 0

# cores
cores = (
    (0.509, 0.354, 0.094),
    (0.298, 0.719, 0.215),
    (0.984, 0.311, 0.550),
    (0, 0.758, 1)
)
cores_cima_baixo = (1, 1, 1)
cor_fundo = (0.1, 0.19, 0.719, 1)

# variaveis iniciais
vertices = 3
raio = 2
altura_prisma = 3
piramid_modifier = 1


def figure():
    vertices_poligonos = []
    angulo_faces = (2*pi)/vertices
    GL.glPushMatrix()
    GL.glTranslatef(0.0, 1.5, -10)
    GL.glRotatef(90, 1.0, 0.0, 0.0)

    # translacao e zoom
    GL.glTranslatef(delta_x, delta_y, delta_z)

    # rotacao
    GL.glRotatef(alpha, 0.0, 0.0, 1.0)  # X axis
    GL.glRotatef(beta, 0.0, 1.0, 0.0)  # Y axis

    # figura de baixo
    GL.glColor3fv(cores_cima_baixo)
    GL.glBegin(GL.GL_POLYGON)
    for i in range(vertices):
        x = raio * cos(i*angulo_faces)
        y = raio * sin(i*angulo_faces)
        vertices_poligonos += [(x, y)]
        GL.glVertex3f(x, y, 0.0)
    GL.glEnd()

    # figura de cima
    GL.glBegin(GL.GL_POLYGON)
    for x, y in vertices_poligonos:
        GL.glVertex3f(piramid_modifier*x, piramid_modifier*y, altura_prisma)
    GL.glEnd()

    # outros lados
    GL.glBegin(GL.GL_QUADS)
    for i in range(vertices):
        GL.glColor3fv(cores[i % 3])

        GL.glVertex3f(vertices_poligonos[i][0], vertices_poligonos[i][1], 0)
        GL.glVertex3f(
            piramid_modifier*vertices_poligonos[i][0], piramid_modifier*vertices_poligonos[i][1], altura_prisma)

        GL.glVertex3f(piramid_modifier*vertices_poligonos[(i+1) % vertices][0],
                      piramid_modifier*vertices_poligonos[(i+1) % vertices][1], altura_prisma)
        GL.glVertex3f(vertices_poligonos[(i+1) % vertices]
                      [0], vertices_poligonos[(i+1) % vertices][1], 0)
    GL.glEnd()
    GL.glPopMatrix()


def draw():
    global alpha, botao_esquerdo, botao_direito
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    figure()
    # Auto-Rotation
    alpha = alpha + delta_alpha
    GLUT.glutSwapBuffers()


def timer(i):
    GLUT.glutPostRedisplay()
    GLUT.glutTimerFunc(10, timer, 1)


def special_key_pressed(key, x, y):
    global vertices, piramid_modifier

    if (key == GLUT.GLUT_KEY_UP and vertices < 12):
        vertices += 1

    elif (key == GLUT.GLUT_KEY_DOWN and vertices > 3):
        vertices -= 1

    GLUT.glutPostRedisplay()


def key_pressed(key, x, y):
    global delta_alpha, piramid_modifier
    if key == b"\033":
        GLUT.glutLeaveMainLoop()

    # piramide
    elif key == b"p":
        if piramid_modifier == 1:
            piramid_modifier = 0.5
        else:
            piramid_modifier = 1

    # rotacao
    elif key == b" ":
        if delta_alpha == 0:
            delta_alpha = 0.5
        else:
            delta_alpha = 0

    GLUT.glutPostRedisplay()


def mouse_click(button, state, x, y):
    global down_x, down_y, botao_esquerdo, botao_direito, delta_y, piramid_modifier

    down_x, down_y = x, y

    botao_esquerdo = button == GLUT.GLUT_LEFT_BUTTON and state == GLUT.GLUT_DOWN
    botao_direito = button == GLUT.GLUT_RIGHT_BUTTON and state == GLUT.GLUT_DOWN

    # zoom
    if button == 3 and state == GLUT.GLUT_DOWN:
        delta_y += 1
    elif button == 4 and state == GLUT.GLUT_DOWN:
        delta_y -= 1

    # piramide
    elif button == GLUT.GLUT_MIDDLE_BUTTON and state == GLUT.GLUT_DOWN:
        if piramid_modifier == 1:
            piramid_modifier = 0.5
        else:
            piramid_modifier = 1

    GLUT.glutPostRedisplay()


def mouse_move(x, y):
    global alpha, beta, down_x, down_y, delta_x, delta_y, delta_alpha

    # girando
    if botao_esquerdo:
        delta_alpha = 0
        # alpha
        alpha -= ((x - down_x) / 4.0) * -1

        if alpha >= 360:
            alpha -= 360

        if alpha <= 0:
            alpha += 360

        # beta
        if alpha >= 180:
            beta += (y - down_y) / 4.0 * -1
        else:
            beta -= (y - down_y) / 4.0 * -1

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
    GL.glClearColor(*cor_fundo)
    # posicionando a camera
    GLU.gluPerspective(-45, window_width / window_height, 0.1, 100.0)
    GLUT.glutTimerFunc(10, timer, 1)
    GLUT.glutMainLoop()


if(__name__ == '__main__'):
    main()
