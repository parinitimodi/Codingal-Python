import pygame
import random
screenwidth,screenheight = 500,400
speed = 6
font = 78
pygame.init()
ing = pygame.image.load("siuuu.jpg")
backgroundimage = pygame.transform.scale(ing,(screenwidth,screenheight))
font = pygame.font.SysFont("Harlow Solid Italic",font)
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(pygame.Color("pink"))
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect = self.image.get_rect()
    def move(self, x_change,y_change):
        self.rect.x = max(min(self.rect.x + x_change,screenwidth - self.rect.width),0)
        self.rect.y = max(min(self.rect.y + y_change,screenheight - self.rect.width),0)
screen = pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("Sprite Collision")
allsprites = pygame.sprite.Group()
sprite1 = Sprite(pygame.Color("black"),30,30)
sprite1.rect.x,sprite1.rect.y = random.randit(0,screenwidth - sprite1.rect.width),random.randit(0,screenheight - sprite1.rect.height)
allsprites.add(sprite1)
sprite2 = Sprite(pygame.Color("red"),30,30)
sprite2.rect.x,sprite2.rect.y = random.randit(0,screenwidth - sprite2.rect.width),random.randit(0,screenheight - sprite2.rect.height)
allsprites.add(sprite2)
running,won = True,False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or(event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False
    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])*speed
        y_change = (keys[pygame.K_DOWN]-keys[pygame.K_UP])*speed
        sprite1.move(x_change,y_change)
        if sprite1.rect.colliderect(sprite2.rect):
            allsprites.remove(sprite2)
            won = True
    screen.blit(backgroundimage,(0,0))
    allsprites.draw(screen)
    if won:
        wintext = font.render("You Win!!",True,pygame.Color("Black"))
        screen.blit(wintext,(screenwidth-wintext.get_width())//2,(screenheight-wintext.get_height())//2,)
    pygame.display.flip()
    clock.tick(90)
pygame.quit()