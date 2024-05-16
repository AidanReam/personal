import pygame
import random

pygame.init()

width = 1920
hight = 1020
again = True
ys = False

player = pygame.Rect(300, 250, 50, 50)
screen = pygame.display.set_mode((width, hight))
enemy = random.randint(0, 1000)

while again:
    
    
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0 ,0), player)
    
    key = pygame.key.get_pressed()
    
    if key[pygame.K_w] == True:
        player.move_ip(0, -1)
        ys = True
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            again = False
    if ys != True:
        player.move_ip(0, 1)
        
        
    
    pygame.display.update()
    ys = False
    
pygame.quit()
