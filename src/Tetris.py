import pygame
import pygame.freetype
from pygame.locals import *
import time
import math
import copy

from pygame.time import get_ticks
from shapes import Shapes
import random

class Tetris:
    def __init__(self):
        pygame.init()
        self.w_width = 400
        self.w_height = 500
        self.g_width = 250
        self.g_height = 500
        self.block_size = 25
        self.width = 10
        self.height = 20
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
        self.colorGrid = []
        self.cellPos = [0, 0]
        self.initGrid()
        self.shapes = Shapes()
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(self.icon)

    def initGrid(self):
        for i in range(20):
            row = [0 for i in range(10)]
            colorRow = [[0, 0, 0] for i in range(10)]
            self.grid.append(row)
            self.colorGrid.append(colorRow)
    

    def newShape(self):
        self.shapes.setNextShape()
        self.cellPos = [0, 0]
        

    def drawGrid(self, background):


        self.tempGrid = copy.deepcopy(self.grid)
        self.tempColorGrid = copy.deepcopy(self.colorGrid)
        
        #self.grid[self.cellPos[0]:self.cellPos[1], self.cellPos[0], self.cellPos[1]] = self.shapes.getCurrentShape()

        x_max = min(self.height, self.cellPos[0] + len(self.shapes.getCurrentShape()))
        y_max = min(self.width, self.cellPos[1] + len(self.shapes.getCurrentShape()[0]))


        x = 0
        y = 0

        for i in range(self.cellPos[0], x_max):
            y = 0
            for j in range(self.cellPos[1], y_max):
                isBlock = int(self.shapes.getCurrentShape()[x][y]) == 1
                self.tempGrid[i][j] = 1 if  isBlock else self.grid[i][j]
                self.tempColorGrid[i][j] = self.shapes.getCurrentColor() if isBlock else self.colorGrid[i][j]
                y += 1
            x += 1


        x = 3
        y = 3

        for i in range(20):
            y = 3
            for j in range(10):
                if self.tempGrid[i][j] == 1:
                    pygame.draw.rect(background,
                                    self.tempColorGrid[i][j],
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

    def move(self, key = None):
        if (key == None):
            if self.check_collision([self.cellPos[0] + 1, self.cellPos[1]]):
                self.cellPos[0] += 1
            else:
                return False
            
        
        if (key == pygame.K_UP):
            self.shapes.getRotatedShape()
        elif (key == pygame.K_DOWN and self.check_collision([self.cellPos[0] + 1, self.cellPos[1]])):
            self.cellPos[0] += 1
        elif (key == pygame.K_LEFT and self.check_collision([self.cellPos[0], self.cellPos[1] - 1])):
            self.cellPos[1] -= 1
        elif (key == pygame.K_RIGHT and self.check_collision([self.cellPos[0], self.cellPos[1] + 1])):
            self.cellPos[1] += 1

        return True

        
        #self.grid[self.cellPos[0]][self.cellPos[1]] = 1

    def check_collision(self, newCellPos):


        current = self.shapes.getCurrentShape()

        x_max = min(self.height, newCellPos[0] + len(self.shapes.getCurrentShape()))
        y_max = min(self.width, newCellPos[1] + len(self.shapes.getCurrentShape()[0]))

        x = newCellPos[0]
        y = newCellPos[1]
            
        for i in range(0, len(self.shapes.getCurrentShape())):
            y = newCellPos[1]
            for j in range(0, len(self.shapes.getCurrentShape()[0])):
                if (x >= self.height or y >= self.width or newCellPos[1] + j < 0):
                    if int(current[i][j]) == 1:
                        return False
                    else:
                        continue
                
                if self.grid[x][y] == 1 and int(current[i][j]) == 1:
                    return False
                    
                
                y += 1
            x += 1

        
    
        return True
    
    def settleShape(self):
        x_max = min(self.height, self.cellPos[0] + len(self.shapes.getCurrentShape()))
        y_max = min(self.width, self.cellPos[1] + len(self.shapes.getCurrentShape()[0]))


        x = 0
        y = 0

        for i in range(self.cellPos[0], x_max):
            y = 0
            for j in range(self.cellPos[1], y_max):
                isBlock = int(self.shapes.getCurrentShape()[x][y]) == 1
                self.grid[i][j] = 1 if isBlock else self.grid[i][j]
                self.colorGrid[i][j] = self.shapes.getCurrentColor() if isBlock else self.colorGrid[i][j]
                y += 1
            x += 1

    def gravity(self):
        a = self.move()
    
        if not a:
            self.settleShape()
            self.newShape()

    def clearFullRows(self):
        rowsToClear = 0

        for i in range(self.height):
            rowIsFull = True
            for j in range(self.width):
                if self.grid[i][j] == 0:
                    rowIsFull = False
                    break
            rowsToClear += 1 if rowIsFull else 0

        for i in range(0, self.height - rowsToClear):
            for j in range(self.width):
                self.grid[i - rowsToClear][j] = self.grid[i][j]
                if i > i - rowsToClear:
                    self.grid[i][j] = 0
                else:
                    self.grid[i][j] = self.grid[i + rowsToClear][j]
    
            

    def display(self):
        self.showBoard(self.window, self.drawBoard(self.window))

    def check_if_in_game_key_pressed(self, key):
        return key == pygame.K_RIGHT or key == pygame.K_LEFT or key == pygame.K_DOWN


t = Tetris()
time = 0
timeStep = 1000
downStep = 50
downTime = 0
clock = pygame.time.Clock()
down_pressed = False

while True:
    t.display()
    
    if (down_pressed and (pygame.time.get_ticks() - downStep) > downTime):
        downTime = pygame.time.get_ticks()
        t.move(pygame.K_DOWN)
        
    for event in pygame.event.get():
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            down_pressed = False
            
        
        
        if event.type == pygame.QUIT:
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if t.move(event.key) and event.key == pygame.K_DOWN:
                down_pressed = True
                time = pygame.time.get_ticks()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            t.newShape()

    t.clearFullRows()
        

    clock.tick(60)


    if ((pygame.time.get_ticks() - timeStep) > time):
        time = pygame.time.get_ticks()
        t.gravity()
        