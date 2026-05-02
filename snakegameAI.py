import pygame
import random
import numpy as np

pygame.init()

WIDTH,HEIGHT = 600,400
BLOCK_SIZE = 10

ACTION_SPACE = [0,1,2]

DIRECTIONS = ["UP","RIGHT","DOWN","LEFT"]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

snake = []
direction = "RIGHT"
food = (0,0)
score = 0

def reset():
    
    global snake,direction,food,score
    
    snake = [(100,100),(90,100),(80,100)]
    
    direction = "RIGHT"
    score = 0
    
    spawn_food()
    get_state()
    
    

def spawn_food():
    global food
    food = (random.randrange(0,WIDTH,BLOCK_SIZE),random.randrange(0,HEIGHT,BLOCK_SIZE))

def step(action):
    global direction, score
    change_direction(action)
    head_x,head_y = snake[0]
    
    if direction == "RIGHT":
        head_x += BLOCK_SIZE
    elif direction == "LEFT":
        head_x -= BLOCK_SIZE
    elif direction == "UP":
        head_y -= BLOCK_SIZE
    elif direction == "DOWN":
        head_y += BLOCK_SIZE
        
    
    new_head = (head_x,head_y)
    reward = 0
    done = False


def change_direction(action):
    global direction
    idx = DIRECTIONS.index(direction)
    if action == 1:
        direction = DIRECTIONS[(idx + 1) % 4]
    elif action == 2:
        direction = DIRECTIONS[(idx - 1) % 4]
        
def get_state():
    head_x, head_y = snake[0]
    state = np.array([head_x/WIDTH,head_y/HEIGHT,food[0]/WIDTH,food[1]/HEIGHT])
    return state

def render():
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0),
                     (food[0],food[1],BLOCK_SIZE,BLOCK_SIZE))
    
    for block in snake:
        pygame.draw.rect(screen,(0,255,0),block[0])
        
def close():
    pygame.quit()