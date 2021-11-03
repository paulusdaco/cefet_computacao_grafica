from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import png
from pathlib import Path

# Ao inves de ESCAPE = 27, vamos usar:
ESCAPE = b'\033'

# Numero de GLUT p janelas
window = 0

# Rotacoes no cubo
xrot = yrot = zrot = 0.0
dx = 0.1
dy = 0
dz = 0


def LoadTextures():
    global texture
    texture = [glGenTextures(1)]
    ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[0])
    image_file = Path.cwd() / 'c:\\Users\\paulu\\Documents\\vs-code\\computacao-grafica\\textura\dado.png'
    print(image_file)
    reader = png.Reader(filename=image_file)
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo,
                 GL_UNSIGNED_BYTE, pixels.tolist())
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################


def InitGL(Width, Height):
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def ReSizeGLScene(Width, Height):
    if Height == 0:
        Height = 1
    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def DrawGLScene():
    global xrot, yrot, zrot, texture

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(0.5, 0.5, 0.5, 1.0)
    glTranslatef(0.0, 0.0, -5.0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glRotatef(zrot, 0.0, 0.0, 1.0)

    glBindTexture(GL_TEXTURE_2D, texture[0])
    glBegin(GL_QUADS)

    # Face (1)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glTexCoord2f(0.0, 1/2)
    glVertex3f(1.0, -1.0,  1.0)
    glTexCoord2f(1/3, 1/2)
    glVertex3f(1.0,  1.0,  1.0)
    glTexCoord2f(1/3, 0.0)
    glVertex3f(-1.0,  1.0,  1.0)

    # Face (6)
    glTexCoord2f(2/3, 1/2)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(2/3, 1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0,  1.0, -1.0)
    glTexCoord2f(1.0, 1/2)
    glVertex3f(1.0, -1.0, -1.0)

    # Face (4)
    glTexCoord2f(0.0, 1/2)
    glVertex3f(-1.0,  1.0, -1.0)
    glTexCoord2f(1/3, 1/2)
    glVertex3f(-1.0,  1.0,  1.0)
    glTexCoord2f(1/3, 1.0)
    glVertex3f(1.0,  1.0,  1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0,  1.0, -1.0)

    # Face (3)
    glTexCoord2f(2/3, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(2/3, 1/2)
    glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1/2)
    glVertex3f(1.0, -1.0,  1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0,  1.0)

    # Face (2)
    glTexCoord2f(1/3, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(1/3, 1/2)
    glVertex3f(1.0,  1.0, -1.0)
    glTexCoord2f(2/3, 1/2)
    glVertex3f(1.0,  1.0,  1.0)
    glTexCoord2f(2/3, 0.0)
    glVertex3f(1.0, -1.0,  1.0)

    # Face (5)
    glTexCoord2f(1/3, 1/2)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1/3, 1.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glTexCoord2f(2/3, 1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glTexCoord2f(2/3, 1/2)
    glVertex3f(-1.0,  1.0, -1.0)

    glEnd() # Desenhando o cubo

    xrot = xrot + 0.01 # rotacao eixo X
    yrot = yrot + 0.01 # rotacao eixo Y
    zrot = zrot + 0.01 # rotacao eixo X

    glutSwapBuffers()


def keyPressed(tecla, x, y):
    global dx, dy, dz
    if tecla == ESCAPE:
        glutLeaveMainLoop()
    elif tecla == b'x' or tecla == b'X':
        dx = 1.0
        dy = 0
        dz = 0
    elif tecla == b'y' or tecla == b'Y':
        dx = 0
        dy = 1.0
        dz = 0
    elif tecla == b'z' or tecla == b'Z':
        dx = 0
        dy = 0
        dz = 1.0


def teclaEspecialPressionada(tecla, x, y):
    global xrot, yrot, zrot, dx, dy, dz
    if tecla == GLUT_KEY_LEFT:
        print("ESQUERDA")
        xrot -= dx # rotacao eixo X
        yrot -= dy # rotacao eixo Y
        zrot -= dz
    elif tecla == GLUT_KEY_RIGHT:
        print("DIREITA")
        xrot += dx # rotacao eixo X
        yrot += dy # rotacao eixo Y
        zrot += dz
    elif tecla == GLUT_KEY_UP:
        print("CIMA")
    elif tecla == GLUT_KEY_DOWN:
        print("BAIXO")


def main():
    sys.argv = glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Dado com Textura")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(keyPressed)
    glutSpecialFunc(teclaEspecialPressionada)
    InitGL(640, 480)
    glutMainLoop()

main()
