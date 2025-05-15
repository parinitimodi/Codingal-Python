import math
import random
import pygame
screenwidth = 1000
screenheight = 700
playerstartx = 370
playerstarty = 380
enemyymin = 50
enemyymax = 150
enemyspeedx = 4
enemyspeedy = 40
bulletspeedy = 10
collisiondistance = 27
pygame.init()
screen = pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("Space Invader")
background = pygame.image.load("background.png")
ufo = pygame.image.load("ufo.png")
bullet = pygame.image.load("bullet.png")
player = pygame.image.load("player.png")
enemy = pygame.image.load("enemy.png")
playerx = playerstartx
playery = playerstarty
playerxchange = 0
enemyimg = []
enemyx = []
enemyy = []
enemyxchange = []
enemyychange = []
numberofenemies = 6
for i in range(numberofenemies):
    enemyimg.append(pygame.image.load("enemy.png"))
    enemyx.append(random.randint(0,screenwidth - 64))
    enemyy.append(random.randint(enemyymin,enemyymax))
    enemyxchange.append(enemyspeedx)
    enemyychange.append(enemyspeedy)
bulleting = pygame.image.load("bullet.png")
bulletx = 0
bullety = playerstarty
bulletxchange = 0
bulletychange = bulletspeedy
bulletstate = "Ready"
scorevalue = 0
font = pygame.font.Font("freesansbold.ttf",32)
textx = 10
texty = 10
overfont = pygame.font.Font("freesansbold.ttf",64)
def showscore (x,y):
    score = font.render("Score = "+ str (scorevalue),True,(255,255,255))
    screen.blit(score,(x,y))
def gameovertext ():
    overtext = overfont.render("Game Over",True,(0,0,0))
    screen.blit(overtext,(200,250))
def player(x,y):
    screen.blit(player,(x,y))
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
def firebullet(x,y):
    global bulletstate
    bulletstate = "Fire"
    screen.blit(bulleting(x + 16,y+10))
def iscollision(enemyx,enemyy,bulletx,bullety):
    disttance = math.sqrt((enemyx - bulletx) ** 2 + (enemyy - bullety) ** 2)
    return disttance < collisiondistance
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerxchange = -5
            if event.key == pygame.K_RIGHT:
                playerxchange = 5
            if event.key == pygame.K_SPACE and bulletstate == "Ready":
                bulletx = playerx
                firebullet(bulletx,bullety)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
            playerxchange = 0
    playerx = playerx + playerxchange
    playerx = max(0,min(playerx,screenwidth - 64))
    for i in range (numberofenemies):
        if enemyy [i]>340:
            for j in range (numberofenemies):
                enemyy [j] = 2000
            gameovertext()
            break
        enemyx [i] += enemyxchange[i]
        if enemyx [i] <= 0 or enemyx [i]>=screenwidth - 64:
            enemyxchange[i] *= -1
            enemyy[i] += enemyychange[i]
        if iscollision(enemyx[i],enemyy[i],bulletx,bullety):
            bullety = playerstarty
            bulletstate = "Ready"
            scorevalue += 1
            enemyx[i] = random.randint(0,screenwidth - 64)
            enemyx[i] = random.randint(enemyymin,enemyymax)
        enemy(enemyx[i],enemyy[i],i)
    if bullety<=0:
        bullety = playerstarty
        bulletstate = "Ready"
    elif bulletstate == "Fire":
        firebullet(bulletx,bullety)
        bullety -= bulletychange
    player,(playerx,playery)
    showscore(textx,texty)
    pygame.display.update()
print("YAYYY WE DID IT!!")