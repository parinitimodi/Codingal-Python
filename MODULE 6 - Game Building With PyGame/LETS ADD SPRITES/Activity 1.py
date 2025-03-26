import pygame
import random
pygame.init()
spritecolourchange = pygame.USEREVENT +1
backgroundcolourchange = pygame.USEREVENT +2
Blue = pygame.color("blue")
Purple = pygame.color("purple")
Green = pygame.color("green")
Turquoise = pygame.color("turquoise")
Pink = pygame.color("pink")
Red = pygame.color("red")
Orange = pygame.color("orange")
Yellow = pygame.color("yellow")
White = pygame.color("white")
Black = pygame.color("black")
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundaryhit = False
        if self.rect.left<=0 or self.rect.right>=500:
            self.velocity[0] = -self.velocity[0]
            boundaryhit = True
        if self.rect.top<=0 or self.rect.bottom>=400:
            self.velocity[1] = -self.velocity[1]
            boundaryhit = True
        if boundaryhit:
            pygame.event.post(pygame.event.Event(spritecolourchange))
            pygame.event.post(pygame.event.Event(backgroundcolourchange))
    def change_color(self):
        self.image.fill(random.choice([Blue,Purple,Green,Turquoise]))
def change_background_color(): 
    global bg_color

    bg_color = random.choice([Blue, Yellow, Green])

# Create a group to hold the sprite

    all_sprites_list = pygame.sprite.Group()

# Instantiate the sprite

    sp1 = Sprite(White, 20, 30)

# Randomly position the sprite

    sp1.rect.x = random.randint(0, 480)

    sp1.rect.y = random.randint(0, 370)

# Add the sprite to the group

    all_sprites_list.add(sp1)

# Create the game window

    screen = pygame.display.set_mode((500, 400))

# Set the window title

    pygame.display.set_caption("Colorful Bounce")

# Set the initial background color

    bg_color = BLUE

# Apply the background color

    screen.fill(bg_color)

# Game loop control flag

exit = False

# Create a clock object to control frame rate

clock = pygame.time.Clock()

# Main game loop

while not exit:

# Event handling loop

    for event in pygame.event.get():

# If the window's close button is clicked, exit the game

        if event.type == pygame.QUIT:

            exit = True

# If the sprite color change event is triggered, change the sprite's color

        elif event.type == SPRITE_COLOR_CHANGE_EVENT:

            sp1.change_color()

# If the background color change event is triggered, change the background color

        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:

            change_background_color()

# Update all sprites

all_sprites_list.update()

# Fill the screen with the current background color

screen.fill(bg_color)

# Draw all sprites to the screen

all_sprites_list.draw(screen)

# Refresh the display

pygame.display.flip()

# Limit the frame rate to 240 fps

clock.tick(240)

# Uninitialize all pygame modules and close the window

pygame.quit()                   