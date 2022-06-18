import pygame

class animation:
    def __init__(self, rows, display):
        self.display = display
        self.rows = rows
        self.sizeright = 0
        self.sizeleft = 300
        self.y = 800 - (20 - rows) * 40
        self.height = 40 # does right thing?
        self.rect = pygame.Rect(100, self.y, 400, self.height)
    def animate(self, dt, speed):
        self.sizeright += 2*dt*speed
        self.sizeleft -= 2*dt*speed
        pygame.draw.rect(self.display, (255, 255, 255), (300, self.y, self.sizeright, self.height))
        pygame.draw.rect(self.display, (255, 255, 255), (self.sizeleft, self.y, self.sizeright, self.height))