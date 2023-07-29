import pygame as pg
from OpenGL.GL import *
import numpy as np
import ctypes
from OpenGL.GL.shaders import compileProgram, compileShader

class App:


    def __init__(self):

        # Inicializa o Pygame
        pg.init()
        pg.display.set_mode((640, 480), pg.OPENGL | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        # Inicializa o OpenGL
        glClearColor(1, 0.2, 0.2, 1.0)

        # Cria o shader
        self.shader = self.createShader('shaders/vertex.txt', 'shaders/fragment.txt')
        glUseProgram(self.shader)

        # Cria triangulo
        self.triangulo = Triangulo()

        self.mainLoop()

    def createShader(self, vertexFilepath, fragmentFilepath):

        with open(vertexFilepath, 'r') as f:
            vertex_src = f.read()

        with open(fragmentFilepath, 'r') as f:
            fragment_src = f.read()

        shader = compileProgram(
            compileShader(vertex_src, GL_VERTEX_SHADER),
            compileShader(fragment_src, GL_FRAGMENT_SHADER)
        )

        return shader

    # Loop principal do jogo
    def mainLoop(self):

        running = True
        while running:
            # verifica eventos
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            # limpa a tela
            glClear(GL_COLOR_BUFFER_BIT)

            # desenha o triangulo
            glUseProgram(self.shader)
            glBindVertexArray(self.triangulo.vao)
            glDrawArrays(GL_TRIANGLES, 0, self.triangulo.vertex_count)
            pg.display.flip()

            # limita a 60 fps
            self.clock.tick(60)

        self.quit()

    # Finaliza o jogo
    def quit(self):
        self.triangle.destroy()
        glDeleteProgram(self.shader)
        pg.quit()

class Triangulo:

    def __init__(self):
        
        # x, y, z, r, g, b
        self.vertices = (
            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
            0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
            0.0, 0.5, 0.0, 0.0, 0.0, 1.0
        )

        self.vertices = np.array(self.vertices, dtype=np.float32)

        self.vertex_count = 3

        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)
        # position
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
        # color
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

    def destroy(self):
        glDeleteVertexArrays(1, (self.vao))
        glDeleteBuffers(1, (self.vbo))


if __name__ == '__main__':
    App()
