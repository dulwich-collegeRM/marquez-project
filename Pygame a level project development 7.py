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

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.x_speed = 0
        self.y_speed = 0
        
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()
        #self.rect.topleft = pos

    def control(self,x,y):
        self.x_speed = x
        self.y_speed = y

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
            self.x_speed = 0
            self.y_speed = 0
            

class Block(pygame.sprite.Sprite):
    def __init__(self, colour, x, y):
        super().__init__()
        self.image = pygame.Surface([x, y])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, colour, [0, 0, x, y])

        self.rect = self.image.get_rect()
    



all_sprites_list = pygame.sprite.Group()

block = Block(BLUE, 50, 50)

player = Player(BLACK,30,30)
player.rect.x = 100
player.rect.y = 100

all_sprites_list.add(player)
all_sprites_list.add(block)

 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-4,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(4,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0,-4)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0,4)

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
