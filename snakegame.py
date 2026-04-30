import pygame
import sys
import random

pygame.init()

WIDTH,HEIGHT = 600,400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
snake = [(100,100), (90,100), (80,100)]
block_size = 10

direction = "RIGHT"
food = (random.randrange(0,WIDTH,block_size),random.randrange(0,HEIGHT,block_size))



while True:
    
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            pygame.quit()
    
            sys.exit()
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'    
          
    head_x,head_y = snake[0]
 
    if direction == 'RIGHT':
        head_x += block_size
    elif direction == 'LEFT':
        head_x -= block_size
    elif direction == 'UP':
        head_y -= block_size
    elif direction == 'DOWN':
        head_y += block_size
            
    new_head = (head_x,head_y)
    snake.insert(0,new_head)
    
    if new_head == food:
        food = ((random.randrange(0,WIDTH,block_size),
                 random.randrange(0,HEIGHT,block_size)))
    snake.pop()
 
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,0,0),(food[0],food[1],block_size,block_size))
 
    for block in snake:
        pygame.draw.rect(screen,(0,255,0),(block[0],block[1],block_size,block_size))       
 
    pygame.display.update()
 
    clock.tick(10)
    
            