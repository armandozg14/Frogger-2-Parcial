from OpenGL.GL import *
from glew_wish import *
import glfw
import math
from Modelo import *

class Mosca(Modelo):
    posicion_mosca = [0,-1,0]
    angulo = 0
    fase= 90
    def __init__(self):
        super().__init__(posicion_x=0, posicion_y=-1, posicion_z=0)
        
    def actualizar(self, tiempo_delta):
        cantidad_movimiento = 0.6 * tiempo_delta
        self.posicion_x = self.posicion_x + (math.cos((self.angulo + self.fase) * math.pi/ 180)  * cantidad_movimiento )
        self.posicion_y = self.posicion_y + (math.sin((self.angulo + self.fase) * math.pi/ 180)  * cantidad_movimiento )

        self.angulo = self.angulo + 0.2

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posicion_x, self.posicion_y, 0)
        glBegin(GL_POLYGON)
        glColor3f(31/255, 31/255, 31/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.02 * math.cos(angulo * math.pi / 180) , 0.025 * math.sin(angulo * math.pi / 180) -.08, 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(147/255, 234/255, 249/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.025 * math.cos(angulo * math.pi / 180) +0.03, 0.010 * math.sin(angulo * math.pi / 180) -.08, 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(147/255, 234/255, 249/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.025 * math.cos(angulo * math.pi / 180) -0.03, 0.010 * math.sin(angulo * math.pi / 180) -.08, 0)
        glEnd()
        glPopMatrix()