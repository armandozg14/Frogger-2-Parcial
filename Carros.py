from OpenGL.GL import *
from glew_wish import *
import glfw
import math
from Modelo import *

class Carros(Modelo):
    def __init__(self, x, y, z, velocidad, direccion):
        super().__init__(x, y, z, velocidad, direccion)
        self.extremo_izquierdo = 0.05
        self.extremo_derecho = 0.05
        self.extremo_inferior = 0.05
        self.extremo_superior =0.05

    tiempo_anterior = 0.0
    
    def actualizar(self, tiempo_delta):
        cantidad_movimiento = self.velocidad * tiempo_delta
        if self.direccion == 2:
            self.posicion_x = self.posicion_x - cantidad_movimiento
            if self.posicion_x <= -1:
                self.posicion_x = 1
        if self.direccion == 3:
            self.posicion_x = self.posicion_x + cantidad_movimiento
            if self.posicion_x >= 1:
                self.posicion_x = -1

    def dibujar(self):

        glPushMatrix()
        glTranslatef(self.posicion_x, self.posicion_y, 0.0)
        if self.direccion==2:
            glRotatef(180, 0, 0, 1)
            glBegin(GL_QUADS)
            
            glColor3f(234/255,129/255,25/255)
            glVertex3f(-0.05,0.04,0.0)
            glVertex3f(-0.03,0.04,0.0)
            glVertex3f(-0.03,-0.04,0.0)
            glVertex3f(-0.05,-0.04,0.0)

            glColor3f(234/255,129/255,25/255)
            glVertex3f(-0.03,0.01,0.0)
            glVertex3f(-0.01,0.01,0.0)
            glVertex3f(-0.01,-0.01,0.0)
            glVertex3f(-0.03,-0.01,0.0)

            glColor3f(234/255,129/255,25/255)
            glVertex3f(-0.01,0.03,0.0)
            glVertex3f(0.05,0.03,0.0)
            glVertex3f(0.05,-0.03,0.0)
            glVertex3f(-0.01,-0.03,0.0)

            glColor3f(234/255,129/255,25/255)
            glVertex3f(0.05,0.015,0.0)
            glVertex3f(0.065,0.015,0.0)
            glVertex3f(0.065,-0.015,0.0)
            glVertex3f(0.05,-0.015,0.0)

            glColor3f(234/255,129/255,25/255)
            glVertex3f(0.05,0.01,0.0)
            glVertex3f(0.1,0.01,0.0)
            glVertex3f(0.1,-0.01,0.0)
            glVertex3f(0.05,-0.01,0.0)

            glColor3f(99/255,156/255,247/255)
            glVertex3f(-0.005,0.01,0.0)
            glVertex3f(0.03,0.01,0.0)
            glVertex3f(0.03,-0.01,0.0)
            glVertex3f(-0.005,-0.01,0.0)

            #Llanta arriba trasera
            glColor3f(0,0,0)
            glVertex3f(-0.01,0.04,0.0)
            glVertex3f(0.015,0.04,0.0)
            glVertex3f(0.015,0.03,0.0)
            glVertex3f(-0.01,0.03,0.0)

            #Llanta abajo trasera
            glColor3f(0,0,0)
            glVertex3f(-0.01,-0.041,0.0)
            glVertex3f(0.015,-0.041,0.0)
            glVertex3f(0.015,-0.03,0.0)
            glVertex3f(-0.01,-0.03,0.0)

            #tubo llanta superior
            glColor3f(207/255,209/255,212/255)
            glVertex3f(0.09,0.03,0.0)
            glVertex3f(0.08,0.03,0.0)
            glVertex3f(0.08,0.01,0.0)
            glVertex3f(0.09,0.01,0.0)

            #tubo llanta inferior
            glColor3f(207/255,209/255,212/255)
            glVertex3f(0.09,-0.01,0.0)
            glVertex3f(0.08,-0.01,0.0)
            glVertex3f(0.08,-0.03,0.0)
            glVertex3f(0.09,-0.03,0.0)

            #Llanta abajo frontal
            glColor3f(0,0,0)
            glVertex3f(0.1,-0.041,0.0)
            glVertex3f(0.07,-0.041,0.0)
            glVertex3f(0.07,-0.03,0.0)
            glVertex3f(0.1,-0.03,0.0)

            #Llanta arriba trasera
            glColor3f(0,0,0)
            glVertex3f(0.1,0.04,0.0)
            glVertex3f(0.07,0.04,0.0)
            glVertex3f(0.07,0.03,0.0)
            glVertex3f(0.1,0.03,0.0)

            glEnd()
            
            glPopMatrix()
        else:
            glBegin(GL_QUADS)
            
            glColor3f(198/255,27/255,0/255)
            glVertex3f(-0.05,0.04,0.0)
            glVertex3f(-0.03,0.04,0.0)
            glVertex3f(-0.03,-0.04,0.0)
            glVertex3f(-0.05,-0.04,0.0)

            glColor3f(198/255,27/255,0/255)
            glVertex3f(-0.03,0.01,0.0)
            glVertex3f(-0.01,0.01,0.0)
            glVertex3f(-0.01,-0.01,0.0)
            glVertex3f(-0.03,-0.01,0.0)

            glColor3f(198/255,27/255,0/255)
            glVertex3f(-0.01,0.03,0.0)
            glVertex3f(0.05,0.03,0.0)
            glVertex3f(0.05,-0.03,0.0)
            glVertex3f(-0.01,-0.03,0.0)

            glColor3f(198/255,27/255,0/255)
            glVertex3f(0.05,0.015,0.0)
            glVertex3f(0.065,0.015,0.0)
            glVertex3f(0.065,-0.015,0.0)
            glVertex3f(0.05,-0.015,0.0)

            glColor3f(198/255,27/255,0/255)
            glVertex3f(0.05,0.01,0.0)
            glVertex3f(0.1,0.01,0.0)
            glVertex3f(0.1,-0.01,0.0)
            glVertex3f(0.05,-0.01,0.0)

            glColor3f(99/255,156/255,247/255)
            glVertex3f(-0.005,0.01,0.0)
            glVertex3f(0.03,0.01,0.0)
            glVertex3f(0.03,-0.01,0.0)
            glVertex3f(-0.005,-0.01,0.0)

            #Llanta arriba trasera
            glColor3f(0,0,0)
            glVertex3f(-0.01,0.04,0.0)
            glVertex3f(0.015,0.04,0.0)
            glVertex3f(0.015,0.03,0.0)
            glVertex3f(-0.01,0.03,0.0)

            #Llanta abajo trasera
            glColor3f(0,0,0)
            glVertex3f(-0.01,-0.041,0.0)
            glVertex3f(0.015,-0.041,0.0)
            glVertex3f(0.015,-0.03,0.0)
            glVertex3f(-0.01,-0.03,0.0)

            #tubo llanta superior
            glColor3f(207/255,209/255,212/255)
            glVertex3f(0.09,0.03,0.0)
            glVertex3f(0.08,0.03,0.0)
            glVertex3f(0.08,0.01,0.0)
            glVertex3f(0.09,0.01,0.0)

            #tubo llanta inferior
            glColor3f(207/255,209/255,212/255)
            glVertex3f(0.09,-0.01,0.0)
            glVertex3f(0.08,-0.01,0.0)
            glVertex3f(0.08,-0.03,0.0)
            glVertex3f(0.09,-0.03,0.0)

            #Llanta abajo frontal
            glColor3f(0,0,0)
            glVertex3f(0.1,-0.041,0.0)
            glVertex3f(0.07,-0.041,0.0)
            glVertex3f(0.07,-0.03,0.0)
            glVertex3f(0.1,-0.03,0.0)

            #Llanta arriba trasera
            glColor3f(0,0,0)
            glVertex3f(0.1,0.04,0.0)
            glVertex3f(0.07,0.04,0.0)
            glVertex3f(0.07,0.03,0.0)
            glVertex3f(0.1,0.03,0.0)

            glEnd()
            
            glPopMatrix()