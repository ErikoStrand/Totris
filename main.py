import pygame, sys
import numpy as np
from board import Board
from blocks import sizes
from animation import animation
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
FULL_ROWS = []
MOVE = True
DROP = 0
SPEED = 15
GO_RIGHT = True
GO_LEFT = True
LEFT_HIT = True
RIGHT_HIT = True
BLOCK_LOCATIONS = {
    "I": [],
    "J": [],
    "L": [],
    "O": [],
    "S": [],
    "T": [],
    "Z": [],
}
COLORS = {
    "I": (0, 240, 240),
    "J": (0, 0, 240),
    "L": (240, 160, 0),
    "O": (240, 240, 0),
    "S": (0, 240, 0),
    "T": (160, 0, 240),
    "Z": (240, 0, 0),
}

def random_block():
    global CURRENT_BLOCK, GO_LEFT, GO_RIGHT, LEFT_HIT, RIGHT_HIT
    GO_LEFT = True
    GO_RIGHT = True
    RIGHT_HIT = True
    LEFT_HIT = True
    #CURRENT_BLOCK = np.random.choice(["I", "J", "L", "O", "S", "T", "Z"], 1)
    CURRENT_BLOCK = np.random.choice(["L"], 1)
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
    dt = CLOCK.tick(60) / 1000
    DROP += SPEED*dt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and GO_RIGHT and RIGHT_HIT:
                GO_LEFT = True
                for block in BLOCKS:
                    block.x += 40
                                
            if event.key == pygame.K_LEFT and GO_LEFT and LEFT_HIT:
                GO_RIGHT = True
                for block in BLOCKS:
                    block.x -= 40      
    # update
    if DROP >= 1:
        for block in BLOCKS:
            block.y += 40
            block.update() 
        DROP = 0 
            
    for block in BLOCKS:
        if block.x >= 460:
            GO_RIGHT = False
            block.x = 460
   
        if block.x <= 100:
            block.x = 100
            GO_LEFT = False
        block.update()
    # collisions with floor
    for block in BLOCKS:
        if block.y > 760:
            dif = block.y - 760
            for block in BLOCKS:
                block.y -= dif
                block.update()
                for col in range(BOARD.col):
                    for row in range(BOARD.row):
                        if BOARD.grid[row][col] == block.rect:
                            BLOCK_LOCATIONS[CURRENT_BLOCK[0]].append(block)
                            BOARD.board[row][col] = CURRENT_BLOCK[0]
            BLOCKS = []
            random_block()
            print(BOARD.board)                 
    # collision with placed blocks
    for col in range(BOARD.col):
        for row in range(BOARD.row):
            if BOARD.board[row][col] != "":
                for count, block in enumerate(BLOCKS):
                    # PLACED FLOOR
                    #left wall
                    if block.rect.midleft == BOARD.grid[row][col].midright:
                        LEFT_HIT = False
                        
                    # right wall
                    if block.rect.midright == BOARD.grid[row][col].midleft:
                        RIGHT_HIT = False
                               
                    if block.rect == BOARD.grid[row][col]:
                        print(block.rect, BOARD.grid[row][col])
                        for block in BLOCKS:
                            block.y -= 40
                            block.update()
                            for col in range(BOARD.col):
                                for row in range(BOARD.row):
                                    if BOARD.grid[row][col] == block.rect:
                                        BLOCK_LOCATIONS[CURRENT_BLOCK[0]].append(block)
                                        BOARD.board[row][col] = CURRENT_BLOCK[0]
                        BLOCKS = []
                        random_block()
                        print(BOARD.board)
    # DESTROY ANIMATION and removes destroyed blocks from block_locations                    
    for row in range(BOARD.row):
        if BOARD.board[row][0] != "" and BOARD.board[row][1] != "" and BOARD.board[row][2] != "" and BOARD.board[row][3] != "" and BOARD.board[row][4] != "" and BOARD.board[row][5] != "" and BOARD.board[row][6] != "" and BOARD.board[row][7] != "" and BOARD.board[row][8] != "" and BOARD.board[row][9] != "":
            for i in range(10):
                for x, y in BLOCK_LOCATIONS.items():
                    for blocks in y:
                        if blocks.rect == BOARD.grid[row][i]:
                            BLOCK_LOCATIONS[x].remove(blocks)
                BOARD.board[row][i] = ""
            FULL_ROWS.append(animation(row, DISPLAY))
            for x, y in BLOCK_LOCATIONS.items():
                for blocks in y:
                    height = 800 - (20 - row) * 40
                    if blocks.rect.top < height:           
                        blocks.rect.top += 40
                        for col in range(BOARD.col):
                                for row in range(BOARD.row):
                                    if BOARD.grid[row][col] == blocks.rect:
                                        BOARD.board[row][col] = x
                    print(height)
                    
            print(BOARD.board)
            print(row)    
    while len(FULL_ROWS) > 0:
        for rows in FULL_ROWS:
            rows.animate(dt, 2)
            pygame.display.update(rows.rect)
            if rows.sizeright >= 200 and rows.sizeleft <= 100:
                FULL_ROWS.remove(rows)
    #print(BOARD.board)
                    
    # fix so blocks above a destoryed block falls down the lenght of which it was destroyed.
    
    DISPLAY.fill(BACKGROUND)
    BOARD.draw_grid(DISPLAY)
    # drawing falling block
    for block in BLOCKS:
        pygame.draw.rect(DISPLAY, COLORS[CURRENT_BLOCK[0]], block.rect)
    # drawing placed blocks    
    for col in range(BOARD.col):
        for row in range(BOARD.row):
            if BOARD.board[row][col] != "":
                pygame.draw.rect(DISPLAY, COLORS[BOARD.board[row][col]], BOARD.grid[row][col])
                
    pygame.draw.line(DISPLAY, (255, 255, 255), (0, 100), (100, 100), 5)
    pygame.draw.line(DISPLAY, (255, 255, 255), (500, 100), (600, 100), 5)
    pygame.draw.line(DISPLAY, (255, 255, 255), (100, 0), (100, 800), 5)
    pygame.draw.line(DISPLAY, (255, 255, 255), (500, 0), (500, 800), 5)
    pygame.display.flip()