import pygame
import random

pygame.init()

width = 1920
hight = 1020

again = True
ball = pygame.Rect(width/2 - 15, hight/2 - 15, 10, 10)
player = pygame.Rect(200, 510, 10, 50)
op = pygame.Rect(1720, 510, 10, 50)

ball_speed_x = 1
ball_speed_y = 1

screen = pygame.display.set_mode((width, hight))

while again:
    
    screen.fill((0, 0, 0))
    
    pygame.draw.rect(screen, (255, 255 ,255), player)
    pygame.draw.rect(screen, (255, 255, 255), ball)
    pygame.draw.rect(screen, (255, 255, 255), op)
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= hight:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= width:
        ball_speed_x *= -1
        
    if ball.left == player.right and ball in :
        ball_speed_x *= -1
        ball_speed_y *= -1
        
    if ball.right == op.left:
        ball_speed_x *= -1
        ball_speed_y *= -1
        
    key = pygame.key.get_pressed()
    
    if key[pygame.K_w] == True:
        player.move_ip(0, -1)
        
    if key[pygame.K_s] == True:
        player.move_ip(0, 1)
        
    if key[pygame.K_i] == True:
        op.move_ip(0, -1)
    
    if key[pygame.K_k] == True:
        op.move_ip(0, 1)
        
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            again = False
            
            
    pygame.display.update()
            
pygame.quit()