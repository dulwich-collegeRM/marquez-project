import pygame
import time

#variables wont be changed
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)
YELLOW = (255,255,0)
HEIGHT = 600
WIDTH = 600
done = False

FPS = 60
block_x = 24
block_y = 24
screen_y = 0
screen_x = 0

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My maze")

player_x = 15
player_y = 15

# Speed in pixels per frame
x_speed = 0
y_speed = 0
 
# Current position
x_coord = 30
y_coord = 30

class Player():
    def _init_(self):
        self.shape("square")
        self.color("Blue")
        player_x = 15
        player_y = 15
        
    def draw_player(x,y):
        pygame.draw.rect(screen,BLUE,[x,y,player_x,player_y],0)
    
class Block():
    def _init_(self):
        self.shape("square")
        self.color("white")
        block_x = 24
        block_y = 24
        

#Levels array
levels = []

#the first level
level_0 =(
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXX  XXXXXXXXYXXXXX",
"X  XXXXXX  XXXXX     XXXX",
"X          XXXXX     XXXX",
"XXXXX  XXXXXXXXX     XXXX",
"XXXXX  XXXXXXXXX     XXXX",
"X                    XXXX",
"XXXXXXXXXXX   XXXXXXXXXXX",
"XXXX          XXXXXXXXXXX",
"XXXX                 XXXX",
"XXXX    XXXXXXXXXXX  XXXX",
"XXXX    XXXXXXXXXXX  XXXX",
"XXXX           XX      XX",
"XXXX           XX      XX",
"XXXX           XXXY   XXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"X                    XXXX",
"X                    XXXX",
"X   XXXXXXXXXXXXXXXXXXXXX",
"X   XXXXXXXXXXXXXXXXXXXXX",
"X                    XXXX",
"XXXXXXXX      XXXX   XXXX",
"XXXXXXXX     YXXXX   XXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",)

levels.append(level_0)

#the second level
level_1 =(
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"XXXXXXXXXXXXXXXXXXXXXXXXX")

levels.append(level_1)
#the maze set up code
def maze_setup(level):
    y_count = 0
    for row in level:
        x_count = 0        
        for character in row:
            #print(character)            
            screen_y = 0 + (y_count * 24)
            screen_x = 0 + (x_count * 24)

            if character == "X":
                pygame.draw.rect(screen,BLACK,[screen_x,screen_y,block_x,block_y],0)
            if character == " ":
                pygame.draw.rect(screen,WHITE,[screen_x,screen_y,block_x,block_y],0)
            if character == "Y":
                pygame.draw.rect(screen,YELLOW,[screen_x,screen_y,block_x,block_y],0)
            x_count = x_count + 1
        # Next
        y_count = y_count + 1
    #next
block = Block()


while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0

    print(y_speed)    
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
    maze_setup(levels[0])
    Player.draw_player(x_coord,y_coord)
    clock.tick(60)
    pygame.display.flip()


pygame.quit()
