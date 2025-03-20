import pygame
pygame.init()
screenwidth, screenheight = 500,500
displaysurface = pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption ("Adding an image and backround to Pygame")
backgroundimage = pygame.transform.scale(pygame.image.load("backround_image.jpg").convert(),(screenwidth,screenheight))
penguinimage = pygame.transform.scale(pygame.image.load("image.jpg").convert(),(200,200))
x = penguinimage.get_rect(center =(screenwidth//2,screenheight//2-30) )
y = pygame.font.Font(None,36).render("Hello! I am Penguin!!",True,pygame.Color("white"))
z = penguinimage.get_rect(center =(screenwidth//2,screenheight//2+110))
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        displaysurface.blit(backgroundimage,(0,0))
        displaysurface.blit(penguinimage,x)
        displaysurface.blit(y,z)
        pygame.display.flip()
        clock.tick(30)
        pygame.quit()
if __name__ == "__main__":
    game_loop()

    