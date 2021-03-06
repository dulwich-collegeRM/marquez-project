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

#This is the player class which governs the users sprite as it manouvers around in the game

class Player(pygame.sprite.Sprite):
    
    x_speed = 0
    y_speed = 0
    lives = 3

#This function initiates the player's sprite

    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

#This creates the player and sets its starting posiion        
        pygame.draw.rect(self.image, color, [0, 0, 20, 20])

#This sets the players boundaries which can later be used for collisions


        self.rect = self.image.get_rect()
        self.rect.x = x     #This sets the players new x position
        self.rect.y = y     #This sets the players new y position
        self.blocks = None

#This functions controls the players movement by making use of inputs

    def control(self, x, y):

        self.x_speed += x   #This sets the players horizontal rate of movement
        self.y_speed += y   #This sets the players vertical rate of movement

            


# This is the update function, it governs wether the user is colliding agains other sprites

    def update(self):

        self.rect.x += self.x_speed # increases the x coordinate of the player sprite
        
        block_hit_list = pygame.sprite.spritecollide(self, self.blocks, False) 
        for block in block_hit_list:    #Checks if the new proposed position of the player sprite collides with any block sprites
            if self.x_speed > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

                
        self.rect.y += self.y_speed # increases the y coordinate of the player sprite
        
        block_hit_list = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in block_hit_list: #Checks wether the new proposed position collides with any block sprites
            if self.y_speed > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

        floor_standing_list =  pygame.sprite.spritecollide(self, self.floors, False)
        
#This is the block class, it spawns in a block/wall which the player can not pass through

class Block(pygame.sprite.Sprite):

#This functions initiates the block when called

    def __init__(self, colour, x, y):
        super().__init__()
        self.image = pygame.Surface([40, 40])
        self.image.fill(BLACK)


        pygame.draw.rect(self.image, colour, [x, y, 40, 40]) #sets a black square as the block sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        
#This is the floor class which is used to place floors across which the player can traverse

class Floor(pygame.sprite.Sprite):

#This function initiates the floor class
    
    def __init__(self, colour, x, y):
        super().__init__()
        self.image = pygame.Surface([40, 40])
        self.image.fill(LIGHTGRAY)


        pygame.draw.rect(self.image, colour, [x, y, 40, 40]) #sets a gray square as the floor sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


#this array contains all of the floors which have been used by the maze:

floor_array = []
    
#These three groups are used to hold all the different sprites generated by the program

all_sprites_list = pygame.sprite.Group()

block_sprite_list = pygame.sprite.Group()
floor_sprite_list = pygame.sprite.Group()


#This array holds all the positions of the blocks in the maze

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


#This is the main function in the program which initiates the maze

def maze_initiate():

    for x in range(20): #This fills the entirety of the screen with block sprites
        for y in range(20):
            maze_array[x][y] = Block(BLACK, x * 40, y * 40)
            block_sprite_list.add(maze_array[x][y])
            all_sprites_list.add(maze_array[x][y])

    #set a starting block
    random_int = [random.randint(0,19), random.randint(0,19), random.randint(0,19), random.randint(0,19)] #chooses 4 random values which will be assigned as the starting points of the algorithm

    block_sprite_list.remove(maze_array[0][random_int[0]])
    all_sprites_list.remove(maze_array[0][random_int[0]]) #This section removes the block sprite stored in the x position and replaces it with a floor sprite
    maze_array[0][random_int[0]] = Floor(LIGHTGRAY, 0, random_int[0] * 40)
    floor_sprite_list.add(maze_array[0][random_int[0]])
    all_sprites_list.add(maze_array[0][random_int[0]])
    floor_array.append(maze_array[0][random_int[0]])

    leftside_x = 0 #assigns the variables which will be used by the left path
    leftside_y = random_int[0]
    leftside_connect = False
    previous_leftside = None 
    #create a block on the left side on the screen which will be the starting point for the left path
    
    block_sprite_list.remove(maze_array[19][random_int[1]])
    all_sprites_list.remove(maze_array[19][random_int[1]]) #This section removes the block sprite stored in the x position and replaces it with a floor sprite
    maze_array[19][random_int[1]] = Floor(LIGHTGRAY, 19* 40, random_int[1] * 40)
    floor_sprite_list.add(maze_array[19][random_int[1]])
    all_sprites_list.add(maze_array[19][random_int[1]])
    floor_array.append(maze_array[19][random_int[1]])

    rightside_x = 19 #assigns the variables which will be used by the right path
    rightside_y = random_int[1]
    rightside_connect = False
    previous_rightside = None
    #create a block on the right which will be a starting point for the right path
    
    block_sprite_list.remove(maze_array[random_int[2]][0])
    all_sprites_list.remove(maze_array[random_int[2]][0]) #This section removes the block sprite stored in the x position and replaces it with a floor sprite
    maze_array[random_int[2]][0] = Floor(LIGHTGRAY, random_int[2] * 40, 0)
    floor_sprite_list.add(maze_array[random_int[2]][0])
    all_sprites_list.add(maze_array[random_int[2]][0])
    floor_array.append(maze_array[random_int[2]][0])

    top_x = random_int[2] #assigns the variables which will be used by the top path
    top_y = 0
    top_connect = False
    previous_top = None
    #create a block on the top side of the screen which will be a starting point for that path
    

    block_sprite_list.remove(maze_array[random_int[3]][19])
    all_sprites_list.remove(maze_array[random_int[3]][19]) #This section removes the block sprite stored in the x position and replaces it with a floor sprite
    maze_array[random_int[3]][19] = Floor(LIGHTGRAY, random_int[3] * 40, 19 * 40)
    floor_sprite_list.add(maze_array[random_int[3]][19])
    all_sprites_list.add(maze_array[random_int[3]][19])
    floor_array.append(maze_array[random_int[3]][19])

    bottom_x = random_int[3] #assigns the variables which will be used by the bottom path
    bottom_y = 19
    bottom_connect = False
    previous_bottom = None
    #create a block on the bottom of the screen to start the bottom path

    reach_floor = False
    while not reach_floor:


#This is the section of the function which carves a path from the block on the top of the screen


        if top_connect == False: # this sets the clear condition for the maze generation done by the path created from the top of the screen

       # This section of code sets parameters which need to be followed when choosing the next position for the path
      
            if previous_top != None: # this checks if the previous_block variable is empty

                
                if previous_top == 0: #this sets the previous choice of direction as the opposite being the previous path placed

                    previous_top = 2
                elif previous_top == 2: #this sets the previous choice of direction as the opposite being the previous path placed

                    previous_top = 0
                elif previous_top == 1: #this makes there ben no previous block set and the next floor values can be any
                    previous_top = None
            
            
            next_block_top = [0, 1, 2] # this array is used to choose a number, each number correlates to a direction

        #This checks the coordinates of the block to see if in any particular direction is off the screen

            if top_x == 0:
                next_block_top.remove(2) 
            if top_x == 19:
                next_block_top.remove(0)
            if top_y == 19:
                next_block_top.remove(1)
            if previous_top in next_block_top:
                if previous_top != None:

                    next_block_top.remove(previous_top) # THis checks to see if the value of the variable previous block has been removed, if not it is then removed



                    

        if len(next_block_top) != 0:    #This checks if the arrays size is empty and therefore will have no values
            random_top = random.choice(next_block_top)

            

            


            if random_top == 0: #This recognises that the positio of the next block is to the right of the prior one
                top_x += 1
                if isinstance(maze_array[top_x][top_y], Block) == True:  # This checks if the new position is part of a path already
                    block_sprite_list.remove(maze_array[top_x][top_y])
                    all_sprites_list.remove(maze_array[top_x][top_y])
                    maze_array[top_x][top_y] = Floor(LIGHTGRAY, top_x * 40, top_y * 40) # this removes the block holding the position and places a floor in its place
                    all_sprites_list.add(maze_array[top_x][top_y])
                    floor_sprite_list.add(maze_array[top_x][top_y])
                else:
                    top_x -= 1
                    top_connect = True


           
            if random_top == 1: #This recognises that the positio of the next block is below of the prior one
                top_y += 1
                if isinstance(maze_array[top_x][top_y], Block) == True: # This checks if the new position is part of a path already
                    block_sprite_list.remove(maze_array[top_x][top_y])
                    all_sprites_list.remove(maze_array[top_x][top_y])
                    maze_array[top_x][top_y] = Floor(LIGHTGRAY, top_x * 40, top_y * 40) # this removes the block holding the position and places a floor in its place
                    all_sprites_list.add(maze_array[top_x][top_y])
                    floor_sprite_list.add(maze_array[top_x][top_y])
                else:
                    top_y -= 1
                    top_connect = True
                
                    
            if random_top == 2: #This recognises that the positio of the next block is to the left of the prior one
                top_x -= 1
                if isinstance(maze_array[top_x][top_y], Block) == True: # This checks if the new position is part of a path already
                    block_sprite_list.remove(maze_array[top_x][top_y])
                    all_sprites_list.remove(maze_array[top_x][top_y])
                    maze_array[top_x][top_y] = Floor(LIGHTGRAY, top_x * 40, top_y * 40) # this removes the block holding the position and places a floor in its place
                    all_sprites_list.add(maze_array[top_x][top_y])
                    floor_sprite_list.add(maze_array[top_x][top_y])
                else:
                    top_x += 1
                    top_connect = True
            previous_top = random_top
        else:
            top_connect = True

        if leftside_connect == False: # this sets a clear condition for the left path being created


#This repeats the process done by the top block, for the block on the left side

            if previous_leftside!= None:
                if previous_leftside == 0:
                    previous_leftside = 2
                elif previous_leftside == 2:
                    previous_leftside = 0
                elif previous_leftside == 1:
                    previous_leftside = None

            
            next_block_leftside = [0, 1, 2] # This whole section is 

            if leftside_x == 19:
                next_block_leftside.remove(1)
            if leftside_y == 0:
                next_block_leftside.remove(0)
            if leftside_y == 19:
                next_block_leftside.remove(2)
            if previous_leftside in next_block_leftside:
                if previous_leftside != None:
                    next_block_leftside.remove(previous_leftside)
            

                    
        if len(next_block_leftside) != 0:
            random_leftside = random.choice(next_block_leftside)

            if random_leftside == 0: #This recognises that the positio of the next block is on top of the prior one
                leftside_y -= 1
                if isinstance(maze_array[leftside_x][leftside_y], Block) == True: # This checks if the new position is part of a path already
                    block_sprite_list.remove(maze_array[leftside_x][leftside_y])
                    all_sprites_list.remove(maze_array[leftside_x][leftside_y])
                    maze_array[leftside_x][leftside_y] = Floor(LIGHTGRAY, leftside_x * 40, leftside_y * 40) # this removes the block holding the position and places a floor in its place
                    all_sprites_list.add(maze_array[leftside_x][leftside_y])
                    floor_sprite_list.add(maze_array[leftside_x][leftside_y])
                else:
                    leftside_y += 1
                    leftside_connect = True
                

            if random_leftside == 1: #This recognises that the positio of the next block is to the right of the prior one
                leftside_x += 1
                if isinstance(maze_array[leftside_x][leftside_y], Block) == True: # This checks if the new position is part of a path already
                    block_sprite_list.remove(maze_array[leftside_x][leftside_y])
                    all_sprites_list.remove(maze_array[leftside_x][leftside_y])
                    maze_array[leftside_x][leftside_y] = Floor(LIGHTGRAY, leftside_x * 40, leftside_y * 40) # this removes the block holding the position and places a floor in its place
                    all_sprites_list.add(maze_array[leftside_x][leftside_y])
                    floor_sprite_list.add(maze_array[leftside_x][leftside_y])
                else:
                    leftside_x -= 1
                    leftside_connect = True
                
                    
            if random_leftside == 2: #This recognises that the positio of the next block is below the prior one
                leftside_y += 1
                if isinstance(maze_array[leftside_x][leftside_y], Block) == True: # This checks if the new position is part of a path already
                    block_sprite_list.remove(maze_array[leftside_x][leftside_y])
                    all_sprites_list.remove(maze_array[leftside_x][leftside_y])
                    maze_array[leftside_x][leftside_y] = Floor(LIGHTGRAY, leftside_x * 40, leftside_y * 40) # this removes the block holding the position and places a floor in its place
                    all_sprites_list.add(maze_array[leftside_x][leftside_y])
                    floor_sprite_list.add(maze_array[leftside_x][leftside_y])
                else:
                    leftside_y -= 1
                    leftside_connect = True
            previous_leftside = random_leftside
        else:
            leftside_connect = True


        if rightside_connect == False:

#This repeats the process done by the top block, for the block on the right side

            if previous_rightside != None:
                if previous_rightside == 0:
                    previous_rightside = 2
                elif previous_rightside == 2:
                    previous_rightside = 0
                elif previous_rightside == 1:
                    previous_rightside = None
            
            
            next_block_rightside = [0, 1, 2]

            if rightside_x == 0:
                next_block_rightside.remove(1)
            if rightside_y == 0:
                next_block_rightside.remove(0)
            if rightside_y == 19:
                next_block_rightside.remove(2)
            if previous_rightside in next_block_rightside:
                if previous_rightside != None:
                    next_block_rightside.remove(previous_rightside)

        if len(next_block_rightside) != 0:    
            random_rightside = random.choice(next_block_rightside)
                
            if random_rightside == 0:
                rightside_y -= 1
                if isinstance(maze_array[rightside_x][rightside_y], Block) == True: # This checks if the new position is part of a path already
                    block_sprite_list.remove(maze_array[rightside_x][rightside_y])
                    all_sprites_list.remove(maze_array[rightside_x][rightside_y])
                    maze_array[rightside_x][rightside_y] = Floor(LIGHTGRAY, rightside_x * 40, rightside_y * 40) # this removes the block holding the position and places a floor in its place
                    all_sprites_list.add(maze_array[rightside_x][rightside_y])
                    floor_sprite_list.add(maze_array[rightside_x][rightside_y])
                else:
                    rightside_y += 1
                    rightside_connect = True
                



            if random_rightside == 2:
                rightside_y += 1
                if isinstance(maze_array[rightside_x][rightside_y], Block) == True: # This checks if the new position is part of a path already 
                    block_sprite_list.remove(maze_array[rightside_x][rightside_y])
                    all_sprites_list.remove(maze_array[rightside_x][rightside_y])
                    maze_array[rightside_x][rightside_y] = Floor(LIGHTGRAY, rightside_x * 40, rightside_y * 40) # this removes the block holding the position and places a floor in its place
                    all_sprites_list.add(maze_array[rightside_x][rightside_y])
                    floor_sprite_list.add(maze_array[rightside_x][rightside_y])
                else:
                    rightside_y -= 1
                    rightside_connect = True
                
                    
            if random_rightside == 1:
                rightside_x -= 1
                if isinstance(maze_array[rightside_x][rightside_y], Block) == True: # This checks if the new position is part of a path already
                
                    block_sprite_list.remove(maze_array[rightside_x][rightside_y])
                    all_sprites_list.remove(maze_array[rightside_x][rightside_y])
                    maze_array[rightside_x][rightside_y] = Floor(LIGHTGRAY, rightside_x * 40, rightside_y * 40) # this removes the block holding the position and places a floor in its place
                    all_sprites_list.add(maze_array[rightside_x][rightside_y])
                    floor_sprite_list.add(maze_array[rightside_x][rightside_y])
                else:
                    rightside_x += 1
                    rightside_connect = True
            previous_rightside = random_rightside
        else:
            rightside_connect = True


        if bottom_connect == False:

#This repeats the process done by the top block, for the block on the bottom of the screen

            if previous_bottom != None:
                if previous_bottom == 0:
                    previous_bottom = 2
                elif previous_bottom == 2:
                    previous_bottom = 0
                elif previous_bottom == 1:
                    previous_bottom = None
            
            
            next_block_bottom = [0, 1, 2]

            if bottom_x == 0:
                next_block_bottom.remove(0)
            if bottom_x == 19:
                next_block_bottom.remove(2)
            if bottom_y == 0:
                next_block_bottom.remove(1)
            if previous_bottom in next_block_bottom:
                if previous_bottom != None:
                    next_block_bottom.remove(previous_bottom)

        if len(next_block_bottom) != 0:
            random_bottom = random.choice(next_block_bottom)

            if random_bottom == 1:
                bottom_y -= 1
                if isinstance(maze_array[bottom_x][bottom_y], Block) == True: # This checks if the new position is part of a path already
                    block_sprite_list.remove(maze_array[bottom_x][bottom_y])
                    all_sprites_list.remove(maze_array[bottom_x][bottom_y])
                    maze_array[bottom_x][bottom_y] = Floor(LIGHTGRAY, bottom_x * 40, bottom_y * 40) # this removes the block holding the position and places a floor in its place
                    all_sprites_list.add(maze_array[bottom_x][bottom_y])
                    floor_sprite_list.add(maze_array[bottom_x][bottom_y])
                else:
                    bottom_y += 1
                    bottom_connect = True
                previous_bottom = random_bottom                     

            if random_bottom == 2:
                bottom_x += 1
                if isinstance(maze_array[bottom_x][bottom_y], Block) == True: # This checks if the new position is part of a path already
                    block_sprite_list.remove(maze_array[bottom_x][bottom_y])
                    all_sprites_list.remove(maze_array[bottom_x][bottom_y])
                    maze_array[bottom_x][bottom_y] = Floor(LIGHTGRAY, bottom_x * 40, bottom_y * 40) # this removes the block holding the position and places a floor in its place
                    all_sprites_list.add(maze_array[bottom_x][bottom_y])
                    floor_sprite_list.add(maze_array[bottom_x][bottom_y])
                else:
                    bottom_x -= 1
                    bottom_connect = True
                previous_bottom = random_bottom


                  
                
            if random_bottom == 0:
                bottom_x -= 1
                if isinstance(maze_array[bottom_x][bottom_y], Block) == True: # This checks if the new position is part of a path already
                    block_sprite_list.remove(maze_array[bottom_x][bottom_y])
                    all_sprites_list.remove(maze_array[bottom_x][bottom_y])
                    maze_array[bottom_x][bottom_y] = Floor(LIGHTGRAY, bottom_x * 40, bottom_y * 40) # this removes the block holding the position and places a floor in its place
                    all_sprites_list.add(maze_array[bottom_x][bottom_y])
                    floor_sprite_list.add(maze_array[bottom_x][bottom_y])
                else:
                    bottom_x += 1
                    bottom_connect = True
                previous_bottom = random_bottom
        else:
            bottom_connect = True

# This is the clear condition for ending the maze generation algorithm, which occurs when all the paths have connected with one another

        if leftside_connect == True and top_connect == True and rightside_connect == True and bottom_connect == True:
            reach_floor = True





        
# This calls the function to create the maze

maze_initiate()
                 





# This initialises the player and places it in the all sprites list

player = Player(BLUE, 100, 100)

all_sprites_list.add(player)

player.blocks = block_sprite_list
player.floors = floor_sprite_list

 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
#This checks for inputs from key presses and moves the player accordingly
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
