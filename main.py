import random
from tkinter import CURRENT
import pygame, sys
import numpy as np
from board import Board
from blocks import sizes

#values
CLOCK = pygame.time.Clock()
RUNNING = True
BACKGROUND = (39, 39, 39)
WIDTH, HEIGHT = 600, 800
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
BOARD = Board()
BOARD.create_grid()
BLOCKS = []
CURRENT_BLOCK = []
MOVE = True
def random_block():
    global CURRENT_BLOCK
    CURRENT_BLOCK = np.random.choice(["I", "J", "L", "O", "S", "T", "Z"], 1)
    print(CURRENT_BLOCK)
    if CURRENT_BLOCK == "I":
        BLOCKS.append(sizes(260, 0, 40, 40))
        BLOCKS.append(sizes(260, 40, 40, 40))
        BLOCKS.append(sizes(260, 80, 40, 40))
        BLOCKS.append(sizes(260, 120, 40, 40))
    if CURRENT_BLOCK == "J":
        BLOCKS.append(sizes(260, 0, 40, 40))
        BLOCKS.append(sizes(300, 0, 40, 40))
        BLOCKS.append(sizes(260, 40, 40, 40))
        BLOCKS.append(sizes(260, 80, 40, 40))
    if CURRENT_BLOCK == "L":
        BLOCKS.append(sizes(260, 0, 40, 40))
        BLOCKS.append(sizes(260, 40, 40, 40))
        BLOCKS.append(sizes(260, 80, 40, 40))
        BLOCKS.append(sizes(300, 80, 40, 40))
    if CURRENT_BLOCK == "O":
        BLOCKS.append(sizes(260, 0, 40, 40))
        BLOCKS.append(sizes(300, 0, 40, 40))
        BLOCKS.append(sizes(260, 40, 40, 40))
        BLOCKS.append(sizes(300, 40, 40, 40))
    if CURRENT_BLOCK == "S":
        BLOCKS.append(sizes(260, 0, 40, 40))
        BLOCKS.append(sizes(260, 40, 40, 40))
        BLOCKS.append(sizes(300, 40, 40, 40))
        BLOCKS.append(sizes(300, 80, 40, 40))
    if CURRENT_BLOCK == "T":
        BLOCKS.append(sizes(260, 0, 40, 40))
        BLOCKS.append(sizes(260, 40, 40, 40))
        BLOCKS.append(sizes(260, 80, 40, 40))
        BLOCKS.append(sizes(300, 40, 40, 40))
    if CURRENT_BLOCK == "Z":
        BLOCKS.append(sizes(300, 0, 40, 40))
        BLOCKS.append(sizes(300, 40, 40, 40))
        BLOCKS.append(sizes(260, 40, 40, 40))
        BLOCKS.append(sizes(260, 80, 40, 40))
        
random_block()
while RUNNING:
    dt = CLOCK.tick(60) / 100
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                for block in BLOCKS:
                    block.x += 40
            if event.key == pygame.K_LEFT:
                for block in BLOCKS:
                    block.x -= 40       
    # update
    for block in BLOCKS:
        block.update(dt, 3)
        
    # collisions with floor
    for block in BLOCKS:
        if block.y > 760:
            dif = block.y - 760
            for block in BLOCKS:
                block.y -= dif
                block.rect = pygame.Rect(block.x, block.y, block.width, block.heigth)
                for col in range(BOARD.col):
                    for row in range(BOARD.row):
                        if BOARD.grid[row][col] == block.rect:
                            BOARD.board[row][col] = CURRENT_BLOCK[0]
                            
            BLOCKS = []   
    #print(BOARD.board)          
    DISPLAY.fill(BACKGROUND)
    BOARD.draw_grid(DISPLAY)
    pygame.draw.line(DISPLAY, (255, 255, 255), (0, 100), (100, 100), 5)
    pygame.draw.line(DISPLAY, (255, 255, 255), (500, 100), (600, 100), 5)
    for block in BLOCKS:
        pygame.draw.rect(DISPLAY, (238, 238, 238), block.rect)
        
    for col in range(BOARD.col):
        for row in range(BOARD.row):
            if BOARD.board[row][col] != "":
                pygame.draw.rect(DISPLAY, (238, 238, 238), BOARD.grid[row][col])
    pygame.display.flip()