from OpenGL.GL import *
from glew_wish import *
import glfw
import math

class Fondo():
    def dibujar(self):

        glPushMatrix()
        glTranslatef(-.3,.43,0)

        glBegin(GL_POLYGON)
        glColor3f(221/255, 7/255, 7/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.05 * math.cos(angulo * math.pi / 180) , 0.045 * math.sin(angulo * math.pi / 180) -0, 0)
        glEnd()

        glPopMatrix()

        #ground
        glBegin(GL_QUADS)
        glColor3f(30/255, 69/255, 34/255)
        glVertex3f(-1.0,2.0,0.0)
        glVertex3f(1.0,2.0,0.0)
        glVertex3f(1.0,-2.0,0.0)
        glVertex3f(-1.0,-2.0,0.0)
        glEnd()

        #Calle
        glBegin(GL_QUADS)
        glColor3f(92/255,92/255,92/255)
        glVertex3f(-1.0,0.9,0.0)
        glVertex3f(1.0,0.9,0.0)
        glVertex3f(1.0,-0.9,0.0)
        glVertex3f(-1.0,-0.9,0.0)
        glEnd()

        #Banqueta
        glBegin(GL_QUADS)
        glColor3f(184/255, 186/255, 186/255)
        glVertex3f(-1.0,-0.30,0.0)
        glVertex3f(1.0,-0.30,0.0)
        glVertex3f(1.0,-0.40,0.0)
        glVertex3f(-1.0,-0.40,0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(184/255, 186/255, 186/255)
        glVertex3f(-1.0,0.30,0.0)
        glVertex3f(1.0,0.30,0.0)
        glVertex3f(1.0,0.40,0.0)
        glVertex3f(-1.0,0.40,0.0)
        glEnd()

        #Lineas calle
        glPushMatrix()
        glTranslatef(0,0,0)
        glBegin(GL_QUADS)
        glColor3f(255/255, 227/255, 11/255)
        glVertex3f(-1.0,0.025,0.0)
        glVertex3f(-0.8,0.025,0.0)
        glVertex3f(-0.8,-0.025,0.0)
        glVertex3f(-1.0,-0.025,0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(255/255, 227/255, 11/255)
        glVertex3f(-0.5,0.025,0.0)
        glVertex3f(-0.3,0.025,0.0)
        glVertex3f(-0.3,-0.025,0.0)
        glVertex3f(-0.5,-0.025,0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(255/255, 227/255, 11/255)
        glVertex3f(0.0,0.025,0.0)
        glVertex3f(0.2,0.025,0.0)
        glVertex3f(0.2,-0.025,0.0)
        glVertex3f(0.0,-0.025,0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(255/255, 227/255, 11/255)
        glVertex3f(0.5,0.025,0.0)
        glVertex3f(0.7,0.025,0.0)
        glVertex3f(0.7,-0.025,0.0)
        glVertex3f(0.5,-0.025,0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(255/255, 227/255, 11/255)
        glVertex3f(0.5,0.025,0.0)
        glVertex3f(0.7,0.025,0.0)
        glVertex3f(0.7,-0.025,0.0)
        glVertex3f(0.5,-0.025,0.0)
        glEnd()
        glPopMatrix()

        #Lineas calle
        glPushMatrix()
        glTranslatef(.1,-.67,0)
        glBegin(GL_QUADS)
        glColor3f(255/255, 255/255, 255/255)
        glVertex3f(-1.0,0.025,0.0)
        glVertex3f(-0.8,0.025,0.0)
        glVertex3f(-0.8,-0.025,0.0)
        glVertex3f(-1.0,-0.025,0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(255/255, 255/255, 255/255)
        glVertex3f(-0.5,0.025,0.0)
        glVertex3f(-0.3,0.025,0.0)
        glVertex3f(-0.3,-0.025,0.0)
        glVertex3f(-0.5,-0.025,0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(255/255, 255/255, 255/255)
        glVertex3f(0.0,0.025,0.0)
        glVertex3f(0.2,0.025,0.0)
        glVertex3f(0.2,-0.025,0.0)
        glVertex3f(0.0,-0.025,0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(255/255, 255/255, 255/255)
        glVertex3f(0.5,0.025,0.0)
        glVertex3f(0.7,0.025,0.0)
        glVertex3f(0.7,-0.025,0.0)
        glVertex3f(0.5,-0.025,0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(255/255, 255/255, 255/255)
        glVertex3f(0.5,0.025,0.0)
        glVertex3f(0.7,0.025,0.0)
        glVertex3f(0.7,-0.025,0.0)
        glVertex3f(0.5,-0.025,0.0)
        glEnd()
        glPopMatrix()

        #Lineas calle
        glPushMatrix()
        glTranslatef(.1,.67,0)
        glBegin(GL_QUADS)
        glColor3f(255/255, 255/255, 255/255)
        glVertex3f(-1.0,0.025,0.0)
        glVertex3f(-0.8,0.025,0.0)
        glVertex3f(-0.8,-0.025,0.0)
        glVertex3f(-1.0,-0.025,0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(255/255, 255/255, 255/255)
        glVertex3f(-0.5,0.025,0.0)
        glVertex3f(-0.3,0.025,0.0)
        glVertex3f(-0.3,-0.025,0.0)
        glVertex3f(-0.5,-0.025,0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(255/255, 255/255, 255/255)
        glVertex3f(0.0,0.025,0.0)
        glVertex3f(0.2,0.025,0.0)
        glVertex3f(0.2,-0.025,0.0)
        glVertex3f(0.0,-0.025,0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(255/255, 255/255, 255/255)
        glVertex3f(0.5,0.025,0.0)
        glVertex3f(0.7,0.025,0.0)
        glVertex3f(0.7,-0.025,0.0)
        glVertex3f(0.5,-0.025,0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(255/255, 255/255, 255/255)
        glVertex3f(0.5,0.025,0.0)
        glVertex3f(0.7,0.025,0.0)
        glVertex3f(0.7,-0.025,0.0)
        glVertex3f(0.5,-0.025,0.0)
        glEnd()
        glPopMatrix()

        #Baja
        glBegin(GL_QUADS)
        glColor3f(255/255, 255/255, 255/255)
        glVertex3f(-1.0,-0.070,0.0)
        glVertex3f(-0.8,-0.070,0.0)
        glVertex3f(-0.8,-0.085,0.0)
        glVertex3f(-1.0,-0.085,0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(255/255, 255/255, 255/255)
        glVertex3f(-1.0,-0.12,0.0)
        glVertex3f(-0.8,-0.12,0.0)
        glVertex3f(-0.8,-0.14,0.0)
        glVertex3f(-1.0,-0.14,0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(255/255, 255/255, 255/255)
        glVertex3f(-1.0,-0.18,0.0)
        glVertex3f(-0.8,-0.18,0.0)
        glVertex3f(-0.8,-0.20,0.0)
        glVertex3f(-1.0,-0.20,0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(255/255, 255/255, 255/255)
        glVertex3f(-1.0,-0.24,0.0)
        glVertex3f(-0.8,-0.24,0.0)
        glVertex3f(-0.8,-0.26,0.0)
        glVertex3f(-1.0,-0.26,0.0)
        glEnd()
        
        #Sube
        glBegin(GL_QUADS)
        glColor3f(255/255, 255/255, 255/255)
        glVertex3f(-1.0,0.070,0.0)
        glVertex3f(-0.8,0.070,0.0)
        glVertex3f(-0.8,0.085,0.0)
        glVertex3f(-1.0,0.085,0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(255/255, 255/255, 255/255)
        glVertex3f(-1.0,0.12,0.0)
        glVertex3f(-0.8,0.12,0.0)
        glVertex3f(-0.8,0.14,0.0)
        glVertex3f(-1.0,0.14,0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(255/255, 255/255, 255/255)
        glVertex3f(-1.0,0.18,0.0)
        glVertex3f(-0.8,0.18,0.0)
        glVertex3f(-0.8,0.20,0.0)
        glVertex3f(-1.0,0.20,0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(255/255, 255/255, 255/255)
        glVertex3f(-1.0,0.24,0.0)
        glVertex3f(-0.8,0.24,0.0)
        glVertex3f(-0.8,0.26,0.0)
        glVertex3f(-1.0,0.26,0.0)
        glEnd()

        #Alcantarillas
        glBegin(GL_POLYGON)
        glColor3f(143/255, 145/255, 148/255)
        for angulo in range(0,359,5):
            glVertex3f(0.06 * math.cos(angulo * math.pi / 180) - 0.3, 0.06 * math.sin(angulo * math.pi/180) + 0.58, 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(175/255, 176/255, 179/255)
        for angulo in range(0,359,5):
            glVertex3f(0.05 * math.cos(angulo * math.pi / 180) - 0.3, 0.05 * math.sin(angulo * math.pi/180) + 0.58, 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(143/255, 145/255, 148/255)
        for angulo in range(0,359,5):
            glVertex3f(0.06 * math.cos(angulo * math.pi / 180) + 0.3, 0.06 * math.sin(angulo * math.pi/180) - 0.58, 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(0/255, 0/255, 0/255)
        for angulo in range(0,359,5):
            glVertex3f(0.05 * math.cos(angulo * math.pi / 180) + 0.3, 0.05 * math.sin(angulo * math.pi/180) - 0.58, 0)
        glEnd()

        #arbol1
        glPushMatrix()
        glTranslatef(.3,.42,0)
        glBegin(GL_POLYGON)
        glColor3f(66/255, 193/255, 42/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.1 * math.cos(angulo * math.pi / 180) , 0.065 * math.sin(angulo * math.pi / 180) -.08, 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(66/255, 193/255, 42/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.065 * math.cos(angulo * math.pi / 180) , 0.09 * math.sin(angulo * math.pi / 180) -.08, 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(40/255, 121/255, 24/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.01 * math.cos(angulo * math.pi / 180) +.03, 0.01 * math.sin(angulo * math.pi / 180) -.09, 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(40/255, 121/255, 24/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.01 * math.cos(angulo * math.pi / 180) -.03, 0.01 * math.sin(angulo * math.pi / 180) -.01, 0)
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor3f(40/255, 121/255, 24/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.01 * math.cos(angulo * math.pi / 180) +0.05, 0.01 * math.sin(angulo * math.pi / 180) -.03, 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(40/255, 121/255, 24/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.01 * math.cos(angulo * math.pi / 180) -0.03, 0.01 * math.sin(angulo * math.pi / 180) -.05, 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(40/255, 121/255, 24/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.01 * math.cos(angulo * math.pi / 180) -0.07, 0.01 * math.sin(angulo * math.pi / 180) -.08, 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(40/255, 121/255, 24/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.01 * math.cos(angulo * math.pi / 180) +0.04, 0.01 * math.sin(angulo * math.pi / 180) -.06, 0)
        glEnd()
        glPopMatrix()

#arbol2
        glPushMatrix()
        glTranslatef(-.29,-.29,0)
        glBegin(GL_POLYGON)
        glColor3f(182/255, 204/255, 4/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.1 * math.cos(angulo * math.pi / 180) , 0.065 * math.sin(angulo * math.pi / 180) -.08, 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(182/255, 204/255, 4/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.065 * math.cos(angulo * math.pi / 180) , 0.09 * math.sin(angulo * math.pi / 180) -.08, 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(87/255, 95/255, 21/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.01 * math.cos(angulo * math.pi / 180) +.03, 0.01 * math.sin(angulo * math.pi / 180) -.09, 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(87/255, 95/255, 21/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.01 * math.cos(angulo * math.pi / 180) -.03, 0.01 * math.sin(angulo * math.pi / 180) -.01, 0)
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor3f(87/255, 95/255, 21/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.01 * math.cos(angulo * math.pi / 180) +0.05, 0.01 * math.sin(angulo * math.pi / 180) -.03, 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(87/255, 95/255, 21/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.01 * math.cos(angulo * math.pi / 180) +0.03, 0.01 * math.sin(angulo * math.pi / 180) -.05, 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(87/255, 95/255, 21/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.01 * math.cos(angulo * math.pi / 180) -0.02, 0.01 * math.sin(angulo * math.pi / 180) -.02, 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(87/255, 95/255, 21/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.01 * math.cos(angulo * math.pi / 180) -0.08, 0.01 * math.sin(angulo * math.pi / 180) -.05, 0)
        glEnd()
        glPopMatrix()

        #Buzón azul
        glBegin(GL_QUADS)
        glColor3f(61/255, 0/255, 198/255)
        glVertex3f(0.65,-0.31,0.0)
        glVertex3f(0.75,-0.31,0.0)
        glVertex3f(0.75,-0.37,0.0)
        glVertex3f(0.65,-0.37,0.0) 
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(138/255, 152/255, 161/255)
        for angulo in range(0,182,5):
            glVertex3f(-0.045 * math.cos(angulo * math.pi / 180) + 0.70, - 0.045 * math.sin(angulo * math.pi/180) - 0.31, 0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(236/255, 240/255, 12/255)
        glVertex3f(-0.79,0.31,0.0)
        glVertex3f(-0.83,0.31,0.0)
        glVertex3f(-0.83,0.37,0.0)
        glVertex3f(-0.79,0.37,0.0) 
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(38/255, 38/255, 36/255)
        for angulo in range(0,182,5):
            glVertex3f(-0.021 * math.cos(angulo * math.pi / 180) - 0.810, - 0.021 * math.sin(angulo * math.pi/180) + 0.31, 0)
        glEnd()

            #focos banqueta arriba
        #focos Izquierdo
        glBegin(GL_QUADS)
        glColor3f(84/255, 88/255, 89/255)
        glVertex3f(-0.85,0.31,0.0)
        glVertex3f(-0.9,0.31,0.0)
        glVertex3f(-0.9,0.37,0.0)
        glVertex3f(-0.85,0.37,0.0)

        #foco
        glColor3f(240/255, 242/255, 131/255)
        glVertex3f(-0.853,0.265,0.0)
        glVertex3f(-0.895,0.265,0.0)
        glVertex3f(-0.895,0.30,0.0)
        glVertex3f(-0.853,0.30,0.0)

        #tubo
        glColor3f(43/255, 45/255, 46/255)
        glVertex3f(-0.86,0.27,0.0)
        glVertex3f(-0.89,0.27,0.0)
        glVertex3f(-0.89,0.39,0.0)
        glVertex3f(-0.86,0.39,0.0)

        #foco derecho amarillo
        glColor3f(236/255, 240/255, 12/255)
        glVertex3f(0.85,0.31,0.0)
        glVertex3f(0.9,0.31,0.0)
        glVertex3f(0.9,0.37,0.0)
        glVertex3f(0.85,0.37,0.0)

        #foco
        glColor3f(237/255, 237/255, 237/255)
        glVertex3f(0.853,0.265,0.0)
        glVertex3f(0.895,0.265,0.0)
        glVertex3f(0.895,0.30,0.0)
        glVertex3f(0.853,0.30,0.0)

        #tubo
        glColor3f(211/255, 214/255, 26/255)
        glVertex3f(0.86,0.27,0.0)
        glVertex3f(0.89,0.27,0.0)
        glVertex3f(0.89,0.39,0.0)
        glVertex3f(0.86,0.39,0.0)

        glEnd()

        #focos banqueta abajo
        #Izquierdo amarillo
        glBegin(GL_QUADS)
        glColor3f(236/255, 240/255, 12/255)
        glVertex3f(-0.85,-0.33,0.0)
        glVertex3f(-0.9,-0.33,0.0)
        glVertex3f(-0.9,-0.39,0.0)
        glVertex3f(-0.85,-0.39,0.0)

        #foco
        glColor3f(237/255, 237/255, 237/255)
        glVertex3f(-0.853,-0.445,0.0)
        glVertex3f(-0.895,-0.445,0.0)
        glVertex3f(-0.895,-0.40,0.0)
        glVertex3f(-0.853,-0.40,0.0)

        #tubo
        glColor3f(211/255, 214/255, 26/255)
        glVertex3f(-0.86,-0.31,0.0)
        glVertex3f(-0.89,-0.31,0.0)
        glVertex3f(-0.89,-0.44,0.0)
        glVertex3f(-0.86,-0.44,0.0)

        #Derecho
        glColor3f(84/255, 88/255, 89/255)
        glVertex3f(0.85,-0.33,0.0)
        glVertex3f(0.9,-0.33,0.0)
        glVertex3f(0.9,-0.39,0.0)
        glVertex3f(0.85,-0.39,0.0)

        #foco
        glColor3f(240/255, 242/255, 131/255)
        glVertex3f(0.853,-0.445,0.0)
        glVertex3f(0.895,-0.445,0.0)
        glVertex3f(0.895,-0.40,0.0)
        glVertex3f(0.853,-0.40,0.0)

        #tubo
        glColor3f(43/255, 45/255, 46/255)
        glVertex3f(0.86,-0.31,0.0)
        glVertex3f(0.89,-0.31,0.0)
        glVertex3f(0.89,-0.44,0.0)
        glVertex3f(0.86,-0.44,0.0)

        glEnd()

            #petalos
        glBegin(GL_POLYGON)
        glColor3f(214/255, 214/255, 214/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.04 * math.cos(angulo * math.pi / 180) + 0.15, 0.012 * math.sin(angulo * math.pi / 180) -0.95, 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(214/255, 214/255, 214/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.012 * math.cos(angulo * math.pi / 180) + 0.15, 0.04 * math.sin(angulo * math.pi / 180) -0.95, 0)
        glEnd()

        #centro
        glBegin(GL_POLYGON)
        glColor3f(128/255, 112/255, 62/255)
        for angulo in range(0,359,5):
            glVertex3f(0.012 * math.cos(angulo * math.pi / 180) + 0.15, 0.012 * math.sin(angulo * math.pi/180) -0.95, 0)
        glEnd()

        #petalos
        glBegin(GL_POLYGON)
        glColor3f(214/255, 214/255, 214/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.04 * math.cos(angulo * math.pi / 180) - 0.3, 0.012 * math.sin(angulo * math.pi / 180) +0.95, 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(214/255, 214/255, 214/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.012 * math.cos(angulo * math.pi / 180) - 0.3, 0.04 * math.sin(angulo * math.pi / 180) +0.95, 0)
        glEnd()

        #centro
        glBegin(GL_POLYGON)
        glColor3f(128/255, 112/255, 62/255)
        for angulo in range(0,359,5):
            glVertex3f(0.012 * math.cos(angulo * math.pi / 180) - 0.3, 0.012 * math.sin(angulo * math.pi/180) +0.95, 0)
        glEnd()

        

            #Buzón rojo
        glBegin(GL_QUADS)
        glColor3f(235/255, 64/255, 52/255)
        glVertex3f(-0.65,0.31,0.0)
        glVertex3f(-0.75,0.31,0.0)
        glVertex3f(-0.75,0.37,0.0)
        glVertex3f(-0.65,0.37,0.0) 
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(138/255, 152/255, 161/255)
        for angulo in range(0,182,5):
            glVertex3f(0.045 * math.cos(angulo * math.pi / 180) - 0.70, 0.045 * math.sin(angulo * math.pi/180) + 0.31, 0)
        glEnd()

        