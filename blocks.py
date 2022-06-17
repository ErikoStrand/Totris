from turtle import width
import pygame

class sizes:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.heigth)
    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.heigth)
        