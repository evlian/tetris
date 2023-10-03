import copy
import random

class Shapes:
    S = [['00000',
        '00000',
        '00110',
        '01100',
        '00000'],
        ['00000',
        '00100',
        '00110',
        '00010',
        '00000']]

    Z = [['00000',
        '00000',
        '01100',
        '00110',
        '00000'],
        ['00000',
        '00100',
        '01100',
        '01000',
        '00000']]

    I = [['00100',
        '00100',
        '00100',
        '00100',
        '00000'],
        ['00000',
        '11110',
        '00000',
        '00000',
        '00000']]

    O = [['00000',
        '00000',
        '01100',
        '01100',
        '00000']]

    J = [['00000',
        '01000',
        '01110',
        '00000',
        '00000'],
        ['00000',
        '00110',
        '00100',
        '00100',
        '00000'],
        ['00000',
        '00000',
        '01110',
        '00010',
        '00000'],
        ['00000',
        '00100',
        '00100',
        '01100',
        '00000']]

    L = [['00000',
        '00010',
        '01110',
        '00000',
        '00000'],
        ['00000',
        '00100',
        '00100',
        '00110',
        '00000'],
        ['00000',
        '00000',
        '01110',
        '01000',
        '00000'],
        ['00000',
        '01100',
        '00100',
        '00100',
        '00000']]

    T = [['00000',
        '00100',
        '01110',
        '00000',
        '00000'],
        ['00000',
        '00100',
        '00110',
        '00100',
        '00000'],
        ['00000',
        '00000',
        '01110',
        '00100',
        '00000'],
        ['00000',
        '00100',
        '01100',
        '00100',
        '00000']]

    colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

    def __init__(self):
        self.shapes = [self.S, self.Z, self.I, self.O, self.J, self.L, self.T]
        self.currentShape = [0, 0, 0, 0]
        self.lastShape = [0, 0, 0]
        pass

    def setNextShape(self):
        index = random.randint(0, 6)
        color = random.randint(0, len(self.colors) - 1)
        rotation = random.randint(0, len(self.shapes[index]) - 1)
        self.lastShape = copy.deepcopy(self.currentShape)
        self.currentShape = [index, rotation, len(self.shapes[index]) - 1, color]
        

    def getCurrentShape(self):
        return self.shapes[self.currentShape[0]][self.currentShape[1]]
    
    def getCurrentColor(self):
        return self.colors[self.currentShape[3]]

    def getRotatedShape(self):
        shapeIndex = self.currentShape[0]
        currentIndex = self.currentShape[1]
        maxIndex = self.currentShape[2]
        if currentIndex == maxIndex:
            self.currentShape[1] = -1
        self.currentShape[1] += 1
        return self.currentShape

    def getRandomColor(self):
        return self.colors[random.randint(0, len(self.colors))]
