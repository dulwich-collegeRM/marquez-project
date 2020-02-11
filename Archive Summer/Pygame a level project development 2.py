import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    
    #initialisation function for the player class
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        #this sets the players sprite as a square

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()
    #this is called to move the player right
    def move_r(self, x_speed):
        self.rect.x += x_speed

    #This is called to move the player left
    def move_l(self, x_speed):
        self.rect.x -= x_speed

    #This function is called to move the player up
    def move_u(self, y_speed):
        self.rect.y -= y_speed

    #This function is called to move the player down
    def move_d(self, y_speed):
        self.rect.y += y_speed

all_sprites_list = pygame.sprite.Group()

Player1 = Player(BLACK,20,20)
Player1.rect.x = 100
Player1.rect.y = 100

all_sprites_list.add(Player1)

 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #code to end game will go here


    # --- Game logic should go here

    #In the event that a key gets pressed
    key_pr = pygame.key.get_pressed()

    #If the left arrow key is pressed move left
    if key_pr[pygame.K_LEFT]:
        Player.move_l(3)

    #if the right arrow key is pressed move right
    if key_pr[pygame.K_RIGHT]:
        Player.move_r(3)

    #If the up arrow key is pressed move up
    if key_pr[pygame.K_UP]:
        Player.move_u(3)

    #If the down arrow key is pressed move down
    if key_pr[pygame.K_DOWN]:
        Player.move_d(3)
    
    all_sprites_list.update()
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    all_sprites_list.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
