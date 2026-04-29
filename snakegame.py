import pygame
import sys

pygame.init()

WIDTH,HEIGHT = 600,400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((0,0,0))    
    pygame.display.update()
    clock.tick()
    
            