from argparse import Action
from pickle import POP_MARK
from OpenGL.GL import *
from glew_wish import *
import glfw
import math
from Fondo import *
from Rana import *
from Carros import *
from Mosca import *

fondo = Fondo()
rana = Rana(0.0, -0.95, 0.0, 0.1)
mosca = Mosca()
carross = []

#unidades por segundo
velocidad = 0.8
posicion_mosca = [0,-1,0]
angulo_mosca = 0
posicion_triangulo = [0.0,-0.95,0.0]
posiciones_carros = [
     [0.3,-0.85, 0.0],
     [0.8, -0.75, 0.0],
     [-0.4, -0.65, 0.0],
     [0.2, -0.55, 0.0],
     [0.7, -0.45, 0.0],
     [-0.1, -0.55, 0.0],
     [-0.3, -0.25, 0.0],
     [-0.6, -0.15, 0.0],
     [-0.2, -0.05, 0.0],
     [0.5, 0.05, 0.0],
     [0.3, 0.15, 0.0],
     [0.7, 0.25, 0.0],
     [0.9, 0.75, 0.0],
     [0.2, 0.45, 0.0],
     [-0.4, 0.55, 0.0],
     [-0.2, 0.65, 0.0],
     [0.5, 0.75, 0.0],
     [0.2, 0.85, 0.0],
     [0.5,-0.85, 0.0],
     [0.5, -0.75, 0.0],
     [-0.9, -0.65, 0.0],
     [0.8, -0.55, 0.0],
     [0.9, -0.45, 0.0],
     [-0.8, -0.85, 0.0],
     [-0.7, -0.25, 0.0],
     [-0.2, -0.15, 0.0],
     [-0.5, -0.05, 0.0],
     [0.9, 0.05, 0.0],
     [0.7, 0.15, 0.0],
     [0.2, 0.25, 0.0],
     [0.7, 0.65, 0.0],
     [0.5, 0.45, 0.0]
 ]

velocidades_carros=[0.5, 0.6, 0.5, 0.7, 0.5, 0.8, 0.5, 0.9, 0.5, 0.6, 0.5, 0.7, 0.5, 0.8, 0.5, 0.9, 0.5, 0.6, 0.5, 0.8, 0.5, 0.9, 0.5, 0.6, 0.5, 0.7, 0.5, 0.8, 0.9, 0.5]
direcciones_carros=[2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]

window = None
velocidad_triangulo = 0.1
velocidad_rotacion_triangulo = 90.0
fase = 90.0

tiempo_anterior = 0.0

#0 arriba , 1 abajo, 2 izquierda, 3 derecha
direccion_triangulo = 0
angulo_triangulo = 0
direccion_derecha = 3
direccion_izquierda = 2

def inicializar_carros():
    for i in range(30):
        posicion_x=posiciones_carros[i][0]
        posicion_y=posiciones_carros[i][1]
        posicion_z=posiciones_carros[i][2]
        velocidad=velocidades_carros[i]
        direccion=direcciones_carros[i]
        carross.append(Carros(posicion_x, posicion_y, posicion_z, velocidad, direccion))

def actualizar():

    global tiempo_anterior
    global window
    global posicion_triangulo
    global direccion_triangulo
    global angulo_triangulo
    global velocidad_triangulo

    tiempo_actual = glfw.get_time()
    tiempo_delta = tiempo_actual - tiempo_anterior
    
    #actualizar_mosca(tiempo_delta)
    mosca.actualizar(tiempo_delta)
    for carro in carross:
        carro.actualizar(tiempo_delta)

    for carro in carross:
        if carro.colisionando(rana):
            glfw.set_window_should_close(window, 1)
    tiempo_anterior = tiempo_actual
    
def draw():
#    draw_flor()
    fondo.dibujar()
    rana.dibujar()
    for carro in carross:
        carro.dibujar()
    mosca.dibujar()

def main():
    global window

    width = 600
    height = 700

    if not glfw.init():
        return

    window = glfw.create_window(width, height, "Frogger", None, None)

    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glewExperimental = True

    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    version = glGetString(GL_VERSION)
    print(version)

    glfw.set_key_callback(window, rana.actualizar)
    inicializar_carros()

    while not glfw.window_should_close(window):
        glClearColor(0.7,0.7,0.7,1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        actualizar()
        draw()

        glfw.poll_events()

        glfw.swap_buffers(window)

    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()