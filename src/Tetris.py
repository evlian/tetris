import pygame
import pygame.freetype
from pygame.locals import *
import time

from pygame.time import get_ticks
from Shapes import Shapes
import random

class Tetris:
    def __init__(self):
        pygame.init()
        self.w_width = 400
        self.w_height = 500
        self.g_width = 250
        self.g_height = 500
        self.block_size = 25
        self.window = pygame.display.set_mode((self.w_width, self.w_height))
        self.title = "Tetris"
        self.score = 0
        self.level = 1
        self.running = True
        self.font_big = pygame.freetype.Font("../res/8.ttf", 18)
        self.font = pygame.freetype.Font("../res/8.ttf", 16)
        self.font_small = pygame.freetype.Font("../res/8.ttf", 13)
        self.font_smaller = pygame.freetype.Font("../res/8.ttf", 9)
        self.icon = pygame.image.load("../res/icon.png")
        self.logo = pygame.image.load("../res/logo.png")
        self.sound = pygame.image.load("../res/sound.png")
        self.sound_off = pygame.image.load("../res/sound_off.png")
        self.tetris_image = pygame.image.load("../res/tetris_image.png")
        self.grid = []
        self.cellPos = [0, 0]
        self.initGrid()
        self.grid[0][0] = 1
        self.shapes = Shapes()
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(self.icon)

    def initGrid(self):
        for i in range(20):
            row = [0 for i in range(10)]
            self.grid.append(row)

    def drawGrid(self, background):
        x = 3
        y = 3
        for i in range(20):
            y = 3
            for j in range(10):
                if self.grid[i][j] == 1:
                    pygame.draw.rect(background,
                                    (255, 255, 0),
                                    (y, x, 20, 20))
                y += 25
            x += 25
        pygame.display.flip()

    def drawBoard(self, window):
        background = pygame.Surface(window.get_size())
        background = background.convert()
        background.fill((23, 23, 23))
        i = 0
        for x in range(21):
            pygame.draw.line(background, (100, 100, 100), (0, i), (250, i), 1)
            i += 25
        i = 0
        for x in range(11):
            pygame.draw.line(background, (100, 100, 100), (i, 0), (i, 500), 1)
            i += 25
        pygame.draw.rect(background, (100, 100, 100), (275, 80, 100, 60), 1)
        pygame.draw.rect(background, (100, 100, 100), (285, 170, 80, 40), 3)
        pygame.draw.rect(background, (100, 100, 100), (285, 220, 80, 40), 3)
        pygame.draw.rect(background, (100, 100, 100), (285, 270, 80, 40), 3)
        pygame.draw.rect(background, (100, 100, 100), (285, 320, 80, 40), 3)
        background.blit(self.tetris_image, (280, 5))
        self.drawGrid(background)
        self.font.render_to(background, (295, 183), "PLAY", (110, 110, 110))
        self.font_small.render_to(background, (295, 233), "PAUSE", (110, 110, 110))
        self.font_smaller.render_to(background, (295, 285), "RESTART", (110, 110, 110))
        self.font_big.render_to(background, (295, 333), "QUIT", (110, 110, 110))
        self.font_small.render_to(background, (265, 390), "SCORE ", (110, 110, 110))
        self.font_small.render_to(background, (265, 410), str(self.score), (110, 110, 110))
        self.font_small.render_to(background, (265, 440), "LEVEL ", (110, 110, 110))
        self.font_small.render_to(background, (265, 460), str(self.level), (110, 110, 110))
        return background

    def showBoard(self, window, board):
        window.blit(board, (0, 0))
        pygame.display.flip()

    def move(self, key):
        self.grid[self.cellPos[0]][self.cellPos[1]] = 0
        if (key == pygame.K_UP and self.cellPos[0] > 0):
            self.cellPos[0] -= 1
        elif (key == pygame.K_DOWN and self.cellPos[0] < 19):
            self.cellPos[0] += 1
        elif (key == pygame.K_LEFT and self.cellPos[1] > 0):
            self.cellPos[1] -= 1
        elif (key == pygame.K_RIGHT and self.cellPos[1] < 9):
            self.cellPos[1] += 1
        self.grid[self.cellPos[0]][self.cellPos[1]] = 1

    def gravity(self):
        self.move(pygame.K_DOWN)

    def display(self):
        self.showBoard(self.window, self.drawBoard(self.window))


t = Tetris()
while True:
    t.display()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            t.move(event.key)

    if (pygame.time.get_ticks() % 1000 == 0):
        print(pygame.time.get_ticks())
        t.gravity()