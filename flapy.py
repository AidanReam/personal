import pygame

pygame.init()

width = 1920
hight = 1020
again = True
player = pygame.Rect(300, 250, 50, 50)
screen = pygame.display.set_mode((width, hight))

while again:
    
    screen.fill((0, 0, 0))
    
    pygame.draw.rect(screen, (255, 0 ,0), player)
    
    key = pygame.key.get_pressed()
    
    if key[pygame.K_w] == True:
        player.move_ip(0, -1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            again = False
    if key != pygame.K_w:
        player.move_ip(0, 1)
        
    
    pygame.display.update()
    

pygame.quit()
    