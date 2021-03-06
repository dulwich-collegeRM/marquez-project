import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHTGRAY = (200, 200, 200)
block_array = []
floor_array = []
    

all_sprites_list = pygame.sprite.Group()

block_sprite_list = pygame.sprite.Group()
floor_sprite_list = pygame.sprite.Group()

graph_array = []

##maze_array = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
##              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
##              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
##              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
##              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
##              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
##              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
##              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
##              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
##              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
##              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
##              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
##              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
##              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
##              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
##              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
##              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
##              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
##              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
##              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,]]

##maze_floor_array = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
##                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
##                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
##                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
##                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
##                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
##                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
##                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
##                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
##                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
##                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
##                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
##                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
##                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
##                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
##                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
##                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
##                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
##                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
##                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
                    
##floor_array = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
##              [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,],
##              [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,],
##              [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,],
##              [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,],
##              [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119,],
##              [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139,],
##              [140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159,],
##              [160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179,],
##              [180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199,],
##              [200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219,],
##              [220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,],
##              [240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259,],
##              [260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279,],
##              [280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299,],
##              [300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319,],
##              [320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339,],
##              [340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359,],
##              [360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379,],
##              [380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399,]]



##object_dictionary = {}
##floor_pos_list = []

 
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

#sets the movement and life attributes of the player

    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        #initiates the player as a square sprite
        pygame.draw.rect(self.image, color, [0, 0, 20, 20])


        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.blocks = None

        #initiates the players boundaries

    def control(self, x, y):

        self.x_speed += x
        self.y_speed += y
    #This is how the user controls the player sprite using inputs
            




    def update(self):

        self.rect.x += self.x_speed
        #estimates the players new position
        
        block_hit_list = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in block_hit_list:
            if self.x_speed > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        #if the new estimated position causes a collision do not move the player

                
        self.rect.y += self.y_speed
        #estimates the players new position
        
        block_hit_list = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in block_hit_list:
            if self.y_speed > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
        #if the new estimated position causes a collision do not move the player

        floor_standing_list =  pygame.sprite.spritecollide(self, self.floors, False)

class Enemy(pygame.sprite.Sprite):

    x_speed = 0
    y_speed = 0
    floor_pos = None
    x_pos = None
    y_pos = None
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([20,20])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, RED, [0, 0, 20, 20])

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.blocks = None
        self.floors = None



    def control(self, array):
        #print("jeff")

        self.floor_pos = (self.rect.x // 40) + (20 * (self.rect.y // 40))
        self.x_pos = self.floor_pos // 20
        self.y_pos = self.floor_pos % 20
        

        if array[1] == object_array[self.x_pos + 1][self.y_pos]:
            self.x_speed = 1

        if array[1] == object_array[self.x_pos - 1][self.y_pos]:
            self.x_speed = -1

        if array[1] == object_array[self.x_pos][self.y_pos + 1]:
            self.y_speed = 1

        if array[1] == object_array[self.x_pos][self.y_pos - 1]:
            self.y_speed = -1
                                                
##        if player_x > self.rect.x:
##            self.x_speed = 0
##        elif player_x < self.rect.x:
##            self.x_speed = 0
##        if player_y > self.rect.y:
##            self.y_speed = 0
##        elif player_y < self.rect.y:
##            self.y_speed = 0




        

        

        
        


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



class Maze_game():
    old_player_pos = 100000000
    old_enemy_pos = 100000000

    def __init__(self):
        self.object_array = [['aa', 'ab', 'ac', 'ad', 'ae', 'af', 'ag', 'ah', 'ai', 'aj', 'ak', 'al', 'am', 'an', 'ao', 'ap', 'aq', 'ar', 'as', 'at'],
                ['ba', 'bb', 'bc', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bk', 'bl', 'bm', 'bn', 'bo', 'bp', 'bq', 'br', 'bs', 'bt'],
                ['ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'cg', 'ch', 'ci', 'cj', 'ck', 'cl', 'cm', 'cn', 'co', 'cp', 'cq', 'cr', 'cs', 'ct'],
                ['da', 'db', 'dc', 'dd', 'de', 'df', 'dg', 'dh', 'di', 'dj', 'dk', 'dl', 'dm', 'dn', 'do', 'dp', 'dq', 'dr', 'ds', 'dt'],
                ['ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'eg', 'eh', 'ei', 'ej', 'ek', 'el', 'em', 'en', 'eo', 'ep', 'eq', 'er', 'es', 'et'],
                ['fa', 'fb', 'fc', 'fd', 'fe', 'ff', 'fg', 'fh', 'fi', 'fj', 'fk', 'fl', 'fm', 'fn', 'fo', 'fp', 'fq', 'fr', 'fs', 'ft'],
                ['ga', 'gb', 'gc', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gj', 'gk', 'gl', 'gm', 'gn', 'go', 'gp', 'gq', 'gr', 'gs', 'gt'],
                ['ha', 'hb', 'hc', 'hd', 'he', 'hf', 'hg', 'hh', 'hi', 'hj', 'hk', 'hl', 'hm', 'hn', 'ho', 'hp', 'hq', 'hr', 'hs', 'ht'],
                ['ia', 'ib', 'ic', 'id', 'ie', 'if', 'ig', 'ih', 'ii', 'ij', 'ik', 'il', 'im', 'in', 'io', 'ip', 'iq', 'ir', 'is', 'it'],
                ['ja', 'jb', 'jc', 'jd', 'je', 'jf', 'jg', 'jh', 'ji', 'jj', 'jk', 'jl', 'jm', 'jn', 'jo', 'jp', 'jq', 'jr', 'js', 'jt'],
                ['ka', 'kb', 'kc', 'kd', 'ke', 'kf', 'kg', 'kh', 'ki', 'kj', 'kk', 'kl', 'km', 'kn', 'ko', 'kp', 'kq', 'kr', 'ks', 'kt'],
                ['la', 'lb', 'lc', 'ld', 'le', 'lf', 'lg', 'lh', 'li', 'lj', 'lk', 'll', 'lm', 'ln', 'lo', 'lp', 'lq', 'lr', 'ls', 'lt'],
                ['ma', 'mb', 'mc', 'md', 'me', 'mf', 'mg', 'mh', 'mi', 'mj', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mq', 'mr', 'ms', 'mt'],
                ['na', 'nb', 'nc', 'nd', 'ne', 'nf', 'ng', 'nh', 'ni', 'nj', 'nk', 'nl', 'nm', 'nn', 'no', 'np', 'nq', 'nr', 'ns', 'nt'],
                ['oa', 'ob', 'oc', 'od', 'oe', 'of', 'og', 'oh', 'oi', 'oj', 'ok', 'ol', 'om', 'on', 'oo', 'op', 'oq', 'or', 'os', 'ot'],
                ['pa', 'pb', 'pc', 'pd', 'pe', 'pf', 'pg', 'ph', 'pi', 'pj', 'pk', 'pl', 'pm', 'pn', 'po', 'pp', 'pq', 'pr', 'ps', 'pt'],
                ['qa', 'qb', 'qc', 'qd', 'qe', 'qf', 'qg', 'qh', 'qi', 'qj', 'qk', 'ql', 'qm', 'qn', 'qo', 'qp', 'qq', 'qr', 'qs', 'qt'],
                ['ra', 'rb', 'rc', 'rd', 're', 'rf', 'rg', 'rh', 'ri', 'rj', 'rk', 'rl', 'rm', 'rn', 'ro', 'rp', 'rq', 'rr', 'rs', 'rt'],
                ['sa', 'sb', 'sc', 'sd', 'se', 'sf', 'sg', 'sh', 'si', 'sj', 'sk', 'sl', 'sm', 'sn', 'so', 'sp', 'sq', 'sr', 'ss', 'st'],
                ['ta', 'tb', 'tc', 'td', 'te', 'tf', 'tg', 'th', 'ti', 'tj', 'tk', 'tl', 'tm', 'tn', 'to', 'tp', 'tq', 'tr', 'ts', 'tt']]
        self.array = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
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

        self.floor_array = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
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
        self.maze_floor_array = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
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

        self.object_dictionary = {}
        self.floor_pos_list = []
        self.maze_generate = False
        self.all_sprites_list = pygame.sprite.Group()
        self.block_sprite_list = pygame.sprite.Group()
        self.floor_sprite_list = pygame.sprite.Group()
        
        

        self.player_spawn = False
        self.enemy_spawn = False
        self.start_game = True
        self.test_array = []

#    def game_display():

        
        

    def maze_create(self):


        
    #set a starting block
        random_int = [random.randint(0,19), random.randint(0,19), random.randint(0,19), random.randint(0,19)]
    
        self.maze_floor_array[0][random_int[0]] = 0
        self.floor_pos_list.append(self.floor_array[0][random_int[0]])

        leftside_x = 0
        leftside_y = random_int[0]
        leftside_connect = False
        previous_leftside = None 
        #create a block on the left side on the screen which will be the starting point for the left path

        self.maze_floor_array[19][random_int[1]] = 0
        self.floor_pos_list.append(self.floor_array[19][random_int[1]])

        rightside_x = 19
        rightside_y = random_int[1]
        rightside_connect = False
        previous_rightside = None
        #create a block on the right which will be a starting point for the right path

        self.maze_floor_array[random_int[2]][0] = 0
        self.floor_pos_list.append(self.floor_array[random_int[2]][0])

        top_x = random_int[2]
        top_y = 0
        top_connect = False
        previous_top = None
        #create a block on the top side of the screen which will be a starting point for that path
    
        self.maze_floor_array[random_int[3]][19] = 0
        self.floor_pos_list.append(self.floor_array[random_int[3]][19])

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
                    if self.maze_floor_array[top_x][top_y] == 1:

                        self.maze_floor_array[top_x][top_y] = 0
                        self.floor_pos_list.append(self.floor_array[top_x][top_y])

                    else:
                        top_x -= 1
                        top_connect = True
                    #This checks whether the next block on the right is part of the floor class and if not it replaces the prior block with 
            
                if random_top == 1:
                    top_y += 1
                    if self.maze_floor_array[top_x][top_y] == 1:

                        self.maze_floor_array[top_x][top_y] = 0
                        self.floor_pos_list.append(self.floor_array[top_x][top_y])


                    else:
                        top_y -= 1
                        top_connect = True
                
                    
                if random_top == 2:
                    top_x -= 1
                    if self.maze_floor_array[top_x][top_y] == 1:# != Floor(LIGHTGRAY, top_x * 40, top_y * 40):

                        self.maze_floor_array[top_x][top_y] = 0
                        self.floor_pos_list.append(self.floor_array[top_x][top_y])
                
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
                    if self.maze_floor_array[leftside_x][leftside_y] == 1: # != Floor(LIGHTGRAY, leftside_x * 40, leftside_y * 40):

                        self.maze_floor_array[leftside_x][leftside_y] = 0
                        self.floor_pos_list.append(self.floor_array[leftside_x][leftside_y])

                    else:
                        leftside_y += 1
                        leftside_connect = True
                

                if random_leftside == 1:
                    leftside_x += 1
                    if self.maze_floor_array[leftside_x][leftside_y] == 1: # != Floor(LIGHTGRAY, leftside_x * 40, leftside_y * 40):

                        self.maze_floor_array[leftside_x][leftside_y] = 0
                        self.floor_pos_list.append(self.floor_array[leftside_x][leftside_y])
                                
                    else:
                        leftside_x -= 1
                        leftside_connect = True
                
                    
                if random_leftside == 2:
                    leftside_y += 1
                    if self.maze_floor_array[leftside_x][leftside_y] == 1: # != Floor(LIGHTGRAY, leftside_x * 40, leftside_y * 40):

                        self.maze_floor_array[leftside_x][leftside_y] = 0
                        self.floor_pos_list.append(self.floor_array[leftside_x][leftside_y])

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
                    if self.maze_floor_array[rightside_x][rightside_y] == 1: # != Floor(LIGHTGRAY, rightside_x * 40, rightside_y * 40):

                        self.maze_floor_array[rightside_x][rightside_y] = 0
                        self.floor_pos_list.append(self.floor_array[rightside_x][rightside_y])

                    else:
                        rightside_y += 1
                        rightside_connect = True
                



                if random_rightside == 2:
                    rightside_y += 1
                    if self.maze_floor_array[rightside_x][rightside_y] == 1: # != Floor(LIGHTGRAY, rightside_x * 40, rightside_y * 40):

                        self.maze_floor_array[rightside_x][rightside_y] = 0
                        self.floor_pos_list.append(self.floor_array[rightside_x][rightside_y])

                    else:
                        rightside_y -= 1
                        rightside_connect = True
                
                    
                if random_rightside == 1:
                    rightside_x -= 1
                    if self.maze_floor_array[rightside_x][rightside_y] == 1: # != Floor(LIGHTGRAY, rightside_x * 40, rightside_y * 40):
                
                        self.maze_floor_array[rightside_x][rightside_y] = 0
                        self.floor_pos_list.append(self.floor_array[rightside_x][rightside_y])

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
                    if self.maze_floor_array[bottom_x][bottom_y] == 1: # != Floor(LIGHTGRAY, bottom_x * 40, bottom_y * 40):

                        self.maze_floor_array[bottom_x][bottom_y] = 0
                        self.floor_pos_list.append(self.floor_array[bottom_x][bottom_y])

                    else:
                        bottom_y += 1
                    bottom_connect = True
                    previous_bottom = random_bottom                     
    
                if random_bottom == 2:
                    bottom_x += 1
                    if self.maze_floor_array[bottom_x][bottom_y] == 1: # != Floor(LIGHTGRAY, bottom_x * 40, bottom_y * 40):

                        self.maze_floor_array[bottom_x][bottom_y] = 0
                        self.floor_pos_list.append(self.floor_array[bottom_x][bottom_y])

                    else:
                        bottom_x -= 1
                        bottom_connect = True
                    previous_bottom = random_bottom


                  
                
                if random_bottom == 0:
                    bottom_x -= 1
                    if self.maze_floor_array[bottom_x][bottom_y] == 1: # != Floor(LIGHTGRAY, bottom_x * 40, bottom_y * 40):
    
                        self.maze_floor_array[bottom_x][bottom_y] = 0
                        self.floor_pos_list.append(self.floor_array[bottom_x][bottom_y])

                    else:
                        bottom_x += 1
                        bottom_connect = True
                    previous_bottom = random_bottom
            else:
                bottom_connect = True
    

            if leftside_connect == True and top_connect == True and rightside_connect == True and bottom_connect == True:
                reach_floor = True

        


    def check_floors(self, x, y):

        array = []
        if x != 19:
            if self.maze_floor_array[x+1][y] == 0:
                array.append(self.object_array[x+1][y])
        if x != 0:        
            if self.maze_floor_array[x-1][y] == 0:
                array.append(self.object_array[x-1][y])
        if y != 19:
            if self.maze_floor_array[x][y+1] == 0:
                array.append(self.object_array[x][y+1])
        if y != 0:
            if self.maze_floor_array[x][y-1] == 0:
                array.append(self.object_array[x][y-1])
                
        return array

    def spawn_player(self):    
        random_player = random.choice(self.floor_pos_list)

        return random_player

    def spawn_enemy(self):
        random_enemy = random.choice(self.floor_pos_list)

        return random_enemy



    def game_start(self):

        for i in range(20):
            for j in range(20):
                if self.maze_floor_array[i][j] == 0:
                    self.array[i][j] = Floor(LIGHTGRAY, i * 40, j * 40)
                    self.floor_sprite_list.add(self.array[i][j])
                    self.all_sprites_list.add(self.array[i][j])

                if self.maze_floor_array[i][j] == 1:
                    self.array[i][j] = Block(BLACK, i * 40, j * 40)
                    self.block_sprite_list.add(self.array[i][j])
                    self.all_sprites_list.add(self.array[i][j])

        for k in range(20):
            for l in range(20):
                if self.maze_floor_array[k][l] == 0:
                    self.object_dictionary[self.object_array[k][l]] = self.check_floors(k, l)


        


        
    def breadth_first_search(self, source, dest):

        queue = [[source]]
        explored = []

        if source == dest:
            return "no path"

        while queue:
            path = queue.pop(0)
            node = path[-1]
            
            if node not in explored:

                #print(object_dictionary[node])
                neighbours = self.object_dictionary[node]


                for i in neighbours:
                    new_path = list(path)
                    new_path.append(i)
                    queue.append(new_path)

                    if i == dest:
                        
                        return new_path
                    
                explored.append(path)
                
    def new_block (player_pos, enemy_pos):

        if old_player_pos != player_pos:
            return True
            old_player_pos = player_pos
            return old_player_pos
        
        if old_enemy_pos != enemy_pos:
            return True
            
            old_enemy_pos = enemy_pos
            return old_enemy_pos

##def spawning(self):
##        
##        player_coords = self.spawn_player()
##        player = Player(BLUE,(player_coords // 20) * 40, (player_coords % 20) * 40)
##        self.player_spawn = True
##        self.all_sprites_list.add(player)
##        player.blocks = block_sprite_list
##        player.floors = floor_sprite_list
##        enemy_coords = self.spawn_enemy()
##        enemy = Enemy(((enemy_coords // 20) * 40), ((enemy_coords % 20) * 40) )
##        
##        self.spawn_enemy = True
##        self.all_sprites_list.add(enemy)
##        enemy.blocks = block_sprite_list
##        enemy.floors = floor_sprite_list
##        #enemy.control(enemy_path)

    def ai_movement(self):

        player_floor_x_pos = player.rect.x // 40
        player_floor_y_pos = player.rect.y // 40
                
        player_pos = player.rect.x + (player.rect.y * 800)
                    
        enemy_floor_x_pos = enemy.rect.x // 40
        enemy_floor_y_pos = enemy.rect.y // 40
            
        enemy_pos = enemy.rect.x + (enemy.rect.y * 800)
            


        print(self.breadth_first_search(self.object_array[enemy_floor_x_pos][enemy_floor_y_pos], self.object_array[player_floor_x_pos][player_floor_y_pos]))


    def spawning(self):
        self.player_spawn = True
        self.enemy_spawn = True

maze_game1 = Maze_game()



# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #if gamwe ends end game loop
        if maze_game1.player_spawn == True:        
            if event.type == pygame.KEYDOWN:
            #This is a loo which occurs if a key input is detected
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                #If the key pressed is the left arrow key or the 'a' key the player moves left
                    player.control(-2,0)
                    
                elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.control(2,0)
                #if the key pressed is the right arrow key or the 'd' key the player moves right
                     
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    player.control(0,-2)
                #If the key pressed is the up arrow key or the 'w' key the player moves up
                    
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    player.control(0,2)
                #if the key pressed is the down arrow key or the 's' key move the player down


            if event.type == pygame.KEYUP:
            #If the key is released depending on the key the direction of the players will stop
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
    if maze_game1.start_game == True:
        print("test working")
        maze_game1.maze_create()
        maze_game1.game_start()
        maze_game1.spawning()
        maze_game1.start_game = False
        
#    else:
#        maze_game1.display_menu
        
    if maze_game1.player_spawn == True and maze_game1.enemy_spawn == True:
        player_coords = maze_game1.spawn_player()
        player = Player(BLUE,(player_coords // 20) * 40, (player_coords % 20) * 40)
        maze_game1.all_sprites_list.add(player)
        player.blocks = maze_game1.block_sprite_list
        player.floors = maze_game1.floor_sprite_list

        enemy_coords = maze_game1.spawn_enemy()
        enemy = Enemy(((enemy_coords // 20) * 40), ((enemy_coords % 20) * 40) )
        maze_game1.all_sprites_list.add(enemy)
        enemy.blocks = maze_game1.block_sprite_list
        enemy.floors = maze_game1.floor_sprite_list

        maze_game1.ai_movement()


        maze_game1.enemy_spawn = False
        


        
         
    maze_game1.all_sprites_list.update()
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
    #print(player.x_speed, player.y_speed)
    
    # --- Drawing code should go here
    maze_game1.all_sprites_list.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
