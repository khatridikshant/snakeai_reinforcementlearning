import pygame
import sys

pygame.init()

WIDTH,HEIGHT = 600,400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
snake = [(100,100), (90,100), (80,100)]
block_size = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((0,0,0))
    for block in snake:
        pygame.draw.rect(screen,(0,255,0),(block[0],block[1],block_size,block_size))    
    pygame.display.update()
    clock.tick()
    
            