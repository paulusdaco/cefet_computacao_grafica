import OpenGL.GLUT as GLUT
import OpenGL.GLU as GLU
import OpenGL.GL as GL
from sys import argv
from math import sin, cos, pi, sqrt

# Nome da janela
window_name = "Prismas com iluminacao"

# Background Color RGBA
background_color = (0.184, 0.211, 0.250, 1)

# Figure Vars
vertices = 3
radius = 2
prism_height = 3
piramid_modifier = 1
X = 0
Y = 1
Z = 2

# iluminação
count = 0
materials = [
    [(0.329412, 0.223529, 0.027451, 1.0), (0.780392, 0.568627, 0.113725, 1.0), (0.992157, 0.941176, 0.807843, 1.0), (27.8974)], # Brass
    [(0.2125, 0.1275, 0.054, 1.0), (0.714, 0.4284, 0.18144, 1.0), (0.393548, 0.271906, 0.166721, 1.0), (25.6)], # Bronze
    [(0.25, 0.148, 0.06475, 1.0), (0.4, 0.2368, 0.1036, 1.0), (0.774597, 0.458561, 0.200621, 1.0), (76.8)], # Polished bronze
    [(0.25, 0.25, 0.25, 1.0), (0.4, 0.4, 0.4, 1.0), (0.774597, 0.774597, 0.774597, 1.0), (76.8)], # Chrome
    [(0.19125, 0.0735, 0.0225, 1.0), (0.7038, 0.27048, 0.0828, 1.0), (0.256777, 0.137622, 0.086014,  1.0), (12.8)], # Copper
    [(0.2295, 0.08825, 0.0275, 1.0), (0.5508, 0.2118, 0.066, 1.0), (0.580594, 0.223257, 0.0695701,  1.0), (51.2)], # Polished copper
    [(0.24725, 0.1995, 0.0745, 1.0), (0.75164, 0.60648, 0.22648, 1.0), (0.628281, 0.555802, 0.366065, 1.0), (51.2)], # Gold
    [(0.24725, 0.2245, 0.0645, 1.0), (0.34615, 0.3143, 0.0903, 1.0), (0.797357, 0.723991, 0.208006, 1.0), (83.2)], # Polished gold
    [(0.105882, 0.058824, 0.113725, 1.0), (0.427451, 0.470588,  0.541176,  1.0), (0.333333,  0.333333,  0.521569,  1.0), (9.84615)], # Tin
    [(0.19225, 0.19225, 0.19225, 1.0), (0.50754, 0.50754,  0.50754,  1.0), (0.508273,  0.508273,  0.508273,  1.0), (51.2)], # Silver
    [(0.23125, 0.23125, 0.23125, 1.0), (0.2775,  0.2775,  0.2775,  1.0), (0.773911,  0.773911,  0.773911,  1.0), (89.6)], # Polished silver
    [(0.0215, 0.1745, 0.0215, 0.55), (0.07568, 0.61424, 0.07568, 0.55), (0.633, 0.727811, 0.633, 0.55), (76.8)], # Emerald
    [(0.135, 0.2225, 0.1575, 0.95), (0.54, 0.89, 0.63, 0.95), (0.316228, 0.316228, 0.316228, 0.95), (12.8)], #Jade
    [(0.05375, 0.05, 0.06625, 0.82), (0.18275, 0.17, 0.22525, 0.82), (0.332741, 0.328634, 0.346435, 0.82), (38.4)], #Obsidian
    [(0.25, 0.20725, 0.20725, 0.922), (1.0, 0.829, 0.829, 0.922), (0.296648, 0.296648, 0.296648, 0.922), (11.264)], # Perl
    [(0.1745, 0.01175,  0.01175,  0.55), (0.61424,  0.04136,  0.04136,  0.55), (0.727811,  0.626959,  0.626959,  0.55), (76.8)], # Ruby
    [(0.1, 0.18725, 0.1745, 0.8), (0.396, 0.74151, 0.69102, 0.8), (0.297254, 0.30829, 0.306678, 0.8), (12.8)], # Turquoise
    [(0.0, 0.0, 0.0, 1.0), (0.01, 0.01, 0.01, 1.0), (0.50, 0.50, 0.50, 1.0), (32.0)], # Black plastic
    [(0.0, 0.1, 0.06 , 1.0), (0.0, 0.50980392, 0.50980392, 1.0), (0.50196078, 0.50196078, 0.50196078, 1.0), (32.0)], # Cyan plastic
    [(0.0, 0.0, 0.0, 1.0), (0.1, 0.35, 0.1, 1.0), (0.45, 0.55, 0.45, 1.0), (32.0)], # Green plastic
    [(0.0, 0.0, 0.0, 1.0), (0.5, 0.0, 0.0, 1.0), (0.7, 0.6, 0.6, 1.0), (32.0)], # Red plastic
    [(0.0, 0.0, 0.0, 1.0), (0.55, 0.55, 0.55, 1.0), (0.70, 0.70, 0.70, 1.0), (32.0)], # White plastic
    [(0.0, 0.0, 0.0, 1.0), (0.5, 0.5, 0.0, 1.0), (0.60, 0.60, 0.50, 1.0), (32.0)], # Yellow plastic
    [(0.02,  0.02,  0.02,  1.0), (0.01,  0.01,  0.01,  1.0), (0.4,  0.4,  0.4,  1.0), (10.0)], # Black rubber
    [(0.0, 0.05, 0.05, 1.0), (0.4, 0.5, 0.5, 1.0), (0.04, 0.7, 0.7, 1.0), (10.0)], # Cyan rubber
    [(0.0, 0.05, 0.0, 1.0), (0.4, 0.5, 0.4, 1.0), (0.04, 0.7, 0.04, 1.0), (10.0) ], # Green rubber
    [(0.05, 0.0, 0.0, 1.0), (0.5, 0.4, 0.4, 1.0), (0.7, 0.04, 0.04, 1.0), (10.0)], # Red rubber
    [(0.05, 0.05, 0.05, 1.0), (0.5, 0.5, 0.5, 1.0), (0.7, 0.7, 0.7, 1.0), (10.0)], # White rubber
    [(0.05,  0.05,  0.0,  1.0), (0.5,  0.5,  0.4,  1.0), (0.7,  0.7,  0.04,  1.0), (10.0)] # Yellow rubber
]
#Fonte: http://www.it.hiof.no/~borres/j3d/explain/light/p-materials.html

# Funções
def calcula_normal(v0, v1, v2):
    U = (v2[X]-v0[X], v2[Y]-v0[Y], v2[Z]-v0[Z])
    V = (v1[X]-v0[X], v1[Y]-v0[Y], v1[Z]-v0[Z])
    N = ((U[Y]*V[Z]-U[Z]*V[Y]),(U[Z]*V[X]-U[X]*V[Z]),(U[X]*V[Y]-U[Y]*V[X]))
    normal_length = sqrt(N[X]*N[X]+N[Y]*N[Y]+N[Z]*N[Z])
    return (N[X]/normal_length, N[Y]/normal_length, N[Z]/normal_length)


def calcula_normal_invertida(v0, v1, v2):
    U = ( v2[X]-v0[X], v2[Y]-v0[Y], v2[Z]-v0[Z] )
    V = ( v1[X]-v0[X], v1[Y]-v0[Y], v1[Z]-v0[Z] )
    N = ( (U[Y]*V[Z]-U[Z]*V[Y]),(U[Z]*V[X]-U[X]*V[Z]),(U[X]*V[Y]-U[Y]*V[X]))
    normal_length = sqrt(N[X]*N[X]+N[Y]*N[Y]+N[Z]*N[Z])
    return (-N[X]/normal_length, -N[Y]/normal_length, -N[Z]/normal_length)


def figure():
    polygon_points = []
    faces_angle = (2*pi)/vertices
    GL.glPushMatrix()
    GL.glTranslatef(0.0, -1.0, 0.0)
    GL.glRotatef(-100,1.0,0.0,0.0)
  
    # Figura
    # Embaixo
    GL.glBegin(GL.GL_POLYGON)
    for i in range(vertices):
        x = radius * cos(i*faces_angle)
        y = radius * sin(i*faces_angle)
        polygon_points += [ (x,y) ]
        GL.glVertex3f(x,y,0.0)
    
    u = (polygon_points[0][0], polygon_points[0][1], 0)
    v = (polygon_points[1][0], polygon_points[1][1], 0)
    p = (polygon_points[2][0], polygon_points[2][1], 0)

    GL.glNormal3fv(calcula_normal_invertida(u,v,p))
    GL.glEnd()

    # Em cima
    GL.glBegin(GL.GL_POLYGON)
    for x,y in polygon_points:
        GL.glVertex3f(piramid_modifier*x,piramid_modifier*y, prism_height)
    
    u = (polygon_points[0][0], polygon_points[0][1], prism_height)
    v = (polygon_points[1][0], polygon_points[1][1], prism_height)
    p = (polygon_points[2][0], polygon_points[2][1], prism_height)

    GL.glNormal3fv(calcula_normal(u,v,p))
    GL.glEnd()

    # Lados, depende do numero de vertices
    GL.glBegin(GL.GL_QUADS)
    for i in range(vertices):
        u = (polygon_points[i][0],polygon_points[i][1],0)
        v = (piramid_modifier*polygon_points[i][0],piramid_modifier*polygon_points[i][1],prism_height)
        p = (piramid_modifier*polygon_points[(i+1)%vertices][0],piramid_modifier*polygon_points[(i+1)%vertices][1],prism_height)
        q = (polygon_points[(i+1)%vertices][0],polygon_points[(i+1)%vertices][1],0)

        GL.glNormal3fv(calcula_normal(u,v,q))
        
        GL.glVertex3fv(u)
        GL.glVertex3fv(v)
        GL.glVertex3fv(p)
        GL.glVertex3fv(q)
    GL.glEnd()
    GL.glPopMatrix()


def draw():
    global count
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    GL.glRotatef(2,1,3,0)

    # Materiais nas malhas
    if count % 150 == 0:
        GL.glMaterialfv(GL.GL_FRONT, GL.GL_AMBIENT, materials[(count+1)%len(materials)][0])
        GL.glMaterialfv(GL.GL_FRONT, GL.GL_DIFFUSE, materials[(count+1)%len(materials)][1])
        GL.glMaterialfv(GL.GL_FRONT, GL.GL_SPECULAR, materials[(count+1)%len(materials)][2])
        GL.glMaterialfv(GL.GL_FRONT, GL.GL_SHININESS, materials[(count+1)%len(materials)][3])
    count += 1

    figure()
    GLUT.glutSwapBuffers()


def timer(i):
    GLUT.glutPostRedisplay()
    GLUT.glutTimerFunc(50, timer, 1)


def special_key_pressed(key, x, y):
    global vertices
    if (key == GLUT.GLUT_KEY_UP and vertices < 12):
        vertices += 1

    elif (key == GLUT.GLUT_KEY_DOWN and vertices > 3):
        vertices -= 1
    
    GLUT.glutPostRedisplay()


def key_pressed(key, x, y):
    global piramid_modifier
    if key == b"\033":
        GLUT.glutLeaveMainLoop()

    # Toggles Piramid
    elif key == b"p":
        if piramid_modifier == 1:
            piramid_modifier = 0.5
        else:
            piramid_modifier = 1
    
    GLUT.glutPostRedisplay()


def mouse_click(button, state, x, y):
    global piramid_modifier

    # Piramide cortada ou nao
    if button == GLUT.GLUT_MIDDLE_BUTTON and state == GLUT.GLUT_DOWN:
        if piramid_modifier == 1:
            piramid_modifier = 0.5
        else:
            piramid_modifier = 1

    GLUT.glutPostRedisplay()


def mouse_move(x, y):
    """
    Template
    """


def reshape(w,h):
    GL.glViewport(0,0,w,h)
    GL.glMatrixMode(GL.GL_PROJECTION)
    GLU.gluPerspective(45, float(w) / float(h), 0.1, 50.0)
    GL.glMatrixMode(GL.GL_MODELVIEW)
    GL.glLoadIdentity()

    GLU.gluLookAt(10,0,0,0,0,0,0,1,0)
    

def main():    
    GLUT.glutInit(argv)
    GLUT.glutInitDisplayMode(
        GLUT.GLUT_DOUBLE | GLUT.GLUT_RGBA | GLUT.GLUT_DEPTH | GLUT.GLUT_MULTISAMPLE
    )

    # Tela com boa proporcao de resolucao
    screen_width = GLUT.glutGet(GLUT.GLUT_SCREEN_WIDTH)
    screen_height = GLUT.glutGet(GLUT.GLUT_SCREEN_HEIGHT)

    window_width = round(2 * screen_width / 3)
    window_height = round(2 * screen_height / 3)

    GLUT.glutInitWindowSize(window_width, window_height)
    GLUT.glutInitWindowPosition(
        round((screen_width - window_width) / 2), round((screen_height - window_height) / 2)
    )
    GLUT.glutCreateWindow(window_name)

    # Redimensionar figura
    GLUT.glutReshapeFunc(reshape)

    # Desenhar figura
    GLUT.glutDisplayFunc(draw)

    # Funcoes de teclado e mouse
    GLUT.glutSpecialFunc(special_key_pressed)
    GLUT.glutKeyboardFunc(key_pressed)
    GLUT.glutMouseFunc(mouse_click)
    GLUT.glutMotionFunc(mouse_move)
    
    #GL.glShadeModel(GL.GL_FLAT)
    GL.glShadeModel(GL.GL_SMOOTH)

    # Material de 1a execucao
    GL.glMaterialfv(GL.GL_FRONT, GL.GL_AMBIENT, materials[0][0])
    GL.glMaterialfv(GL.GL_FRONT, GL.GL_DIFFUSE, materials[0][1])
    GL.glMaterialfv(GL.GL_FRONT, GL.GL_SPECULAR, materials[0][2])
    GL.glMaterialfv(GL.GL_FRONT, GL.GL_SHININESS, materials[0][3])
    light_position = (10, 0, 0)
    GL.glEnable(GL.GL_LIGHTING)
    GL.glEnable(GL.GL_LIGHT0)
    GL.glLightfv(GL.GL_LIGHT0, GL.GL_POSITION, light_position)
    GL.glEnable(GL.GL_MULTISAMPLE)
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glClearColor(*background_color)

    # Pre-render camera positioning
    GLU.gluPerspective(45, window_width / window_height, 0.1, 50.0)

    GLUT.glutTimerFunc(50, timer, 1)
    GLUT.glutMainLoop()


if(__name__ == '__main__'):
    main()