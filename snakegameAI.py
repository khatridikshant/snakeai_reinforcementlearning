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
    