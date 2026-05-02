import pygame
import random
import numpy as np

pygame.init()

WIDTH,HEIGHT = 600,400
BLOCK_SIZE = 10

ACTION_SPACE = [0,1,2]

DIRECTIONS = ["UP","RIGHT","DOWN","LEFT"]