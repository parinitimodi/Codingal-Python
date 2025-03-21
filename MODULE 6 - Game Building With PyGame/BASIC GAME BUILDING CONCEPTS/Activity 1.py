import pygame
pygame.init()
screen = pygame.display.set_mode((400,500))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.draw.rect(screen,(0,0,255), pygame.Rect(30,30,60,60))
    pygame.display.flip()