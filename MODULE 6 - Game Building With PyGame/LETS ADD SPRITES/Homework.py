import pygame
import sys
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sprite Movement Game')
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
sprite1 = pygame.Rect(100, 100, 50, 50)
sprite2 = pygame.Rect(100,100,50,50)
speed = 5
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite1.x -= speed
    if keys[pygame.K_RIGHT]:
        sprite1.x += speed
    if keys[pygame.K_UP]:
        sprite1.y -= speed
    if keys[pygame.K_DOWN]:
        sprite1.y += speed
    pygame.draw.rect(screen, RED, sprite1)
    pygame.draw.rect(screen, BLUE, sprite2) 
    pygame.display.update()
    pygame.time.Clock().tick(60)
pygame.quit()
sys.exit()
