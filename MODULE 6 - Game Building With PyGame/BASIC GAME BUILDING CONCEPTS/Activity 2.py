


import pygame
pygame.init()
screen = pygame.display.set_mode((400,400))
screen.fill((255,255,255))
green = (0,255,0)
pygame.draw.circle(screen,green,(300,300),50)
pygame.draw.circle(screen,green,(100,100),100,5)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    










