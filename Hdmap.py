from Mapnode import *


class Hdmap:
    matrix = None

    def __init__(self, width, height):
        self.matrix = [[Mapnode(None, i, j) for j in range(height)] for i in range(width)]

    def set(self, x, y, landmark):
        self.matrix[x][y].landmark = landmark

    def print(self, x, y):
        self.matrix[x][y].print()

    def get(self, x, y):
        return self.matrix[x][y].landmark

    def getnode(self, x, y):
        return self.matrix[x][y]
