import pygame
pygame.init()
screen = pygame.display.set_mode((400,500))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.draw.rect(screen,(0,0,255), pygame.Rect(30,30,60,60))
    pygame.display.flip()
    import pygame
pygame.init()
screenwidth, screenheight = 500,500
screen = pygame.display.set_mode((400,500))
displaysurface = pygame.display.set_mode((screenwidth,screenheight))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.draw.rect(screen,(0,0,255), pygame.Rect(30,30,60,60))
    pygame.display.flip()
    y = pygame.font.Font(None,36).render("Hello! I am Pariniti!!",True,pygame.Color("black"))
    z = screen.get_rect(center =(screenwidth//2,screenheight//2+110))
    displaysurface.blit(y,z)
    running = True
    while running:
        
            if event.type == pygame.QUIT:
                running = False
            displaysurface.blit
            
            pygame.quit()
if __name__ == "__main__":
    game_loop()

    