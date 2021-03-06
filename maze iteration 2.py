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

#sets the movement and life attributes of the player

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

#initiates the player sprite and its boundaries

    def control(self, x, y):

        self.x_speed += x
        self.y_speed += y
#This is how the user controls the player sprite using inputs
            




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

class Enemy(pygame.sprite.Sprite):

    x_speed = 0
    y_speed = 0
    
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20,20])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, RED, [0, 0, 20, 20])

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 100
        self.blocks = None
        self.floors = None



##    def control(self):


        

        

        
        


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

class AdjNode: 
    def __init__(self, data): 
        self.vertex = data 
        self.next = None
  
  
# A class to represent a graph. A graph 
# is the list of the adjacency lists. 
# Size of the array will be the no. of the 
# vertices "V" 
class Graph: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [None] * self.V 
  
    # Function to add an edge in an undirected graph 
    def add_edge(self, src, dest): 
        # Adding the node to the source node 
        node = AdjNode(dest) 
        node.next = self.graph[src] 
        self.graph[src] = node 
  
        # Adding the source node to the destination as 
        # it is the undirected graph 
        node = AdjNode(src) 
        node.next = self.graph[dest] 
        self.graph[dest] = node 

    def print_graph(self): 
        for i in range(self.V): 
            print("Adjacency list of vertex {}\n head".format(i), end="") 
            temp = self.graph[i] 
            while temp: 
                print(" -> {}".format(temp.vertex), end="") 
                temp = temp.next
            print(" \n") 


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

floor_graph =  Graph(400)

##path_array = [["AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AI", "AJ", "AK", "AL", "AM", "AN", "AO", "AP", "AQ", "AR", "AS", "AT"],
##              ["BA", "BB", "BC", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BK", "BL", "BM", "BN", "BO", "BP", "BQ", "BR", "BS", "BT"],
##              ["CA", "CB", "CC", "CD", "CE", "CF", "CG", "CH", "CI", "CJ", "CK", "CL", "CM", "CN", "CO", "CP", "CQ", "CR", "CS", "CT"],
##              ["DA", "DB", "DC", "DD", "DE", "DF", "DG", "DH", "DI", "DJ", "DK", "DL", "DM", "DN", "DO", "DP", "DQ", "DR", "DS", "DT"],
##              ["EA", "EB", "EC", "ED", "EE", "EF", "EG", "EH", "EI", "EJ", "EK", "EL", "EM", "EN", "EO", "EP", "EQ", "ER", "ES", "ET"],
##              ["FA", "FB", "FC", "FD", "FE", "FF", "FG", "FH", "FI", "FJ", "FK", "FL", "FM", "FN", "FO", "FP", "FQ", "FR", "FS", "FT"],
##              ["GA", "GB", "GC", "GD", "GE", "GF", "GG", "GH", "GI", "GJ", "GK", "GL", "GM", "GN", "GO", "GP", "GQ", "GR", "GS", "GT"],
##              ["HA", "HB", "HC", "HD", "HE", "HF", "HG", "HH", "HI", "HJ", "HK", "HL", "HM", "HN", "HO", "HP", "HQ", "HR", "HS", "HT"],
##              ["IA", "IB", "IC", "ID", "IE", "IF", "IG", "IH", "II", "IJ", "IK", "IL", "IM", "IN", "IO", "IP", "IQ", "IR", "IS", "IT"],
##              ["JA", "JB", "JC", "JD", "JE", "JF", "JG", "JH", "JI", "JJ", "JK", "JL", "JM", "JN", "JO", "JP", "JQ", "JR", "JS", "JT"],
##              ["KA", "KB", "KC", "KD", "KE", "KF", "KG", "KH", "KI", "KJ", "KK", "KL", "KM", "KN", "KO", "KP", "KQ", "KR", "KS", "KT"],
##              ["LA", "LB", "LC", "LD", "LE", "LF", "LG", "LH", "LI", "LJ", "LK", "LL", "LM", "LN", "LO", "LP", "LQ", "LR", "LS", "LT"],
##              ["MA", "MB", "MC", "MD", "ME", "MF", "MG", "MH", "MI", "MJ", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT"],
##              ["NA", "NB", "NC", "ND", "NE", "NF", "NG", "NH", "NI", "NJ", "NK", "NL", "NM", "NN", "NO", "NP", "NQ", "NR", "NS", "NT"],
##              ["OA", "OB", "OC", "OD", "OE", "OF", "OG", "OH", "OI", "OJ", "OK", "OL", "OM", "ON", "OO", "OP", "OQ", "OR", "OS", "OT"],
##              ["PA", "PB", "PC", "PD", "PE", "PF", "PG", "PH", "PI", "PJ", "PK", "PL", "PM", "PN", "PO", "PP", "PQ", "PR", "PS", "PT"],
##              ["QA", "QB", "QC", "QD", "QE", "QF", "QG", "QH", "QI", "QJ", "QK", "QL", "QM", "QN", "QO", "QP", "QQ", "QR", "QS", "QT"],
##              ["RA", "RB", "RC", "RD", "RE", "RF", "RG", "RH", "RI", "RJ", "RK", "RL", "RM", "RN", "RO", "RP", "RQ", "RR", "RS", "RT"],
##              ["SA", "SB", "SC", "SD", "SE", "SF", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SP", "SQ", "SR", "SS", "ST"],
##              ["TA", "TB", "TC", "TD", "TE", "TF", "TG", "TH", "TI", "TJ", "TK", "TL", "TM", "TN", "TO", "TP", "TQ", "TR", "TS", "TT"]]
##              
##
##floor_graph = { path_array[0][0]: [],
##                path_array[1][0]: [],
##                   path_array[2][0]: [],
##                   path_array[3][0]: [],
##                   path_array[4][0]: [],
##                   path_array[5][0]: [],
##                   path_array[6][0]: [],
##                   path_array[7][0]: [],
##                   path_array[8][0]: [],
##                   path_array[9][0]: [],
##                   path_array[10][0]: [],
##                   path_array[11][0]: [],
##                   path_array[12][0]: [],
##                   path_array[13][0]: [],
##                   path_array[14][0]: [],
##                   path_array[15][0]: [],
##                   path_array[16][0]: [],
##                   path_array[17][0]: [],
##                   path_array[18][0]: [],
##                   path_array[19][0]: [],
##                   
##                   path_array[0][1]: [],
##                   path_array[1][1]: [],
##                   path_array[2][1]: [],
##                   path_array[3][1]: [],
##                   path_array[4][1]: [],
##                   path_array[5][1]: [],
##                   path_array[6][1]: [],
##                   path_array[7][1]: [],
##                   path_array[8][1]: [],
##                   path_array[9][1]: [],
##                   path_array[10][1]: [],
##                   path_array[11][1]: [],
##                   path_array[12][1]: [],
##                   path_array[13][1]: [],
##                   path_array[14][1]: [],
##                   path_array[15][1]: [],
##                   path_array[16][1]: [],
##                   path_array[17][1]: [],
##                   path_array[18][1]: [],
##                   path_array[19][1]: [],
##                   
##                   path_array[0][2]: [],
##                   path_array[1][2]: [],
##                   path_array[2][2]: [],
##                   path_array[3][2]: [],
##                   path_array[4][2]: [],
##                   path_array[5][2]: [],
##                   path_array[6][2]: [],
##                   path_array[7][2]: [],
##                   path_array[8][2]: [],
##                   path_array[9][2]: [],
##                   path_array[10][2]: [],
##                   path_array[11][2]: [],
##                   path_array[12][2]: [],
##                   path_array[13][2]: [],
##                   path_array[14][2]: [],
##                   path_array[15][2]: [],
##                   path_array[16][2]: [],
##                   path_array[17][2]: [],
##                   path_array[18][2]: [],
##                   path_array[19][2]: [],
##
##
##                   path_array[0][3]: [],
##                   path_array[1][3]: [],
##                   path_array[2][3]: [],
##                   path_array[3][3]: [],
##                   path_array[4][3]: [],
##                   path_array[5][3]: [],
##                   path_array[6][3]: [],
##                   path_array[7][3]: [],
##                   path_array[8][3]: [],
##                   path_array[9][3]: [],
##                   path_array[10][3]: [],
##                   path_array[11][3]: [],
##                   path_array[12][3]: [],
##                   path_array[13][3]: [],
##                   path_array[14][3]: [],
##                   path_array[15][3]: [],
##                   path_array[16][3]: [],
##                   path_array[17][3]: [],
##                   path_array[18][3]: [],
##                   path_array[19][3]: [],
##
##                   path_array[0][4]: [],
##                   path_array[1][4]: [],
##                   path_array[2][4]: [],
##                   path_array[3][4]: [],
##                   path_array[4][4]: [],
##                   path_array[5][4]: [],
##                   path_array[6][4]: [],
##                   path_array[7][4]: [],
##                   path_array[8][4]: [],
##                   path_array[9][4]: [],
##                   path_array[10][4]: [],
##                   path_array[11][4]: [],
##                   path_array[12][4]: [],
##                   path_array[13][4]: [],
##                   path_array[14][4]: [],
##                   path_array[15][4]: [],
##                   path_array[16][4]: [],
##                   path_array[17][4]: [],
##                   path_array[18][4]: [],
##                   path_array[19][4]: [],
##                   
##                   path_array[0][5]: [],
##                   path_array[1][5]: [],
##                   path_array[2][5]: [],
##                   path_array[3][5]: [],
##                   path_array[4][5]: [],
##                   path_array[5][5]: [],
##                   path_array[6][5]: [],
##                   path_array[7][5]: [],
##                   path_array[8][5]: [],
##                   path_array[9][5]: [],
##                   path_array[10][5]: [],
##                   path_array[11][5]: [],
##                   path_array[12][5]: [],
##                   path_array[13][5]: [],
##                   path_array[14][5]: [],
##                   path_array[15][5]: [],
##                   path_array[16][5]: [],
##                   path_array[17][5]: [],
##                   path_array[18][5]: [],
##                   path_array[19][5]: [],
##
##                   path_array[0][6]: [],
##                   path_array[1][6]: [],
##                   path_array[2][6]: [],
##                   path_array[3][6]: [],
##                   path_array[4][6]: [],
##                   path_array[5][6]: [],
##                   path_array[6][6]: [],
##                   path_array[7][6]: [],
##                   path_array[8][6]: [],
##                   path_array[9][6]: [],
##                   path_array[10][6]: [],
##                   path_array[11][6]: [],
##                   path_array[12][6]: [],
##                   path_array[13][6]: [],
##                   path_array[14][6]: [],
##                   path_array[15][6]: [],
##                   path_array[16][6]: [],
##                   path_array[17][6]: [],
##                   path_array[18][6]: [],
##                   path_array[19][6]: [],
##
##                   path_array[0][7]: [],
##                   path_array[1][7]: [],
##                   path_array[2][7]: [],
##                   path_array[3][7]: [],
##                   path_array[4][7]: [],
##                   path_array[5][7]: [],
##                   path_array[6][7]: [],
##                   path_array[7][7]: [],
##                   path_array[8][7]: [],
##                   path_array[9][7]: [],
##                   path_array[10][7]: [],
##                   path_array[11][7]: [],
##                   path_array[12][7]: [],
##                   path_array[13][7]: [],
##                   path_array[14][7]: [],
##                   path_array[15][7]: [],
##                   path_array[16][7]: [],
##                   path_array[17][7]: [],
##                   path_array[18][7]: [],
##                   path_array[19][7]: [],
##
##                   path_array[0][8]: [],
##                   path_array[1][8]: [],
##                   path_array[2][8]: [],
##                   path_array[3][8]: [],
##                   path_array[4][8]: [],
##                   path_array[5][8]: [],
##                   path_array[6][8]: [],
##                   path_array[7][8]: [],
##                   path_array[8][8]: [],
##                   path_array[9][8]: [],
##                   path_array[10][8]: [],
##                   path_array[11][8]: [],
##                   path_array[12][8]: [],
##                   path_array[13][8]: [],
##                   path_array[14][8]: [],
##                   path_array[15][8]: [],
##                   path_array[16][8]: [],
##                   path_array[17][8]: [],
##                   path_array[18][8]: [],
##                   path_array[19][8]: [],
##
##                   path_array[0][9]: [],
##                   path_array[1][9]: [],
##                   path_array[2][9]: [],
##                   path_array[3][9]: [],
##                   path_array[4][9]: [],
##                   path_array[5][9]: [],
##                   path_array[6][9]: [],
##                   path_array[7][9]: [],
##                   path_array[8][9]: [],
##                   path_array[9][9]: [],
##                   path_array[10][9]: [],
##                   path_array[11][9]: [],
##                   path_array[12][9]: [],
##                   path_array[13][9]: [],
##                   path_array[14][9]: [],
##                   path_array[15][9]: [],
##                   path_array[16][9]: [],
##                   path_array[17][9]: [],
##                   path_array[18][9]: [],
##                   path_array[19][9]: [],
##
##                   path_array[0][10]: [],
##                   path_array[1][10]: [],
##                   path_array[2][10]: [],
##                   path_array[3][10]: [],
##                   path_array[4][10]: [],
##                   path_array[5][10]: [],
##                   path_array[6][10]: [],
##                   path_array[7][10]: [],
##                   path_array[8][10]: [],
##                   path_array[9][10]: [],
##                   path_array[10][10]: [],
##                   path_array[11][10]: [],
##                   path_array[12][10]: [],
##                   path_array[13][10]: [],
##                   path_array[14][10]: [],
##                   path_array[15][10]: [],
##                   path_array[16][10]: [],
##                   path_array[17][10]: [],
##                   path_array[18][10]: [],
##                   path_array[19][10]: [],
##
##                   path_array[0][11]: [],
##                   path_array[1][11]: [],
##                   path_array[2][11]: [],
##                   path_array[3][11]: [],
##                   path_array[4][11]: [],
##                   path_array[5][11]: [],
##                   path_array[6][11]: [],
##                   path_array[7][11]: [],
##                   path_array[8][11]: [],
##                   path_array[9][11]: [],
##                   path_array[10][11]: [],
##                   path_array[11][11]: [],
##                   path_array[12][11]: [],
##                   path_array[13][11]: [],
##                   path_array[14][11]: [],
##                   path_array[15][11]: [],
##                   path_array[16][11]: [],
##                   path_array[17][11]: [],
##                   path_array[18][11]: [],
##                   path_array[19][11]: [],
##
##                   path_array[0][12]: [],
##                   path_array[1][12]: [],
##                   path_array[2][12]: [],
##                   path_array[3][12]: [],
##                   path_array[4][12]: [],
##                   path_array[5][12]: [],
##                   path_array[6][12]: [],
##                   path_array[7][12]: [],
##                   path_array[8][12]: [],
##                   path_array[9][12]: [],
##                   path_array[10][12]: [],
##                   path_array[11][12]: [],
##                   path_array[12][12]: [],
##                   path_array[13][12]: [],
##                   path_array[14][12]: [],
##                   path_array[15][12]: [],
##                   path_array[16][12]: [],
##                   path_array[17][12]: [],
##                   path_array[18][12]: [],
##                   path_array[19][12]: [],
##
##                   path_array[0][13]: [],
##                   path_array[1][13]: [],
##                   path_array[2][13]: [],
##                   path_array[3][13]: [],
##                   path_array[4][13]: [],
##                   path_array[5][13]: [],
##                   path_array[6][13]: [],
##                   path_array[7][13]: [],
##                   path_array[8][13]: [],
##                   path_array[9][13]: [],
##                   path_array[10][13]: [],
##                   path_array[11][13]: [],
##                   path_array[12][13]: [],
##                   path_array[13][13]: [],
##                   path_array[14][13]: [],
##                   path_array[15][13]: [],
##                   path_array[16][13]: [],
##                   path_array[17][13]: [],
##                   path_array[18][13]: [],
##                   path_array[19][13]: [],
##
##                   path_array[0][14]: [],
##                   path_array[1][14]: [],
##                   path_array[2][14]: [],
##                   path_array[3][14]: [],
##                   path_array[4][14]: [],
##                   path_array[5][14]: [],
##                   path_array[6][14]: [],
##                   path_array[7][14]: [],
##                   path_array[8][14]: [],
##                   path_array[9][14]: [],
##                   path_array[10][14]: [],
##                   path_array[11][14]: [],
##                   path_array[12][14]: [],
##                   path_array[13][14]: [],
##                   path_array[14][14]: [],
##                   path_array[15][14]: [],
##                   path_array[16][14]: [],
##                   path_array[17][14]: [],
##                   path_array[18][14]: [],
##                   path_array[19][14]: [],
##
##                   path_array[0][15]: [],
##                   path_array[1][15]: [],
##                   path_array[2][15]: [],
##                   path_array[3][15]: [],
##                   path_array[4][15]: [],
##                   path_array[5][15]: [],
##                   path_array[6][15]: [],
##                   path_array[7][15]: [],
##                   path_array[8][15]: [],
##                   path_array[9][15]: [],
##                   path_array[10][15]: [],
##                   path_array[11][15]: [],
##                   path_array[12][15]: [],
##                   path_array[13][15]: [],
##                   path_array[14][15]: [],
##                   path_array[15][15]: [],
##                   path_array[16][15]: [],
##                   path_array[17][15]: [],
##                   path_array[18][15]: [],
##                   path_array[19][15]: [],
##
##                   path_array[0][16]: [],
##                   path_array[1][16]: [],
##                   path_array[2][16]: [],
##                   path_array[3][16]: [],
##                   path_array[4][16]: [],
##                   path_array[5][16]: [],
##                   path_array[6][16]: [],
##                   path_array[7][16]: [],
##                   path_array[8][16]: [],
##                   path_array[9][16]: [],
##                   path_array[10][16]: [],
##                   path_array[11][16]: [],
##                   path_array[12][16]: [],
##                   path_array[13][16]: [],
##                   path_array[14][16]: [],
##                   path_array[15][16]: [],
##                   path_array[16][16]: [],
##                   path_array[17][16]: [],
##                   path_array[18][16]: [],
##                   path_array[19][16]: [],
##
##                   path_array[0][17]: [],
##                   path_array[1][17]: [],
##                   path_array[2][17]: [],
##                   path_array[3][17]: [],
##                   path_array[4][17]: [],
##                   path_array[5][17]: [],
##                   path_array[6][17]: [],
##                   path_array[7][17]: [],
##                   path_array[8][17]: [],
##                   path_array[9][17]: [],
##                   path_array[10][17]: [],
##                   path_array[11][17]: [],
##                   path_array[12][17]: [],
##                   path_array[13][17]: [],
##                   path_array[14][17]: [],
##                   path_array[15][17]: [],
##                   path_array[16][17]: [],
##                   path_array[17][17]: [],
##                   path_array[18][17]: [],
##                   path_array[19][17]: [],
##
##                   path_array[0][18]: [],
##                   path_array[1][18]: [],
##                   path_array[2][18]: [],
##                   path_array[3][18]: [],
##                   path_array[4][18]: [],
##                   path_array[5][18]: [],
##                   path_array[6][18]: [],
##                   path_array[7][18]: [],
##                   path_array[8][18]: [],
##                   path_array[9][18]: [],
##                   path_array[10][18]: [],
##                   path_array[11][18]: [],
##                   path_array[12][18]: [],
##                   path_array[13][18]: [],
##                   path_array[14][18]: [],
##                   path_array[15][18]: [],
##                   path_array[16][18]: [],
##                   path_array[17][18]: [],
##                   path_array[18][18]: [],
##                   path_array[19][18]: [],
##
##                   path_array[0][19]: [],
##                   path_array[1][19]: [],
##                   path_array[2][19]: [],
##                   path_array[3][19]: [],
##                   path_array[4][19]: [],
##                   path_array[5][19]: [],
##                   path_array[6][19]: [],
##                   path_array[7][19]: [],
##                   path_array[8][19]: [],
##                   path_array[9][19]: [],
##                   path_array[10][19]: [],
##                   path_array[11][19]: [],
##                   path_array[12][19]: [],
##                   path_array[13][19]: [],
##                   path_array[14][19]: [],
##                   path_array[15][19]: [],
##                   path_array[16][19]: [],
##                   path_array[17][19]: [],
##                   path_array[18][19]: [],
##                   path_array[19][19]: []
##                }




def maze_initiate():

    for x in range(20):
        for y in range(20):
            maze_array[x][y] = Block(BLACK, x * 40, y * 40)
            block_sprite_list.add(maze_array[x][y])
            all_sprites_list.add(maze_array[x][y])

#set a starting block
    random_int = [random.randint(0,19), random.randint(0,19), random.randint(0,19), random.randint(0,19)]

    block_sprite_list.remove(maze_array[0][random_int[0]])
    all_sprites_list.remove(maze_array[0][random_int[0]])
    maze_array[0][random_int[0]] = Floor(LIGHTGRAY, 0, random_int[0] * 40)
    floor_sprite_list.add(maze_array[0][random_int[0]])
    all_sprites_list.add(maze_array[0][random_int[0]])
    floor_array.append(maze_array[0][random_int[0]])
    

    leftside_x = 0
    leftside_y = random_int[0]
    leftside_connect = False
    previous_leftside = None 
    #create a block on the left side on the screen which will be the starting point for the left path
    
    block_sprite_list.remove(maze_array[19][random_int[1]])
    all_sprites_list.remove(maze_array[19][random_int[1]])
    maze_array[19][random_int[1]] = Floor(LIGHTGRAY, 19* 40, random_int[1] * 40)
    floor_sprite_list.add(maze_array[19][random_int[1]])
    all_sprites_list.add(maze_array[19][random_int[1]])
    floor_array.append(maze_array[19][random_int[1]])
    
    

    rightside_x = 19
    rightside_y = random_int[1]
    rightside_connect = False
    previous_rightside = None
    #create a block on the right which will be a starting point for the right path
    
    block_sprite_list.remove(maze_array[random_int[2]][0])
    all_sprites_list.remove(maze_array[random_int[2]][0])
    maze_array[random_int[2]][0] = Floor(LIGHTGRAY, random_int[2] * 40, 0)
    floor_sprite_list.add(maze_array[random_int[2]][0])
    all_sprites_list.add(maze_array[random_int[2]][0])
    floor_array.append(maze_array[random_int[2]][0])
    

    top_x = random_int[2]
    top_y = 0
    top_connect = False
    previous_top = None
    #create a block on the top side of the screen which will be a starting point for that path
    

    block_sprite_list.remove(maze_array[random_int[3]][19])
    all_sprites_list.remove(maze_array[random_int[3]][19])
    maze_array[random_int[3]][19] = Floor(LIGHTGRAY, random_int[3] * 40, 19 * 40)
    floor_sprite_list.add(maze_array[random_int[3]][19])
    all_sprites_list.add(maze_array[random_int[3]][19])
    floor_array.append(maze_array[random_int[3]][19])
    

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
                if isinstance(maze_array[top_x][top_y], Block) == True: #!= Floor(LIGHTGRAY, top_x * 40, top_y * 40):

                    block_sprite_list.remove(maze_array[top_x][top_y])
                    all_sprites_list.remove(maze_array[top_x][top_y])
                    
                    maze_array[top_x][top_y] = Floor(LIGHTGRAY, top_x * 40, top_y * 40) # this removes the block holding the position and places a floor in its place
                    all_sprites_list.add(maze_array[top_x][top_y])
                    floor_sprite_list.add(maze_array[top_x][top_y])


                    

                else:
                    top_x -= 1
                    top_connect = True
                #This checks whether the next block on the right is part of the floor class and if not it replaces the prior block with 
            
            if random_top == 1:
                top_y += 1
                if isinstance(maze_array[top_x][top_y], Block) == True: #!= Floor(LIGHTGRAY, top_x * 40, top_y * 40):
                    block_sprite_list.remove(maze_array[top_x][top_y])
                    all_sprites_list.remove(maze_array[top_x][top_y])

                    maze_array[top_x][top_y] = Floor(LIGHTGRAY, top_x * 40, top_y * 40) # this removes the block holding the position and places a floor in its place
                    all_sprites_list.add(maze_array[top_x][top_y])
                    floor_sprite_list.add(maze_array[top_x][top_y])


                else:
                    top_y -= 1
                    top_connect = True
                
                    
            if random_top == 2:
                top_x -= 1
                if isinstance(maze_array[top_x][top_y], Block) == True:# != Floor(LIGHTGRAY, top_x * 40, top_y * 40):
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
                    block_sprite_list.remove(maze_array[leftside_x][leftside_y])
                    all_sprites_list.remove(maze_array[leftside_x][leftside_y])

                    maze_array[leftside_x][leftside_y] = Floor(LIGHTGRAY, leftside_x * 40, leftside_y * 40)
                    all_sprites_list.add(maze_array[leftside_x][leftside_y])
                    floor_sprite_list.add(maze_array[leftside_x][leftside_y])


                else:
                    leftside_y += 1
                    leftside_connect = True
                

            if random_leftside == 1:
                leftside_x += 1
                if isinstance(maze_array[leftside_x][leftside_y], Block) == True: # != Floor(LIGHTGRAY, leftside_x * 40, leftside_y * 40):
                    block_sprite_list.remove(maze_array[leftside_x][leftside_y])
                    all_sprites_list.remove(maze_array[leftside_x][leftside_y])

                    maze_array[leftside_x][leftside_y] = Floor(LIGHTGRAY, leftside_x * 40, leftside_y * 40)
                    all_sprites_list.add(maze_array[leftside_x][leftside_y])
                    floor_sprite_list.add(maze_array[leftside_x][leftside_y])


                                
                else:
                    leftside_x -= 1
                    leftside_connect = True
                
                    
            if random_leftside == 2:
                leftside_y += 1
                if isinstance(maze_array[leftside_x][leftside_y], Block) == True: # != Floor(LIGHTGRAY, leftside_x * 40, leftside_y * 40):
                    block_sprite_list.remove(maze_array[leftside_x][leftside_y])
                    all_sprites_list.remove(maze_array[leftside_x][leftside_y])

                    maze_array[leftside_x][leftside_y] = Floor(LIGHTGRAY, leftside_x * 40, leftside_y * 40)
                    all_sprites_list.add(maze_array[leftside_x][leftside_y])
                    floor_sprite_list.add(maze_array[leftside_x][leftside_y])


                    
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
                    block_sprite_list.remove(maze_array[rightside_x][rightside_y])
                    all_sprites_list.remove(maze_array[rightside_x][rightside_y])
                    
                    maze_array[rightside_x][rightside_y] = Floor(LIGHTGRAY, rightside_x * 40, rightside_y * 40)
                    all_sprites_list.add(maze_array[rightside_x][rightside_y])
                    floor_sprite_list.add(maze_array[rightside_x][rightside_y])


                    
                else:
                    rightside_y += 1
                    rightside_connect = True
                



            if random_rightside == 2:
                rightside_y += 1
                if isinstance(maze_array[rightside_x][rightside_y], Block) == True: # != Floor(LIGHTGRAY, rightside_x * 40, rightside_y * 40):
                    block_sprite_list.remove(maze_array[rightside_x][rightside_y])
                    all_sprites_list.remove(maze_array[rightside_x][rightside_y])

                    maze_array[rightside_x][rightside_y] = Floor(LIGHTGRAY, rightside_x * 40, rightside_y * 40)
                    all_sprites_list.add(maze_array[rightside_x][rightside_y])
                    floor_sprite_list.add(maze_array[rightside_x][rightside_y])


                    
                else:
                    rightside_y -= 1
                    rightside_connect = True
                
                    
            if random_rightside == 1:
                rightside_x -= 1
                if isinstance(maze_array[rightside_x][rightside_y], Block) == True: # != Floor(LIGHTGRAY, rightside_x * 40, rightside_y * 40):
                
                    block_sprite_list.remove(maze_array[rightside_x][rightside_y])
                    all_sprites_list.remove(maze_array[rightside_x][rightside_y])
                    
                    maze_array[rightside_x][rightside_y] = Floor(LIGHTGRAY, rightside_x * 40, rightside_y * 40)
                    all_sprites_list.add(maze_array[rightside_x][rightside_y])
                    floor_sprite_list.add(maze_array[rightside_x][rightside_y])


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
                    block_sprite_list.remove(maze_array[bottom_x][bottom_y])
                    all_sprites_list.remove(maze_array[bottom_x][bottom_y])

                    
                    maze_array[bottom_x][bottom_y] = Floor(LIGHTGRAY, bottom_x * 40, bottom_y * 40)
                    all_sprites_list.add(maze_array[bottom_x][bottom_y])
                    floor_sprite_list.add(maze_array[bottom_x][bottom_y])


                else:
                    bottom_y += 1
                    bottom_connect = True
                previous_bottom = random_bottom                     

            if random_bottom == 2:
                bottom_x += 1
                if isinstance(maze_array[bottom_x][bottom_y], Block) == True: # != Floor(LIGHTGRAY, bottom_x * 40, bottom_y * 40):
                    block_sprite_list.remove(maze_array[bottom_x][bottom_y])
                    all_sprites_list.remove(maze_array[bottom_x][bottom_y])
                    
                    maze_array[bottom_x][bottom_y] = Floor(LIGHTGRAY, bottom_x * 40, bottom_y * 40)
                    all_sprites_list.add(maze_array[bottom_x][bottom_y])
                    floor_sprite_list.add(maze_array[bottom_x][bottom_y])


                else:
                    bottom_x -= 1
                    bottom_connect = True
                previous_bottom = random_bottom


                  
                
            if random_bottom == 0:
                bottom_x -= 1
                if isinstance(maze_array[bottom_x][bottom_y], Block) == True: # != Floor(LIGHTGRAY, bottom_x * 40, bottom_y * 40):
                    block_sprite_list.remove(maze_array[bottom_x][bottom_y])
                    all_sprites_list.remove(maze_array[bottom_x][bottom_y])
                    
                    maze_array[bottom_x][bottom_y] = Floor(LIGHTGRAY, bottom_x * 40, bottom_y * 40)
                    all_sprites_list.add(maze_array[bottom_x][bottom_y])
                    floor_sprite_list.add(maze_array[bottom_x][bottom_y])


                else:
                    bottom_x += 1
                    bottom_connect = True
                previous_bottom = random_bottom
        else:
            bottom_connect = True


        if leftside_connect == True and top_connect == True and rightside_connect == True and bottom_connect == True:
            reach_floor = True



def graph_edge_connection():
    n = 0
    for floor in floor_sprite_list:
        x_pos_floor = floor.rect.x
        y_pos_floor = floor.rect.y
        for other_floor in floor_sprite_list:
            if x_pos_floor != other_floor.rect.x:
                if (x_pos_floor == other_floor.rect.x + 40 or x_pos_floor == other_floor.rect.x - 40) and y_pos_floor == other_floor.rect.y:
                    n = n + 1
                    if x_pos_floor == other_floor.rect.x + 40:
                        floor_graph.add_edge(floor, other_floor)
                    if x_pos_floor == other_floor.rect.x - 40:
                        floor_graph.add_edge(floor, other_floor)
            if y_pos_floor != other_floor.rect.y:
                if ( y_pos_floor == other_floor.rect.y + 40 or y_pos_floor == other_floor.rect.y - 40 ) and x_pos_floor == other_floor.rect.x:
                    if y_pos_floor == other_floor.rect.y + 40:
                        floor_graph.add_edge(floor, other_floor)
                    if y_pos_floor == other_floor.rect.y - 40:
                        floor_graph.add_edge(floor, other_floor)
    print(n)



maze_initiate()
graph_edge_connection()                 

#floor_graph.print_graph()

l = 0
for floor in floor_sprite_list:
    l = l + 1
print(l)
enemy = Enemy()

player = Player(BLUE, 100, 100)

##def ai_movement():
##
##        player_floor_x_pos = player.rect.x // 40
##        player_floor_y_pos = player.rect.y // 40
##        
##        enemy_floor_x_pos = enemy.rect.x // 40
##        enemy_floor_y_pos = enemy.rect.y // 40

        


        

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
