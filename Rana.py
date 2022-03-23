from OpenGL.GL import *
from glew_wish import *
import glfw
import math
from Modelo import *

class Rana(Modelo):
    def __init__(self, posicion_x, posicion_y, posicion_z, velocidad):
        super().__init__(posicion_x, posicion_y, posicion_z, velocidad)
        
        self.extremo_izquierdo = 0.05
        self.extremo_derecho = 0.05
        self.extremo_inferior = 0.04
        self.extremo_superior =0.04

    def actualizar(self,window, key, scancode, action, mods):

        #Que la tecla escape cierre ventana al ser presionada
        if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
            glfw.set_window_should_close(window,1)

        #Mover la rana
        #Izquierda
        if key == glfw.KEY_LEFT and (action == glfw.PRESS):
            self.posicion_x =  self.posicion_x - self.velocidad
        #Derecha
        if key == glfw.KEY_RIGHT and (action == glfw.PRESS):
            self.posicion_x =  self.posicion_x + self.velocidad
        #Arriba
        if key == glfw.KEY_UP and (action == glfw.PRESS):
            self.posicion_y =  self.posicion_y + self.velocidad
        #Abajo
        if key == glfw.KEY_DOWN and (action == glfw.PRESS):
            self.posicion_y =  self.posicion_y - self.velocidad

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posicion_x, self.posicion_y, self.posicion_z)
        glScalef(0.5,0.5,0.0) 
        glColor3f(98/255,198/255,0/255)

        #Rana
        glTranslatef(0.75,0.2,0.0)
        glBegin(GL_QUADS)

        glVertex3f(-0.76, -0.11, 0.0)
        glVertex3f(-0.76, -0.15, 0.0)
        glVertex3f(-0.80, -0.15, 0.0)
        glVertex3f(-0.80, -0.11, 0.0)

        glVertex3f(-0.74, -0.25, 0.0)
        glVertex3f(-0.74, -0.15, 0.0)
        glVertex3f(-0.82, -0.15, 0.0)
        glVertex3f(-0.82, -0.25, 0.0)

        glVertex3f(-0.72, -0.18, 0.0)
        glVertex3f(-0.72, -0.15, 0.0)
        glVertex3f(-0.84, -0.15, 0.0)
        glVertex3f(-0.84, -0.18, 0.0)

        glVertex3f(-0.72, -0.22, 0.0)
        glVertex3f(-0.72, -0.25, 0.0)
        glVertex3f(-0.84, -0.25, 0.0)
        glVertex3f(-0.84, -0.22, 0.0)

        glVertex3f(-0.72, -0.27, 0.0)
        glVertex3f(-0.72, -0.22, 0.0)
        glVertex3f(-0.74, -0.22, 0.0)
        glVertex3f(-0.74, -0.27, 0.0)

        glVertex3f(-0.82, -0.27, 0.0)
        glVertex3f(-0.82, -0.22, 0.0)
        glVertex3f(-0.84, -0.22, 0.0)
        glVertex3f(-0.84, -0.27, 0.0)

        glVertex3f(-0.82, -0.13, 0.0)
        glVertex3f(-0.82, -0.15, 0.0)
        glVertex3f(-0.84, -0.15, 0.0)
        glVertex3f(-0.84, -0.13, 0.0)

        glVertex3f(-0.72, -0.13, 0.0)
        glVertex3f(-0.72, -0.15, 0.0)
        glVertex3f(-0.74, -0.15, 0.0)
        glVertex3f(-0.74, -0.13, 0.0)
        glEnd()

        glPopMatrix()