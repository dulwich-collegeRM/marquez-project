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

    #This sets the players directional velocity
    x_speed = 0
    y_speed = 0

#sets the movement and life attributes of the player

    #initialisation function which initialises the player as a sprite with certain parameters
    def __init__(self, color, x, y):
        super().__init__()
        
        self.image = pygame.Surface([20, 20])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        
        pygame.draw.rect(self.image, color, [0, 0, 20, 20])

        #sets the playes appearing immage as well as sets the spawning coordinates of the player
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        #used to hold the walls that the player is colliding with
        self.blocks = None

#initiates the player sprite and its boundaries

    def control(self, x, y):

        #Defines the players directional velocity when called
        self.x_speed += x
        self.y_speed += y

            



    #This function updates the position of the sprite and functions as a collision
    def update(self):

        self.rect.x += self.x_speed

        #Moves the player to a new position
        block_hit_list = pygame.sprite.spritecollide(self, self.blocks, False)
        
        #checks if the new position causes the player to collide with a block
        for block in block_hit_list:
            if self.x_speed > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        #if a collision takes place the player remains at its previous position

                
        self.rect.y += self.y_speed
        #Moves the player to a new position
        
        block_hit_list = pygame.sprite.spritecollide(self, self.blocks, False)
        #checks if the new position causes the player to collide with a block
        
        for block in block_hit_list:
            if self.y_speed > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
        #if a collision takes place the player remains at its previous position

        floor_standing_list =  pygame.sprite.spritecollide(self, self.floors, False)

class Enemy(pygame.sprite.Sprite):

    #initiates the enemy's movement speed

    x_speed = 0
    y_speed = 0

    #function which initiates the class
    def __init__(self, x, y):
        super().__init__()

        #initiates the enemy as a sprite and defines its appearance
        self.image = pygame.Surface([20,20])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, RED, [0, 0, 20, 20])

        #sets the enemy's boundaries as well as its spawning position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.blocks = None
        self.floors = None


    #this is the control functiom which controls the movement of the player
    def control(self, player_x, player_y):

        #checks the players position and oves towards it
        if player_x > self.rect.x:
            self.x_speed = 2
            # if the player is to the right of the enemy move right
        elif player_x < self.rect.x:
            self.x_speed = -2
            #if the player is to the left of the enemy move left
        if player_y > self.rect.y:
            self.y_speed = 2
            #if the player is underneath the enemy move down
        elif player_y < self.rect.y:
            self.y_speed = -2
            #if the player is above the enemy move up
        if player_y == self.rect.y and player_x == self.rect.x:
            print("Game over")
##        self.x_speed += x
##        self.y_speed += y


        

        

        
        


    def update(self):

        self.rect.x += self.x_speed
        #moves the enemy to a new position
        
        block_hit_list = pygame.sprite.spritecollide(self, self.blocks, False)

        #checks if the enemy has collided with any walls
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

##class Graph:
##    #distance = None
##    def __init__(self, V): 
##        self.V = V  
##        self.adj = [[] for i in range(V)]
##        self.distance = [[1000000000000] for i in range(V)]
##        self.prev = [[] for i in range(V)]
##        
##  
##    # add edge to graph  
##    def addEdge (self, s , d ): 
##        self.adj[s].append(d)
##        self.distance[s] = 1000000

##class Node():
##    def __init__(self,parent = None, position = None):
##        self.parent = parent
##        self.position = position
##
##        self.g = 0
##        self.h = 0
##        self.f = 0
##
##    def __eq__(self, other):
##        return self.position == other.position
##    def astar(maze, start, end):
##        
##                # Create start and end node
##        start_node = Node(None, start)
##        start_node.g = 0
##        start_node.h = 0
##        start_node.f = 0
##        end_node = Node(None, end)
##        end_node.g = 0
##        end_node.h = 0
##        end_node.f = 0
##
##        # Initialize both open and closed list
##        open_list = []
##        closed_list = []
##        path_list = []
##
##    # Add the start node
##        open_list.append(start_node)
##
##    # Loop until you find the end
##        while len(open_list) > 0:
##
##        # Get the current node
##            current_node = open_list[0]
##            current_index = 0
##            for index, item in enumerate(open_list):
##                if item.f < current_node.f:
##                    current_node = item
##                    current_index = index
##            
##        # Pop current off open list, add to closed list
##            open_list.pop(current_index)
##            path_list.append(current_index)
##            closed_list.append(current_node)
##
##        # Found the goal
##            if current_node == end_node:
##                path = []
##                current = current_node
##                while current is not None:
##                    path.append(current.position)
##                    current = current.parent
##                return path[::-1] # Return reversed path
##
##        # Generate children
##            children = []
##            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares
##
##            # Get node position
##                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
##
##            # Make sure within range
##                if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
##                    continue
##
##            # Make sure walkable terrain
##                if maze[node_position[0]][node_position[1]] != 0:
##                    continue
##
##            # Create new node
##                new_node = Node(current_node, node_position)
##
##            # Append
##                children.append(new_node)
##
##        # Loop through children
##            for child in children:
##
##            # Child is on the closed list
##                for closed_child in closed_list:
##                    if child == closed_child:
##                        continue
##
##            # Create the f, g, and h values
##                child.g = current_node.g + 1
##                child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
##                child.f = child.g + child.h
##
##            # Child is already in the open list
##                for open_node in open_list:
##                    if child == open_node and child.g > open_node.g:
##                        continue
##
##            # Add the child to the open list
##                open_list.append(child)


    
  



block_array = []
floor_array = []
    

all_sprites_list = pygame.sprite.Group()

block_sprite_list = pygame.sprite.Group()
floor_sprite_list = pygame.sprite.Group()

graph_array = []

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
maze_floor_array = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
                    
floor_array = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
              [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,],
              [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,],
              [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,],
              [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,],
              [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119,],
              [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139,],
              [140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159,],
              [160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179,],
              [180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199,],
              [200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219,],
              [220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,],
              [240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259,],
              [260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279,],
              [280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299,],
              [300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319,],
              [320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339,],
              [340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359,],
              [360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379,],
              [380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399,]]


floor_pos_list = []



def block_replace(x, y):

    block_sprite_list.remove(maze_array[x][y])
    all_sprites_list.remove(maze_array[x][y])
    floor_pos_list.append(floor_array[x][y])
    maze_array[x][y] = Floor(LIGHTGRAY, x * 40, y * 40)
    floor_sprite_list.add(maze_array[x][y])
    all_sprites_list.add(maze_array[x][y])



def maze_initiate():

    for x in range(20):
        for y in range(20):
            maze_array[x][y] = Block(BLACK, x * 40, y * 40)
            block_sprite_list.add(maze_array[x][y])
            all_sprites_list.add(maze_array[x][y])

#set a starting block
    random_int = [random.randint(0,19), random.randint(0,19), random.randint(0,19), random.randint(0,19)]
    
    block_replace(0, random_int[0])

    leftside_x = 0
    leftside_y = random_int[0]
    leftside_connect = False
    previous_leftside = None 
    #create a block on the left side on the screen which will be the starting point for the left path

    block_replace(19, random_int[1])

    rightside_x = 19
    rightside_y = random_int[1]
    rightside_connect = False
    previous_rightside = None
    #create a block on the right which will be a starting point for the right path

    block_replace(random_int[2], 0)

    top_x = random_int[2]
    top_y = 0
    top_connect = False
    previous_top = None
    #create a block on the top side of the screen which will be a starting point for that path
    
    block_replace(random_int[3], 19)

    bottom_x = random_int[3]
    bottom_y = 19
    bottom_connect = False
    previous_bottom = None
    #create a block on the bottom of the screen to start the bottom path

    reach_floor = False
    while not reach_floor:

        if top_connect == False:

      
            if previous_top != None:

                
                if previous_top == 0:

                    previous_top = 2
                elif previous_top == 2:

                    previous_top = 0
                elif previous_top == 1:
                    previous_top = None
            
            
            next_block_top = [0, 1, 2]

            if top_x == 0:
                next_block_top.remove(2)
            if top_x == 19:
                next_block_top.remove(0)
            if top_y == 19:
                next_block_top.remove(1)
            if previous_top in next_block_top:
                if previous_top != None:

                    next_block_top.remove(previous_top)

            #this stops the blocks from appearing on the previous block or outside the screen
        if len(next_block_top) != 0:    
            random_top = random.choice(next_block_top)

            if random_top == 0:
                top_x += 1
                if isinstance(maze_array[top_x][top_y], Block) == True: 

                    block_replace(top_x, top_y)

                else:
                    top_x -= 1
                    top_connect = True
                #This checks whether the next block on the right is part of the floor class and if not it replaces the prior block with 
            
            if random_top == 1:
                top_y += 1
                if isinstance(maze_array[top_x][top_y], Block) == True: 

                    block_replace(top_x, top_y)


                else:
                    top_y -= 1
                    top_connect = True
                
                    
            if random_top == 2:
                top_x -= 1
                if isinstance(maze_array[top_x][top_y], Block) == True:# != Floor(LIGHTGRAY, top_x * 40, top_y * 40):

                    block_replace(top_x, top_y)
                
                else:
                    top_x += 1
                    top_connect = True
            previous_top = random_top
        else:
            top_connect = True

            

        if leftside_connect == False:

            if previous_leftside!= None:
                if previous_leftside == 0:
                    previous_leftside = 2
                elif previous_leftside == 2:
                    previous_leftside = 0
                elif previous_leftside == 1:
                    previous_leftside = None

            
            next_block_leftside = [0, 1, 2]

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

            if random_leftside == 0:
                leftside_y -= 1
                if isinstance(maze_array[leftside_x][leftside_y], Block) == True: # != Floor(LIGHTGRAY, leftside_x * 40, leftside_y * 40):

                    block_replace(leftside_x, leftside_y)

                else:
                    leftside_y += 1
                    leftside_connect = True
                

            if random_leftside == 1:
                leftside_x += 1
                if isinstance(maze_array[leftside_x][leftside_y], Block) == True: # != Floor(LIGHTGRAY, leftside_x * 40, leftside_y * 40):

                    block_replace(leftside_x, leftside_y)
                                
                else:
                    leftside_x -= 1
                    leftside_connect = True
                
                    
            if random_leftside == 2:
                leftside_y += 1
                if isinstance(maze_array[leftside_x][leftside_y], Block) == True: # != Floor(LIGHTGRAY, leftside_x * 40, leftside_y * 40):

                    block_replace(leftside_x, leftside_y)

                else:
                    leftside_y -= 1
                    leftside_connect = True
            previous_leftside = random_leftside
        else:
            leftside_connect = True



        if rightside_connect == False:

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
                if isinstance(maze_array[rightside_x][rightside_y], Block) == True: # != Floor(LIGHTGRAY, rightside_x * 40, rightside_y * 40):

                    block_replace(rightside_x, rightside_y)

                else:
                    rightside_y += 1
                    rightside_connect = True
                



            if random_rightside == 2:
                rightside_y += 1
                if isinstance(maze_array[rightside_x][rightside_y], Block) == True: # != Floor(LIGHTGRAY, rightside_x * 40, rightside_y * 40):

                    block_replace(rightside_x, rightside_y)

                else:
                    rightside_y -= 1
                    rightside_connect = True
                
                    
            if random_rightside == 1:
                rightside_x -= 1
                if isinstance(maze_array[rightside_x][rightside_y], Block) == True: # != Floor(LIGHTGRAY, rightside_x * 40, rightside_y * 40):
                
                    block_replace(rightside_x, rightside_y)

                else:
                    rightside_x += 1
                    rightside_connect = True
            previous_rightside = random_rightside
        else:
            rightside_connect = True


        if bottom_connect == False:

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
                if isinstance(maze_array[bottom_x][bottom_y], Block) == True: # != Floor(LIGHTGRAY, bottom_x * 40, bottom_y * 40):

                    block_replace(bottom_x, bottom_y)

                else:
                    bottom_y += 1
                    bottom_connect = True
                previous_bottom = random_bottom                     

            if random_bottom == 2:
                bottom_x += 1
                if isinstance(maze_array[bottom_x][bottom_y], Block) == True: # != Floor(LIGHTGRAY, bottom_x * 40, bottom_y * 40):

                    block_replace(bottom_x, bottom_y)

                else:
                    bottom_x -= 1
                    bottom_connect = True
                previous_bottom = random_bottom


                  
                
            if random_bottom == 0:
                bottom_x -= 1
                if isinstance(maze_array[bottom_x][bottom_y], Block) == True: # != Floor(LIGHTGRAY, bottom_x * 40, bottom_y * 40):

                    block_replace(bottom_x, bottom_y)

                else:
                    bottom_x += 1
                    bottom_connect = True
                previous_bottom = random_bottom
        else:
            bottom_connect = True


        if leftside_connect == True and top_connect == True and rightside_connect == True and bottom_connect == True:
            reach_floor = True
       



def floor_generation():

    
    for i in range(len(floor_pos_list)-1) :
        floor = floor_pos_list[i]
        y_pos_floor = floor // 20
        x_pos_floor = floor % 20
        maze_floor_array[x_pos_floor][y_pos_floor] = 0




maze_initiate()
floor_generation()


def spawn_player():    
    random_player = random.choice(floor_pos_list)

    return random_player

def spawn_enemy():
    random_enemy = random.choice(floor_pos_list)

    return random_enemy


    


    
        





def ai_movement():

        player_floor_x_pos = player.rect.x // 40
        player_floor_y_pos = player.rect.y // 40
        
        player_pos = player.rect.x + (player.rect.y * 800)
        
        enemy_floor_x_pos = enemy.rect.x // 40
        enemy_floor_y_pos = enemy.rect.y // 40
        
        enemy_pos = enemy.rect.x + (enemy.rect.y * 800)
        enemy.control(player.rect.x, player.rect.y)

        enemy_node = (enemy_floor_x_pos, enemy_floor_y_pos)
        player_node = (player_floor_x_pos, player_floor_y_pos)

        #path = Node.astar(maze_floor_array, enemy_node, player_node)
        #print(path)

        
        

player = Player(BLUE,(spawn_player() // 20) * 40, (spawn_player() % 20) * 40)
enemy = Enemy(((spawn_enemy() // 20) * 40), ((spawn_enemy() % 20) * 40) )
all_sprites_list.add(enemy)
all_sprites_list.add(player)

player.blocks = block_sprite_list
player.floors = floor_sprite_list
enemy.blocks = block_sprite_list
enemy.floors = floor_sprite_list

 
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
    ai_movement()
    

    


    
    
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
