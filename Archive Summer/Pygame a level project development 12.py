import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHTGRAY = (200, 200, 200)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (800, 800)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    
    x_speed = 0
    y_speed = 0
    lives = 3

    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        
        pygame.draw.rect(self.image, color, [0, 0, 20, 20])


        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.blocks = None

    def control(self, x, y):

        self.x_speed += x
        self.y_speed += y

            




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
        
        block_hit_list = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in block_hit_list:
            if self.x_speed > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

                
        self.rect.y += self.y_speed
        
        block_hit_list = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in block_hit_list:
            if self.y_speed > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

        floor_standing_list =  pygame.sprite.spritecollide(self, self.floors, False)
        for floor in floor_standing_list:
            print(player.lives)
        
##    def collide(self, all_sprites_list):
##        if pygame.sprite.spritecollide(self, , False):
##            self.lives = 3

class Block(pygame.sprite.Sprite):

    def __init__(self, colour, x, y):
        super().__init__()
        self.image = pygame.Surface([40, 40])
        self.image.fill(BLACK)


        pygame.draw.rect(self.image, colour, [x, y, 40, 40])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        


class Floor(pygame.sprite.Sprite):
    
    def __init__(self, colour, x, y):
        super().__init__()
        self.image = pygame.Surface([40, 40])
        self.image.fill(LIGHTGRAY)


        pygame.draw.rect(self.image, colour, [x, y, 40, 40])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


##            if player.x_speed > 0:
##                player.rect.x = ablock.rect.x - 30
##            if player.x_speed < 0:
##                player.rect.x = ablock.rect.x + 50
##            if player.y_speed > 0:
##                player.rect.y = ablock.rect.y - 30
##            if player.y_speed < 0:
##                player.rect.y = ablock.rect.y + 50

block_array = []
floor_array = []
    

all_sprites_list = pygame.sprite.Group()

block_sprite_list = pygame.sprite.Group()
floor_sprite_list = pygame.sprite.Group()


maze_array = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,]]



maze_graph = { maze_array[0][0]: [maze_array[1][0], maze_array[0][1]],
                   maze_array[1][0]: [maze_array[0][0], maze_array[1][1], maze_array[2][0]],
                   maze_array[2][0]: [maze_array[1][0], maze_array[2][1], maze_array[3][0]],
                   maze_array[3][0]: [maze_array[2][0], maze_array[3][1], maze_array[4][0]],
                   maze_array[4][0]: [maze_array[3][0], maze_array[4][1], maze_array[5][0]],
                   maze_array[5][0]: [maze_array[4][0], maze_array[5][1], maze_array[6][0]],
                   maze_array[6][0]: [maze_array[5][0], maze_array[6][1], maze_array[7][0]],
                   maze_array[7][0]: [maze_array[6][0], maze_array[7][1], maze_array[8][0]],
                   maze_array[8][0]: [maze_array[7][0], maze_array[8][1], maze_array[9][0]],
                   maze_array[9][0]: [maze_array[8][0], maze_array[9][1], maze_array[10][0]],
                   maze_array[10][0]: [maze_array[9][0], maze_array[10][1], maze_array[11][0]],
                   maze_array[11][0]: [maze_array[10][0], maze_array[11][1], maze_array[12][0]],
                   maze_array[12][0]: [maze_array[11][0], maze_array[12][1], maze_array[13][0]],
                   maze_array[13][0]: [maze_array[12][0], maze_array[13][1], maze_array[14][0]],
                   maze_array[14][0]: [maze_array[13][0], maze_array[14][1], maze_array[15][0]],
                   maze_array[15][0]: [maze_array[14][0], maze_array[15][1], maze_array[16][0]],
                   maze_array[16][0]: [maze_array[15][0], maze_array[16][1], maze_array[17][0]],
                   maze_array[17][0]: [maze_array[16][0], maze_array[17][1], maze_array[18][0]],
                   maze_array[18][0]: [maze_array[17][0], maze_array[18][1], maze_array[19][0]],
                   maze_array[19][0]: [maze_array[18][0], maze_array[19][1]],
                   
                   maze_array[0][1]: [maze_array[1][1], maze_array[0][2], maze_array[0][0]],
                   maze_array[1][1]: [maze_array[0][1], maze_array[1][2], maze_array[2][1], maze_array[1][0]],
                   maze_array[2][1]: [maze_array[1][1], maze_array[2][2], maze_array[3][1], maze_array[2][0]],
                   maze_array[3][1]: [maze_array[2][1], maze_array[3][2], maze_array[4][1], maze_array[3][0]],
                   maze_array[4][1]: [maze_array[3][1], maze_array[4][2], maze_array[5][1], maze_array[4][0]],
                   maze_array[5][1]: [maze_array[4][1], maze_array[5][2], maze_array[6][1], maze_array[5][0]],
                   maze_array[6][1]: [maze_array[5][1], maze_array[6][2], maze_array[7][1], maze_array[6][0]],
                   maze_array[7][1]: [maze_array[6][1], maze_array[7][2], maze_array[8][1], maze_array[7][0]],
                   maze_array[8][1]: [maze_array[7][1], maze_array[8][2], maze_array[9][1], maze_array[8][0]],
                   maze_array[9][1]: [maze_array[8][1], maze_array[9][2], maze_array[10][1], maze_array[9][0]],
                   maze_array[10][1]: [maze_array[9][1], maze_array[10][2], maze_array[11][1], maze_array[10][0]],
                   maze_array[11][1]: [maze_array[10][1], maze_array[11][2], maze_array[12][1], maze_array[11][0]],
                   maze_array[12][1]: [maze_array[11][1], maze_array[12][2], maze_array[13][1], maze_array[12][0]],
                   maze_array[13][1]: [maze_array[12][1], maze_array[13][2], maze_array[14][1], maze_array[13][0]],
                   maze_array[14][1]: [maze_array[13][1], maze_array[14][2], maze_array[15][1], maze_array[14][0]],
                   maze_array[15][1]: [maze_array[14][1], maze_array[15][2], maze_array[16][1], maze_array[15][0]],
                   maze_array[16][1]: [maze_array[15][1], maze_array[16][2], maze_array[17][1], maze_array[16][0]],
                   maze_array[17][1]: [maze_array[16][1], maze_array[17][2], maze_array[18][1], maze_array[17][0]],
                   maze_array[18][1]: [maze_array[17][1], maze_array[18][2], maze_array[19][1], maze_array[18][0]],
                   maze_array[19][1]: [maze_array[18][1], maze_array[19][2], maze_array[19][0]],
                   
                   maze_array[0][2]: [maze_array[1][2], maze_array[0][3], maze_array[0][1]],
                   maze_array[1][2]: [maze_array[0][2], maze_array[1][3], maze_array[2][2], maze_array[1][1]],
                   maze_array[2][2]: [maze_array[1][2], maze_array[2][3], maze_array[3][2], maze_array[2][1]],
                   maze_array[3][2]: [maze_array[2][2], maze_array[3][3], maze_array[4][2], maze_array[3][1]],
                   maze_array[4][2]: [maze_array[3][2], maze_array[4][3], maze_array[5][2], maze_array[4][1]],
                   maze_array[5][2]: [maze_array[4][2], maze_array[5][3], maze_array[6][2], maze_array[5][1]],
                   maze_array[6][2]: [maze_array[5][2], maze_array[6][3], maze_array[7][2], maze_array[6][1]],
                   maze_array[7][2]: [maze_array[6][2], maze_array[7][3], maze_array[8][2], maze_array[7][1]],
                   maze_array[8][2]: [maze_array[7][2], maze_array[8][3], maze_array[9][2], maze_array[8][1]],
                   maze_array[9][2]: [maze_array[8][2], maze_array[9][3], maze_array[10][2], maze_array[9][1]],
                   maze_array[10][2]: [maze_array[9][2], maze_array[10][3], maze_array[11][2], maze_array[10][1]],
                   maze_array[11][2]: [maze_array[10][2], maze_array[11][3], maze_array[12][2], maze_array[11][1]],
                   maze_array[12][2]: [maze_array[11][2], maze_array[12][3], maze_array[13][2], maze_array[12][1]],
                   maze_array[13][2]: [maze_array[12][2], maze_array[13][3], maze_array[14][2], maze_array[13][1]],
                   maze_array[14][2]: [maze_array[13][2], maze_array[14][3], maze_array[15][2], maze_array[14][1]],
                   maze_array[15][2]: [maze_array[14][2], maze_array[15][3], maze_array[16][2], maze_array[15][1]],
                   maze_array[16][2]: [maze_array[15][2], maze_array[16][3], maze_array[17][2], maze_array[16][1]],
                   maze_array[17][2]: [maze_array[16][2], maze_array[17][3], maze_array[18][2], maze_array[17][1]],
                   maze_array[18][2]: [maze_array[17][2], maze_array[18][3], maze_array[19][2], maze_array[18][1]],
                   maze_array[19][2]: [maze_array[18][2], maze_array[19][3], maze_array[19][0]],
                   
                   maze_array[0][3]: [maze_array[1][3], maze_array[0][4], maze_array[0][2]],
                   maze_array[1][3]: [maze_array[0][3], maze_array[1][4], maze_array[2][3], maze_array[1][2]],
                   maze_array[2][3]: [maze_array[1][3], maze_array[2][4], maze_array[3][3], maze_array[2][2]],
                   maze_array[3][3]: [maze_array[2][3], maze_array[3][4], maze_array[4][3], maze_array[3][2]],
                   maze_array[4][3]: [maze_array[3][3], maze_array[4][4], maze_array[5][3], maze_array[4][2]],
                   maze_array[5][3]: [maze_array[4][3], maze_array[5][4], maze_array[6][3], maze_array[5][2]],
                   maze_array[6][3]: [maze_array[5][3], maze_array[6][4], maze_array[7][3], maze_array[6][2]],
                   maze_array[7][3]: [maze_array[6][3], maze_array[7][4], maze_array[8][3], maze_array[7][2]],
                   maze_array[8][3]: [maze_array[7][3], maze_array[8][4], maze_array[9][3], maze_array[8][2]],
                   maze_array[9][3]: [maze_array[8][3], maze_array[9][4], maze_array[10][3], maze_array[9][2]],
                   maze_array[10][3]: [maze_array[9][3], maze_array[10][4], maze_array[11][3], maze_array[10][2]],
                   maze_array[11][3]: [maze_array[10][3], maze_array[11][4], maze_array[12][3], maze_array[11][2]],
                   maze_array[12][3]: [maze_array[11][3], maze_array[12][4], maze_array[13][3], maze_array[12][2]],
                   maze_array[13][3]: [maze_array[12][3], maze_array[13][4], maze_array[14][3], maze_array[13][2]],
                   maze_array[14][3]: [maze_array[13][3], maze_array[14][4], maze_array[15][3], maze_array[14][2]],
                   maze_array[15][3]: [maze_array[14][3], maze_array[15][4], maze_array[16][3], maze_array[15][2]],
                   maze_array[16][3]: [maze_array[15][3], maze_array[16][4], maze_array[17][3], maze_array[16][2]],
                   maze_array[17][3]: [maze_array[16][3], maze_array[17][4], maze_array[18][3], maze_array[17][2]],
                   maze_array[18][3]: [maze_array[17][3], maze_array[18][4], maze_array[19][3], maze_array[18][2]],
                   maze_array[19][3]: [maze_array[18][3], maze_array[19][4], maze_array[19][2]],

                   maze_array[0][4]: [maze_array[1][4], maze_array[0][5], maze_array[0][3]],
                   maze_array[1][4]: [maze_array[0][4], maze_array[1][5], maze_array[2][4], maze_array[1][3]],
                   maze_array[2][4]: [maze_array[1][4], maze_array[2][5], maze_array[3][4], maze_array[2][3]],
                   maze_array[3][4]: [maze_array[2][4], maze_array[3][5], maze_array[4][4], maze_array[3][3]],
                   maze_array[4][4]: [maze_array[3][4], maze_array[4][5], maze_array[5][4], maze_array[4][3]],
                   maze_array[5][4]: [maze_array[4][4], maze_array[5][5], maze_array[6][4], maze_array[5][3]],
                   maze_array[6][4]: [maze_array[5][4], maze_array[6][5], maze_array[7][4], maze_array[6][3]],
                   maze_array[7][4]: [maze_array[6][4], maze_array[7][5], maze_array[8][4], maze_array[7][3]],
                   maze_array[8][4]: [maze_array[7][4], maze_array[8][5], maze_array[9][4], maze_array[8][3]],
                   maze_array[9][4]: [maze_array[8][4], maze_array[9][5], maze_array[10][4], maze_array[9][3]],
                   maze_array[10][4]: [maze_array[9][4], maze_array[10][5], maze_array[11][4], maze_array[10][3]],
                   maze_array[11][4]: [maze_array[10][4], maze_array[11][5], maze_array[12][4], maze_array[11][3]],
                   maze_array[12][4]: [maze_array[11][4], maze_array[12][5], maze_array[13][4], maze_array[12][3]],
                   maze_array[13][4]: [maze_array[12][4], maze_array[13][5], maze_array[14][4], maze_array[13][3]],
                   maze_array[14][4]: [maze_array[13][4], maze_array[14][5], maze_array[15][4], maze_array[14][3]],
                   maze_array[15][4]: [maze_array[14][4], maze_array[15][5], maze_array[16][4], maze_array[15][3]],
                   maze_array[16][4]: [maze_array[15][4], maze_array[16][5], maze_array[17][4], maze_array[16][3]],
                   maze_array[17][4]: [maze_array[16][4], maze_array[17][5], maze_array[18][4], maze_array[17][3]],
                   maze_array[18][4]: [maze_array[17][4], maze_array[18][5], maze_array[19][4], maze_array[18][3]],
                   maze_array[19][4]: [maze_array[18][4], maze_array[19][5], maze_array[19][3]],

                   maze_array[0][5]: [maze_array[1][5], maze_array[0][6], maze_array[0][4]],
                   maze_array[1][5]: [maze_array[0][5], maze_array[1][6], maze_array[2][5], maze_array[1][4]],
                   maze_array[2][5]: [maze_array[1][5], maze_array[2][6], maze_array[3][5], maze_array[2][4]],
                   maze_array[3][5]: [maze_array[2][5], maze_array[3][6], maze_array[4][5], maze_array[3][4]],
                   maze_array[4][5]: [maze_array[3][5], maze_array[4][6], maze_array[5][5], maze_array[4][4]],
                   maze_array[5][5]: [maze_array[4][5], maze_array[5][6], maze_array[6][5], maze_array[5][4]],
                   maze_array[6][5]: [maze_array[5][5], maze_array[6][6], maze_array[7][5], maze_array[6][4]],
                   maze_array[7][5]: [maze_array[6][5], maze_array[7][6], maze_array[8][5], maze_array[7][4]],
                   maze_array[8][5]: [maze_array[7][5], maze_array[8][6], maze_array[9][5], maze_array[8][4]],
                   maze_array[9][5]: [maze_array[8][5], maze_array[9][6], maze_array[10][5], maze_array[9][4]],
                   maze_array[10][5]: [maze_array[9][5], maze_array[10][6], maze_array[11][5], maze_array[10][4]],
                   maze_array[11][5]: [maze_array[10][5], maze_array[11][6], maze_array[12][5], maze_array[11][4]],
                   maze_array[12][5]: [maze_array[11][5], maze_array[12][6], maze_array[13][5], maze_array[12][4]],
                   maze_array[13][5]: [maze_array[12][5], maze_array[13][6], maze_array[14][5], maze_array[13][4]],
                   maze_array[14][5]: [maze_array[13][5], maze_array[14][6], maze_array[15][5], maze_array[14][4]],
                   maze_array[15][5]: [maze_array[14][5], maze_array[15][6], maze_array[16][5], maze_array[15][4]],
                   maze_array[16][5]: [maze_array[15][5], maze_array[16][6], maze_array[17][5], maze_array[16][4]],
                   maze_array[17][5]: [maze_array[16][5], maze_array[17][6], maze_array[18][5], maze_array[17][4]],
                   maze_array[18][5]: [maze_array[17][5], maze_array[18][6], maze_array[19][5], maze_array[18][4]],
                   maze_array[19][5]: [maze_array[18][5], maze_array[19][6], maze_array[19][4]],

                   maze_array[0][6]: [maze_array[1][6], maze_array[0][7], maze_array[0][5]],
                   maze_array[1][6]: [maze_array[0][6], maze_array[1][7], maze_array[2][6], maze_array[1][5]],
                   maze_array[2][6]: [maze_array[1][6], maze_array[2][7], maze_array[3][6], maze_array[2][5]],
                   maze_array[3][6]: [maze_array[2][6], maze_array[3][7], maze_array[4][6], maze_array[3][5]],
                   maze_array[4][6]: [maze_array[3][6], maze_array[4][7], maze_array[5][6], maze_array[4][5]],
                   maze_array[5][6]: [maze_array[4][6], maze_array[5][7], maze_array[6][6], maze_array[5][5]],
                   maze_array[6][6]: [maze_array[5][6], maze_array[6][7], maze_array[7][6], maze_array[6][5]],
                   maze_array[7][6]: [maze_array[6][6], maze_array[7][7], maze_array[8][6], maze_array[7][5]],
                   maze_array[8][6]: [maze_array[7][6], maze_array[8][7], maze_array[9][6], maze_array[8][5]],
                   maze_array[9][6]: [maze_array[8][6], maze_array[9][7], maze_array[10][6], maze_array[9][5]],
                   maze_array[10][6]: [maze_array[9][6], maze_array[10][7], maze_array[11][6], maze_array[10][5]],
                   maze_array[11][6]: [maze_array[10][6], maze_array[11][7], maze_array[12][6], maze_array[11][5]],
                   maze_array[12][6]: [maze_array[11][6], maze_array[12][7], maze_array[13][6], maze_array[12][5]],
                   maze_array[13][6]: [maze_array[12][6], maze_array[13][7], maze_array[14][6], maze_array[13][5]],
                   maze_array[14][6]: [maze_array[13][6], maze_array[14][7], maze_array[15][6], maze_array[14][5]],
                   maze_array[15][6]: [maze_array[14][6], maze_array[15][7], maze_array[16][6], maze_array[15][5]],
                   maze_array[16][6]: [maze_array[15][6], maze_array[16][7], maze_array[17][6], maze_array[16][5]],
                   maze_array[17][6]: [maze_array[16][6], maze_array[17][7], maze_array[18][6], maze_array[17][5]],
                   maze_array[18][6]: [maze_array[17][6], maze_array[18][7], maze_array[19][6], maze_array[18][5]],
                   maze_array[19][6]: [maze_array[18][6], maze_array[19][7], maze_array[19][5]],

                   maze_array[0][7]: [maze_array[1][7], maze_array[0][8], maze_array[0][6]],
                   maze_array[1][7]: [maze_array[0][7], maze_array[1][8], maze_array[2][7], maze_array[1][6]],
                   maze_array[2][7]: [maze_array[1][7], maze_array[2][8], maze_array[3][7], maze_array[2][6]],
                   maze_array[3][7]: [maze_array[2][7], maze_array[3][8], maze_array[4][7], maze_array[3][6]],
                   maze_array[4][7]: [maze_array[3][7], maze_array[4][8], maze_array[5][7], maze_array[4][6]],
                   maze_array[5][7]: [maze_array[4][7], maze_array[5][8], maze_array[6][7], maze_array[5][6]],
                   maze_array[6][7]: [maze_array[5][7], maze_array[6][8], maze_array[7][7], maze_array[6][6]],
                   maze_array[7][7]: [maze_array[6][7], maze_array[7][8], maze_array[8][7], maze_array[7][6]],
                   maze_array[8][7]: [maze_array[7][7], maze_array[8][8], maze_array[9][7], maze_array[8][6]],
                   maze_array[9][7]: [maze_array[8][7], maze_array[9][8], maze_array[10][7], maze_array[9][6]],
                   maze_array[10][7]: [maze_array[9][7], maze_array[10][8], maze_array[11][7], maze_array[10][6]],
                   maze_array[11][7]: [maze_array[10][7], maze_array[11][8], maze_array[12][7], maze_array[11][6]],
                   maze_array[12][7]: [maze_array[11][7], maze_array[12][8], maze_array[13][7], maze_array[12][6]],
                   maze_array[13][7]: [maze_array[12][7], maze_array[13][8], maze_array[14][7], maze_array[13][6]],
                   maze_array[14][7]: [maze_array[13][7], maze_array[14][8], maze_array[15][7], maze_array[14][6]],
                   maze_array[15][7]: [maze_array[14][7], maze_array[15][8], maze_array[16][7], maze_array[15][6]],
                   maze_array[16][7]: [maze_array[15][7], maze_array[16][8], maze_array[17][7], maze_array[16][6]],
                   maze_array[17][7]: [maze_array[16][7], maze_array[17][8], maze_array[18][7], maze_array[17][6]],
                   maze_array[18][7]: [maze_array[17][7], maze_array[18][8], maze_array[19][7], maze_array[18][6]],
                   maze_array[19][7]: [maze_array[18][7], maze_array[19][8], maze_array[19][6]],

                   maze_array[0][8]: [maze_array[1][8], maze_array[0][9], maze_array[0][7]],
                   maze_array[1][8]: [maze_array[0][8], maze_array[1][9], maze_array[2][8], maze_array[1][7]],
                   maze_array[2][8]: [maze_array[1][8], maze_array[2][9], maze_array[3][8], maze_array[2][7]],
                   maze_array[3][8]: [maze_array[2][8], maze_array[3][9], maze_array[4][8], maze_array[3][7]],
                   maze_array[4][8]: [maze_array[3][8], maze_array[4][9], maze_array[5][8], maze_array[4][7]],
                   maze_array[5][8]: [maze_array[4][8], maze_array[5][9], maze_array[6][8], maze_array[5][7]],
                   maze_array[6][8]: [maze_array[5][8], maze_array[6][9], maze_array[7][8], maze_array[6][7]],
                   maze_array[7][8]: [maze_array[6][8], maze_array[7][9], maze_array[8][8], maze_array[7][7]],
                   maze_array[8][8]: [maze_array[7][8], maze_array[8][9], maze_array[9][8], maze_array[8][7]],
                   maze_array[9][8]: [maze_array[8][8], maze_array[9][9], maze_array[10][8], maze_array[9][7]],
                   maze_array[10][8]: [maze_array[9][8], maze_array[10][9], maze_array[11][8], maze_array[10][7]],
                   maze_array[11][8]: [maze_array[10][8], maze_array[11][9], maze_array[12][8], maze_array[11][7]],
                   maze_array[12][8]: [maze_array[11][8], maze_array[12][9], maze_array[13][8], maze_array[12][7]],
                   maze_array[13][8]: [maze_array[12][8], maze_array[13][9], maze_array[14][8], maze_array[13][7]],
                   maze_array[14][8]: [maze_array[13][8], maze_array[14][9], maze_array[15][8], maze_array[14][7]],
                   maze_array[15][8]: [maze_array[14][8], maze_array[15][9], maze_array[16][8], maze_array[15][7]],
                   maze_array[16][8]: [maze_array[15][8], maze_array[16][9], maze_array[17][8], maze_array[16][7]],
                   maze_array[17][8]: [maze_array[16][8], maze_array[17][9], maze_array[18][8], maze_array[17][7]],
                   maze_array[18][8]: [maze_array[17][8], maze_array[18][9], maze_array[19][8], maze_array[18][7]],
                   maze_array[19][8]: [maze_array[18][8], maze_array[19][9], maze_array[19][7]],

                   maze_array[0][9]: [maze_array[1][9], maze_array[0][10], maze_array[0][8]],
                   maze_array[1][9]: [maze_array[0][9], maze_array[1][10], maze_array[2][9], maze_array[1][8]],
                   maze_array[2][9]: [maze_array[1][9], maze_array[2][10], maze_array[3][9], maze_array[2][8]],
                   maze_array[3][9]: [maze_array[2][9], maze_array[3][10], maze_array[4][9], maze_array[3][8]],
                   maze_array[4][9]: [maze_array[3][9], maze_array[4][10], maze_array[5][9], maze_array[4][8]],
                   maze_array[5][9]: [maze_array[4][9], maze_array[5][10], maze_array[6][9], maze_array[5][8]],
                   maze_array[6][9]: [maze_array[5][9], maze_array[6][10], maze_array[7][9], maze_array[6][8]],
                   maze_array[7][9]: [maze_array[6][9], maze_array[7][10], maze_array[8][9], maze_array[7][8]],
                   maze_array[8][9]: [maze_array[7][9], maze_array[8][10], maze_array[9][9], maze_array[8][8]],
                   maze_array[9][9]: [maze_array[8][9], maze_array[9][10], maze_array[10][9], maze_array[9][8]],
                   maze_array[10][9]: [maze_array[9][9], maze_array[10][10], maze_array[11][9], maze_array[10][8]],
                   maze_array[11][9]: [maze_array[10][9], maze_array[11][10], maze_array[12][9], maze_array[11][8]],
                   maze_array[12][9]: [maze_array[11][9], maze_array[12][10], maze_array[13][9], maze_array[12][8]],
                   maze_array[13][9]: [maze_array[12][9], maze_array[13][10], maze_array[14][9], maze_array[13][8]],
                   maze_array[14][9]: [maze_array[13][9], maze_array[14][10], maze_array[15][9], maze_array[14][8]],
                   maze_array[15][9]: [maze_array[14][9], maze_array[15][10], maze_array[16][9], maze_array[15][8]],
                   maze_array[16][9]: [maze_array[15][9], maze_array[16][10], maze_array[17][9], maze_array[16][8]],
                   maze_array[17][9]: [maze_array[16][9], maze_array[17][10], maze_array[18][9], maze_array[17][8]],
                   maze_array[18][9]: [maze_array[17][9], maze_array[18][10], maze_array[19][9], maze_array[18][8]],
                   maze_array[19][9]: [maze_array[18][9], maze_array[19][10], maze_array[19][8]],

                   maze_array[0][10]: [maze_array[1][10], maze_array[0][11], maze_array[0][9]],
                   maze_array[1][10]: [maze_array[0][10], maze_array[1][11], maze_array[2][10], maze_array[1][9]],
                   maze_array[2][10]: [maze_array[1][10], maze_array[2][11], maze_array[3][10], maze_array[2][9]],
                   maze_array[3][10]: [maze_array[2][10], maze_array[3][11], maze_array[4][10], maze_array[3][9]],
                   maze_array[4][10]: [maze_array[3][10], maze_array[4][11], maze_array[5][10], maze_array[4][9]],
                   maze_array[5][10]: [maze_array[4][10], maze_array[5][11], maze_array[6][10], maze_array[5][9]],
                   maze_array[6][10]: [maze_array[5][10], maze_array[6][11], maze_array[7][10], maze_array[6][9]],
                   maze_array[7][10]: [maze_array[6][10], maze_array[7][11], maze_array[8][10], maze_array[7][9]],
                   maze_array[8][10]: [maze_array[7][10], maze_array[8][11], maze_array[9][10], maze_array[8][9]],
                   maze_array[9][10]: [maze_array[8][10], maze_array[9][11], maze_array[10][10], maze_array[9][9]],
                   maze_array[10][10]: [maze_array[9][10], maze_array[10][11], maze_array[11][10], maze_array[10][9]],
                   maze_array[11][10]: [maze_array[10][10], maze_array[11][11], maze_array[12][10], maze_array[11][9]],
                   maze_array[12][10]: [maze_array[11][10], maze_array[12][11], maze_array[13][10], maze_array[12][9]],
                   maze_array[13][10]: [maze_array[12][10], maze_array[13][11], maze_array[14][10], maze_array[13][9]],
                   maze_array[14][10]: [maze_array[13][10], maze_array[14][11], maze_array[15][10], maze_array[14][9]],
                   maze_array[15][10]: [maze_array[14][10], maze_array[15][11], maze_array[16][10], maze_array[15][9]],
                   maze_array[16][10]: [maze_array[15][10], maze_array[16][11], maze_array[17][10], maze_array[16][9]],
                   maze_array[17][10]: [maze_array[16][10], maze_array[17][11], maze_array[18][10], maze_array[17][9]],
                   maze_array[18][10]: [maze_array[17][10], maze_array[18][11], maze_array[19][10], maze_array[18][9]],
                   maze_array[19][10]: [maze_array[18][10], maze_array[19][11], maze_array[19][9]],

                   maze_array[0][11]: [maze_array[1][11], maze_array[0][12], maze_array[0][10]],
                   maze_array[1][11]: [maze_array[0][11], maze_array[1][12], maze_array[2][11], maze_array[1][10]],
                   maze_array[2][11]: [maze_array[1][11], maze_array[2][12], maze_array[3][11], maze_array[2][10]],
                   maze_array[3][11]: [maze_array[2][11], maze_array[3][12], maze_array[4][11], maze_array[3][10]],
                   maze_array[4][11]: [maze_array[3][11], maze_array[4][12], maze_array[5][11], maze_array[4][10]],
                   maze_array[5][11]: [maze_array[4][11], maze_array[5][12], maze_array[6][11], maze_array[5][10]],
                   maze_array[6][11]: [maze_array[5][11], maze_array[6][12], maze_array[7][11], maze_array[6][10]],
                   maze_array[7][11]: [maze_array[6][11], maze_array[7][12], maze_array[8][11], maze_array[7][10]],
                   maze_array[8][11]: [maze_array[7][11], maze_array[8][12], maze_array[9][11], maze_array[8][10]],
                   maze_array[9][11]: [maze_array[8][11], maze_array[9][12], maze_array[10][11], maze_array[9][10]],
                   maze_array[10][11]: [maze_array[9][11], maze_array[10][12], maze_array[11][11], maze_array[10][10]],
                   maze_array[11][11]: [maze_array[10][11], maze_array[11][12], maze_array[12][11], maze_array[11][10]],
                   maze_array[12][11]: [maze_array[11][11], maze_array[12][12], maze_array[13][11], maze_array[12][10]],
                   maze_array[13][11]: [maze_array[12][11], maze_array[13][12], maze_array[14][11], maze_array[13][10]],
                   maze_array[14][11]: [maze_array[13][11], maze_array[14][12], maze_array[15][11], maze_array[14][10]],
                   maze_array[15][11]: [maze_array[14][11], maze_array[15][12], maze_array[16][11], maze_array[15][10]],
                   maze_array[16][11]: [maze_array[15][11], maze_array[16][12], maze_array[17][11], maze_array[16][10]],
                   maze_array[17][11]: [maze_array[16][11], maze_array[17][12], maze_array[18][11], maze_array[17][10]],
                   maze_array[18][11]: [maze_array[17][11], maze_array[18][12], maze_array[19][11], maze_array[18][10]],
                   maze_array[19][11]: [maze_array[18][11], maze_array[19][12], maze_array[19][10]],

                   maze_array[0][12]: [maze_array[1][12], maze_array[0][13], maze_array[0][11]],
                   maze_array[1][12]: [maze_array[0][12], maze_array[1][13], maze_array[2][12], maze_array[1][11]],
                   maze_array[2][12]: [maze_array[1][12], maze_array[2][13], maze_array[3][12], maze_array[2][11]],
                   maze_array[3][12]: [maze_array[2][12], maze_array[3][13], maze_array[4][12], maze_array[3][11]],
                   maze_array[4][12]: [maze_array[3][12], maze_array[4][13], maze_array[5][12], maze_array[4][11]],
                   maze_array[5][12]: [maze_array[4][12], maze_array[5][13], maze_array[6][12], maze_array[5][11]],
                   maze_array[6][12]: [maze_array[5][12], maze_array[6][13], maze_array[7][12], maze_array[6][11]],
                   maze_array[7][12]: [maze_array[6][12], maze_array[7][13], maze_array[8][12], maze_array[7][11]],
                   maze_array[8][12]: [maze_array[7][12], maze_array[8][13], maze_array[9][12], maze_array[8][11]],
                   maze_array[9][12]: [maze_array[8][12], maze_array[9][13], maze_array[10][12], maze_array[9][11]],
                   maze_array[10][12]: [maze_array[9][12], maze_array[10][13], maze_array[11][12], maze_array[10][11]],
                   maze_array[11][12]: [maze_array[10][12], maze_array[11][13], maze_array[12][12], maze_array[11][11]],
                   maze_array[12][12]: [maze_array[11][12], maze_array[12][13], maze_array[13][12], maze_array[12][11]],
                   maze_array[13][12]: [maze_array[12][12], maze_array[13][13], maze_array[14][12], maze_array[13][11]],
                   maze_array[14][12]: [maze_array[13][12], maze_array[14][13], maze_array[15][12], maze_array[14][11]],
                   maze_array[15][12]: [maze_array[14][12], maze_array[15][13], maze_array[16][12], maze_array[15][11]],
                   maze_array[16][12]: [maze_array[15][12], maze_array[16][13], maze_array[17][12], maze_array[16][11]],
                   maze_array[17][12]: [maze_array[16][12], maze_array[17][13], maze_array[18][12], maze_array[17][11]],
                   maze_array[18][12]: [maze_array[17][12], maze_array[18][13], maze_array[19][12], maze_array[18][11]],
                   maze_array[19][12]: [maze_array[18][12], maze_array[19][13], maze_array[19][11]],

                   maze_array[0][13]: [maze_array[1][13], maze_array[0][14], maze_array[0][12]],
                   maze_array[1][13]: [maze_array[0][13], maze_array[1][14], maze_array[2][13], maze_array[1][12]],
                   maze_array[2][13]: [maze_array[1][13], maze_array[2][14], maze_array[3][13], maze_array[2][12]],
                   maze_array[3][13]: [maze_array[2][13], maze_array[3][14], maze_array[4][13], maze_array[3][12]],
                   maze_array[4][13]: [maze_array[3][13], maze_array[4][14], maze_array[5][13], maze_array[4][12]],
                   maze_array[5][13]: [maze_array[4][13], maze_array[5][14], maze_array[6][13], maze_array[5][12]],
                   maze_array[6][13]: [maze_array[5][13], maze_array[6][14], maze_array[7][13], maze_array[6][12]],
                   maze_array[7][13]: [maze_array[6][13], maze_array[7][14], maze_array[8][13], maze_array[7][12]],
                   maze_array[8][13]: [maze_array[7][13], maze_array[8][14], maze_array[9][13], maze_array[8][12]],
                   maze_array[9][13]: [maze_array[8][13], maze_array[9][14], maze_array[10][13], maze_array[9][12]],
                   maze_array[10][13]: [maze_array[9][13], maze_array[10][14], maze_array[11][13], maze_array[10][12]],
                   maze_array[11][13]: [maze_array[10][13], maze_array[11][14], maze_array[12][13], maze_array[11][12]],
                   maze_array[12][13]: [maze_array[11][13], maze_array[12][14], maze_array[13][13], maze_array[12][12]],
                   maze_array[13][13]: [maze_array[12][13], maze_array[13][14], maze_array[14][13], maze_array[13][12]],
                   maze_array[14][13]: [maze_array[13][13], maze_array[14][14], maze_array[15][13], maze_array[14][12]],
                   maze_array[15][13]: [maze_array[14][13], maze_array[15][14], maze_array[16][13], maze_array[15][12]],
                   maze_array[16][13]: [maze_array[15][13], maze_array[16][14], maze_array[17][13], maze_array[16][12]],
                   maze_array[17][13]: [maze_array[16][13], maze_array[17][14], maze_array[18][13], maze_array[17][12]],
                   maze_array[18][13]: [maze_array[17][13], maze_array[18][14], maze_array[19][13], maze_array[18][12]],
                   maze_array[19][13]: [maze_array[18][13], maze_array[19][14], maze_array[19][12]],

                   maze_array[0][14]: [maze_array[1][14], maze_array[0][15], maze_array[0][13]],
                   maze_array[1][14]: [maze_array[0][14], maze_array[1][15], maze_array[2][14], maze_array[1][13]],
                   maze_array[2][14]: [maze_array[1][14], maze_array[2][15], maze_array[3][14], maze_array[2][13]],
                   maze_array[3][14]: [maze_array[2][14], maze_array[3][15], maze_array[4][14], maze_array[3][13]],
                   maze_array[4][14]: [maze_array[3][14], maze_array[4][15], maze_array[5][14], maze_array[4][13]],
                   maze_array[5][14]: [maze_array[4][14], maze_array[5][15], maze_array[6][14], maze_array[5][13]],
                   maze_array[6][14]: [maze_array[5][14], maze_array[6][15], maze_array[7][14], maze_array[6][13]],
                   maze_array[7][14]: [maze_array[6][14], maze_array[7][15], maze_array[8][14], maze_array[7][13]],
                   maze_array[8][14]: [maze_array[7][14], maze_array[8][15], maze_array[9][14], maze_array[8][13]],
                   maze_array[9][14]: [maze_array[8][14], maze_array[9][15], maze_array[10][14], maze_array[9][13]],
                   maze_array[10][14]: [maze_array[9][14], maze_array[10][15], maze_array[11][14], maze_array[10][13]],
                   maze_array[11][14]: [maze_array[10][14], maze_array[11][15], maze_array[12][14], maze_array[11][13]],
                   maze_array[12][14]: [maze_array[11][14], maze_array[12][15], maze_array[13][14], maze_array[12][13]],
                   maze_array[13][14]: [maze_array[12][14], maze_array[13][15], maze_array[14][14], maze_array[13][13]],
                   maze_array[14][14]: [maze_array[13][14], maze_array[14][15], maze_array[15][14], maze_array[14][13]],
                   maze_array[15][14]: [maze_array[14][14], maze_array[15][15], maze_array[16][14], maze_array[15][13]],
                   maze_array[16][14]: [maze_array[15][14], maze_array[16][15], maze_array[17][14], maze_array[16][13]],
                   maze_array[17][14]: [maze_array[16][14], maze_array[17][15], maze_array[18][14], maze_array[17][13]],
                   maze_array[18][14]: [maze_array[17][14], maze_array[18][15], maze_array[19][14], maze_array[18][13]],
                   maze_array[19][14]: [maze_array[18][14], maze_array[19][15], maze_array[19][13]],

                   maze_array[0][15]: [maze_array[1][15], maze_array[0][16], maze_array[0][14]],
                   maze_array[1][15]: [maze_array[0][15], maze_array[1][16], maze_array[2][15], maze_array[1][14]],
                   maze_array[2][15]: [maze_array[1][15], maze_array[2][16], maze_array[3][15], maze_array[2][14]],
                   maze_array[3][15]: [maze_array[2][15], maze_array[3][16], maze_array[4][15], maze_array[3][14]],
                   maze_array[4][15]: [maze_array[3][15], maze_array[4][16], maze_array[5][15], maze_array[4][14]],
                   maze_array[5][15]: [maze_array[4][15], maze_array[5][16], maze_array[6][15], maze_array[5][14]],
                   maze_array[6][15]: [maze_array[5][15], maze_array[6][16], maze_array[7][15], maze_array[6][14]],
                   maze_array[7][15]: [maze_array[6][15], maze_array[7][16], maze_array[8][15], maze_array[7][14]],
                   maze_array[8][15]: [maze_array[7][15], maze_array[8][16], maze_array[9][15], maze_array[8][14]],
                   maze_array[9][15]: [maze_array[8][15], maze_array[9][16], maze_array[10][15], maze_array[9][14]],
                   maze_array[10][15]: [maze_array[9][15], maze_array[10][16], maze_array[11][15], maze_array[10][14]],
                   maze_array[11][15]: [maze_array[10][15], maze_array[11][16], maze_array[12][15], maze_array[11][14]],
                   maze_array[12][15]: [maze_array[11][15], maze_array[12][16], maze_array[13][15], maze_array[12][14]],
                   maze_array[13][15]: [maze_array[12][15], maze_array[13][16], maze_array[14][15], maze_array[13][14]],
                   maze_array[14][15]: [maze_array[13][15], maze_array[14][16], maze_array[15][15], maze_array[14][14]],
                   maze_array[15][15]: [maze_array[14][15], maze_array[15][16], maze_array[16][15], maze_array[15][14]],
                   maze_array[16][15]: [maze_array[15][15], maze_array[16][16], maze_array[17][15], maze_array[16][14]],
                   maze_array[17][15]: [maze_array[16][15], maze_array[17][16], maze_array[18][15], maze_array[17][14]],
                   maze_array[18][15]: [maze_array[17][15], maze_array[18][16], maze_array[19][15], maze_array[18][14]],
                   maze_array[19][15]: [maze_array[18][15], maze_array[19][16], maze_array[19][14]],

                   maze_array[0][16]: [maze_array[1][16], maze_array[0][17], maze_array[0][15]],
                   maze_array[1][16]: [maze_array[0][16], maze_array[1][17], maze_array[2][16], maze_array[1][15]],
                   maze_array[2][16]: [maze_array[1][16], maze_array[2][17], maze_array[3][16], maze_array[2][15]],
                   maze_array[3][16]: [maze_array[2][16], maze_array[3][17], maze_array[4][16], maze_array[3][15]],
                   maze_array[4][16]: [maze_array[3][16], maze_array[4][17], maze_array[5][16], maze_array[4][15]],
                   maze_array[5][16]: [maze_array[4][16], maze_array[5][17], maze_array[6][16], maze_array[5][15]],
                   maze_array[6][16]: [maze_array[5][16], maze_array[6][17], maze_array[7][16], maze_array[6][15]],
                   maze_array[7][16]: [maze_array[6][16], maze_array[7][17], maze_array[8][16], maze_array[7][15]],
                   maze_array[8][16]: [maze_array[7][16], maze_array[8][17], maze_array[9][16], maze_array[8][15]],
                   maze_array[9][16]: [maze_array[8][16], maze_array[9][17], maze_array[10][16], maze_array[9][15]],
                   maze_array[10][16]: [maze_array[9][16], maze_array[10][17], maze_array[11][16], maze_array[10][15]],
                   maze_array[11][16]: [maze_array[10][16], maze_array[11][17], maze_array[12][16], maze_array[11][15]],
                   maze_array[12][16]: [maze_array[11][16], maze_array[12][17], maze_array[13][16], maze_array[12][15]],
                   maze_array[13][16]: [maze_array[12][16], maze_array[13][17], maze_array[14][16], maze_array[13][15]],
                   maze_array[14][16]: [maze_array[13][16], maze_array[14][17], maze_array[15][16], maze_array[14][15]],
                   maze_array[15][16]: [maze_array[14][16], maze_array[15][17], maze_array[16][16], maze_array[15][15]],
                   maze_array[16][16]: [maze_array[15][16], maze_array[16][17], maze_array[17][16], maze_array[16][15]],
                   maze_array[17][16]: [maze_array[16][16], maze_array[17][17], maze_array[18][16], maze_array[17][15]],
                   maze_array[18][16]: [maze_array[17][16], maze_array[18][17], maze_array[19][16], maze_array[18][15]],
                   maze_array[19][16]: [maze_array[18][16], maze_array[19][17], maze_array[19][15]],

                   maze_array[0][17]: [maze_array[1][17], maze_array[0][18], maze_array[0][16]],
                   maze_array[1][17]: [maze_array[0][17], maze_array[1][18], maze_array[2][17], maze_array[1][16]],
                   maze_array[2][17]: [maze_array[1][17], maze_array[2][18], maze_array[3][17], maze_array[2][16]],
                   maze_array[3][17]: [maze_array[2][17], maze_array[3][18], maze_array[4][17], maze_array[3][16]],
                   maze_array[4][17]: [maze_array[3][17], maze_array[4][18], maze_array[5][17], maze_array[4][16]],
                   maze_array[5][17]: [maze_array[4][17], maze_array[5][18], maze_array[6][17], maze_array[5][16]],
                   maze_array[6][17]: [maze_array[5][17], maze_array[6][18], maze_array[7][17], maze_array[6][16]],
                   maze_array[7][17]: [maze_array[6][17], maze_array[7][18], maze_array[8][17], maze_array[7][16]],
                   maze_array[8][17]: [maze_array[7][17], maze_array[8][18], maze_array[9][17], maze_array[8][16]],
                   maze_array[9][17]: [maze_array[8][17], maze_array[9][18], maze_array[10][17], maze_array[9][16]],
                   maze_array[10][17]: [maze_array[9][17], maze_array[10][18], maze_array[11][17], maze_array[10][16]],
                   maze_array[11][17]: [maze_array[10][17], maze_array[11][18], maze_array[12][17], maze_array[11][16]],
                   maze_array[12][17]: [maze_array[11][17], maze_array[12][18], maze_array[13][17], maze_array[12][16]],
                   maze_array[13][17]: [maze_array[12][17], maze_array[13][18], maze_array[14][17], maze_array[13][16]],
                   maze_array[14][17]: [maze_array[13][17], maze_array[14][18], maze_array[15][17], maze_array[14][16]],
                   maze_array[15][17]: [maze_array[14][17], maze_array[15][18], maze_array[16][17], maze_array[15][16]],
                   maze_array[16][17]: [maze_array[15][17], maze_array[16][18], maze_array[17][17], maze_array[16][16]],
                   maze_array[17][17]: [maze_array[16][17], maze_array[17][18], maze_array[18][17], maze_array[17][16]],
                   maze_array[18][17]: [maze_array[17][17], maze_array[18][18], maze_array[19][17], maze_array[18][16]],
                   maze_array[19][17]: [maze_array[18][17], maze_array[19][18], maze_array[19][16]],

                   maze_array[0][18]: [maze_array[1][18], maze_array[0][19], maze_array[0][17]],
                   maze_array[1][18]: [maze_array[0][18], maze_array[1][19], maze_array[2][18], maze_array[1][17]],
                   maze_array[2][18]: [maze_array[1][18], maze_array[2][19], maze_array[3][18], maze_array[2][17]],
                   maze_array[3][18]: [maze_array[2][18], maze_array[3][19], maze_array[4][18], maze_array[3][17]],
                   maze_array[4][18]: [maze_array[3][18], maze_array[4][19], maze_array[5][18], maze_array[4][17]],
                   maze_array[5][18]: [maze_array[4][18], maze_array[5][19], maze_array[6][18], maze_array[5][17]],
                   maze_array[6][18]: [maze_array[5][18], maze_array[6][19], maze_array[7][18], maze_array[6][17]],
                   maze_array[7][18]: [maze_array[6][18], maze_array[7][19], maze_array[8][18], maze_array[7][17]],
                   maze_array[8][18]: [maze_array[7][18], maze_array[8][19], maze_array[9][18], maze_array[8][17]],
                   maze_array[9][18]: [maze_array[8][18], maze_array[9][19], maze_array[10][18], maze_array[9][17]],
                   maze_array[10][18]: [maze_array[9][18], maze_array[10][19], maze_array[11][18], maze_array[10][17]],
                   maze_array[11][18]: [maze_array[10][18], maze_array[11][19], maze_array[12][18], maze_array[11][17]],
                   maze_array[12][18]: [maze_array[11][18], maze_array[12][19], maze_array[13][18], maze_array[12][17]],
                   maze_array[13][18]: [maze_array[12][18], maze_array[13][19], maze_array[14][18], maze_array[13][17]],
                   maze_array[14][18]: [maze_array[13][18], maze_array[14][19], maze_array[15][18], maze_array[14][17]],
                   maze_array[15][18]: [maze_array[14][18], maze_array[15][19], maze_array[16][18], maze_array[15][17]],
                   maze_array[16][18]: [maze_array[15][18], maze_array[16][19], maze_array[17][18], maze_array[16][17]],
                   maze_array[17][18]: [maze_array[16][18], maze_array[17][19], maze_array[18][18], maze_array[17][17]],
                   maze_array[18][18]: [maze_array[17][18], maze_array[18][19], maze_array[19][18], maze_array[18][17]],
                   maze_array[19][18]: [maze_array[18][18], maze_array[19][19], maze_array[19][17]],

                   maze_array[0][19]: [maze_array[1][19], maze_array[0][18]],
                   maze_array[1][19]: [maze_array[0][19], maze_array[2][19], maze_array[1][18]],
                   maze_array[2][19]: [maze_array[1][19], maze_array[3][19], maze_array[2][18]],
                   maze_array[3][19]: [maze_array[2][19], maze_array[4][19], maze_array[3][18]],
                   maze_array[4][19]: [maze_array[3][19], maze_array[5][19], maze_array[4][18]],
                   maze_array[5][19]: [maze_array[4][19], maze_array[6][19], maze_array[5][18]],
                   maze_array[6][19]: [maze_array[5][19], maze_array[7][19], maze_array[6][18]],
                   maze_array[7][19]: [maze_array[6][19], maze_array[8][19], maze_array[7][18]],
                   maze_array[8][19]: [maze_array[7][19], maze_array[9][19], maze_array[8][18]],
                   maze_array[9][19]: [maze_array[8][19], maze_array[10][19], maze_array[9][18]],
                   maze_array[10][19]: [maze_array[9][19], maze_array[11][19], maze_array[10][18]],
                   maze_array[11][19]: [maze_array[10][19], maze_array[12][19], maze_array[11][18]],
                   maze_array[12][19]: [maze_array[11][19], maze_array[13][19], maze_array[12][18]],
                   maze_array[13][19]: [maze_array[12][19], maze_array[14][19], maze_array[13][18]],
                   maze_array[14][19]: [maze_array[13][19], maze_array[15][19], maze_array[14][18]],
                   maze_array[15][19]: [maze_array[14][19], maze_array[16][19], maze_array[15][18]],
                   maze_array[16][18]: [maze_array[15][19], maze_array[17][19], maze_array[16][18]],
                   maze_array[17][19]: [maze_array[16][19], maze_array[18][19], maze_array[17][18]],
                   maze_array[18][19]: [maze_array[17][19], maze_array[19][19], maze_array[18][18]],
                   maze_array[19][19]: [maze_array[18][19], maze_array[19][18]]}


for x in range(19):
    for y in range(19):
        rand = random.randint(1,2)
        if rand == 1:
            maze_array[x][y] = Floor(LIGHTGRAY, x * 40, y * 40)
            floor_sprite_list.add(maze_array[x][y])
        else:
            maze_array[x][y] = Block(LIGHTGRAY, x * 40, y * 40)
            block_sprite_list.add(maze_array[x][y])
        all_sprites_list.add(maze_array[x][y])
        
        



                 




##floor = Floor(LIGHTGRAY, 40, 40)
##floor_array.append(floor)
##block2 = Block(BLACK, 0, 40)
##block_array.append(block2)
##block = Block(BLACK, 0, 0)
##block_array.append(block)



player = Player(BLUE, 100, 100)

all_sprites_list.add(player)
##all_sprites_list.add(block)
##all_sprites_list.add(floor)
##all_sprites_list.add(block2)
##block_sprite_list.add(block)
##block_sprite_list.add(block2)
##floor_sprite_list.add(floor)

player.blocks = block_sprite_list
player.floors = floor_sprite_list

 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-2,0)
                
            elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(2,0)
                 
            elif event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0,-2)
                
            elif event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0,2)
                


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(2,0)
            elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-2,0)
            elif event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0,2)
            elif event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0,-2)
            
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
    

    #all_sprites_list.remove(player)
    #player.update()
    #all_sprites_list.add(player)
    
    
    all_sprites_list.update()
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
    #print(player.x_speed, player.y_speed)
    
    # --- Drawing code should go here
    all_sprites_list.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
