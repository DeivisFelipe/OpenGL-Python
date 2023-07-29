import pygame as pg
from OpenGL.GL import *

class App:


    def __init__(self):

        # Inicializa o Pygame
        pg.init()
        pg.display.set_mode((800, 600), pg.OPENGL | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        # Inicializa o OpenGL
        glClearColor(1, 0.2, 0.2, 1.0)

        self.mainLoop()

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
            pg.display.flip()

            # limita a 60 fps
            self.clock.tick(60)

        self.quit()

    # Finaliza o jogo
    def quit(self):
        pg.quit()

if __name__ == '__main__':
    App()
