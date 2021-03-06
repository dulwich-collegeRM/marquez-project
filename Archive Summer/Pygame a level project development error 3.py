import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1000, 800)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):

    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.x_speed = 0
        self.y_speed = 0
        self.lives = 3
        
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.heigth = height
        self.width = width
        self.rect = self.image.get_rect()

        self.rect.topleft = [x, y]
        self.rect.topright = [x + width, y]
        self.rect.bottomleft = [x, y + height]
        self.rect.bottomright = [x + width, y + height]


    def control(self,x,y):

        if movement() == True:
            self.x_speed = x
            self.y_speed = y
        else:
            check_direction(x, y)
            




##    def move_r(self, x_speed):
##        self.rect.x += x_speed
##        
##    def move_l(self, x_speed):
##        self.rect.x -= x_speed
##        
##    def move_u(self, y_speed):
##        self.rect.y -= y_speed
##        
##    def move_d(self, y_speed):
##        self.rect.y += y_speed

    def update(self):
        self.rect.x += self.x_speed 
        self.rect.y += self.y_speed
        
        
    def collide(self, all_sprites_list):
        if pygame.sprite.spritecollide(self, all_sprites_list, False):
            self.lives = 3

class Block(pygame.sprite.Sprite):

    def __init__(self, colour, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, colour, [x, y, width, height])
        self.width = width
        self.height = height
        self.rect = self.image.get_rect()

        x
        pos = [self.rect.x, self.rect.y]
        
        self.rect.topleft = [x, y]
        
        self.rect.topright = [x + width, y]

        self.rect.bottomleft = [x, y + height]

        self.rect.bottomright = [x + width, y + height]


    
class Floor(pygame.sprite.Sprite):
    def __init__(self, colour, x, y):
        super().__init__()
        self.image = pygame.Surface([x, y])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, colour, [50, 50, x, y])

        self.rect = self.image.get_rect()

def movement():
    for ablock in block_sprite_list:
        if (player.rect.x <= (ablock.rect.x + 50) and player.rect.x >= ablock.rect.x) and (player.rect.y <= (ablock.rect.y + 50) and player.rect.y >= ablock.rect.y):
            return False
        else:
            return True
##            if player.x_speed > 0:
##                player.rect.x = ablock.rect.x - 30
##            if player.x_speed < 0:
##                player.rect.x = ablock.rect.x + 50
##            if player.y_speed > 0:
##                player.rect.y = ablock.rect.y - 30
##            if player.y_speed < 0:
##                player.rect.y = ablock.rect.y + 50

def check_direction(x, y):
    if player.x_speed > 0:
        player.x_speed = 0
        player.y_speed = y
    if player.x_speed < 0:
        player.x_speed = 0
        player.y_speed = y
    if player.y_speed > 0:
        player.y_speed = 0
        player.x_speed = x
    if player.y_speed < 0:
        player.y_speed = 0
        player.x_speed = x

block_array = []
floor_array = []
    

all_sprites_list = pygame.sprite.Group()

block_sprite_list = pygame.sprite.Group()
floor_sprite_list = pygame.sprite.Group()
block = Block(BLUE, 50, 50, 0, 0)


player = Player(BLACK,30,30, 100, 100)

all_sprites_list.add(player)
all_sprites_list.add(block)
block_sprite_list.add(block)


 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-4,0)
                movement()
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(4,0)
                movement() 
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0,-4)
                movement()
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0,4)
                movement()


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(0,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(0,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0,0)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0,0)
            
    #code to end game will go here


    # --- Game logic should go here
    
##    key_pr = pygame.key.get_pressed()
##    if key_pr[pygame.K_LEFT]:
##        Player1.control(-4,0)
##    if key_pr[pygame.K_RIGHT]:
##        Player1.control(4,0)
##    if key_pr[pygame.K_UP]:
##        Player1.control(0,-4)
##    if key_pr[pygame.K_DOWN]:
##        Player1.control(0,4)
    

    all_sprites_list.remove(player)
    player.collide(all_sprites_list)
    all_sprites_list.add(player)
    
    all_sprites_list.update()
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
    print(player.x_speed, player.y_speed)
    # --- Drawing code should go here
    all_sprites_list.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
