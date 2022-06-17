import pygame
import numpy as np
class Board:
    def __init__(self):
        self.col = 10 # -
        self.row = 20 # |
        self.square_size = 40
        self.board = np.zeros((self.row, self.col), str)
        self.grid = np.zeros((self.row, self.col), pygame.Rect)
    
    def create_grid(self):
        for col in range(self.col):
            for row in range(self.row):
                self.grid[row][col] = (pygame.Rect(self.square_size * col + 100, self.square_size * row, self.square_size, self.square_size))
                
    def draw_grid(self, display):
        for col in range(self.col):
            for row in range(self.row):
                pygame.draw.rect(display, (51, 51, 51), self.grid[row][col], 2)