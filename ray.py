import math, pygame
from settings import *


#This is to normalize angle
#Don't really understand this too well but know it's needed
def normalizeAngle(angle):
    angle = angle % (2 * math.pi)
    if (angle <= 0):
        angle = (2 * math.pi) + angle
    return angle

# Finds hypotonuse
def distance_between(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))

class Ray:
    def __init__(self, angle, player, map):
        self.rayAngle = normalizeAngle(angle)
        self.player = player
        self.map = map

        self.is_facing_down = self.rayAngle > 0 and self.rayAngle < math.pi
        self.is_facing_up = not self.is_facing_down
        self.is_facing_right = self.rayAngle < 0.5 * math.pi or self.rayAngle > 1.5 * math.pi
        self.is_facing_left = not self.is_facing_right

        self.wall_hit_x = 0
        self.wall_hit_y = 0

        self.distance = 0

        self.color = 255

    def cast(self):
        found_horizontal_wall = False
        horizontal_hit_x = 0
        hortizontal_hit_y = 0

        first_intersection_x = None
        first_intersection_y = None
        
        if self.is_facing_up:
            first_intersection_y = ((self.player.y) // TILESIZE) * TILESIZE - 0.001
        elif self.is_facing_down:
            first_intersection_y = ((self.player.y // TILESIZE) * TILESIZE) + TILESIZE

        # finding x
        first_intersection_x = self.player.x + (first_intersection_y - self.player.y) / math.tan(self.rayAngle)

        next_horizontal_x = first_intersection_x
        next_horizontal_y = first_intersection_y

        xa = 0
        ya = 0

        if self.is_facing_up:
            ya = -TILESIZE
        elif self.is_facing_down:
            ya = TILESIZE
        
        # finding xa
        xa = ya / math.tan(self.rayAngle)

        #Make sure ray stays inside window (and check wall by adding xa and ya)
        while( next_horizontal_x <= WINDOW_WIDTH and next_horizontal_x >= 0 and next_horizontal_y <= WINDOW_HEIGHT and next_horizontal_y >= 0):
            if self.map.has_wall_at(next_horizontal_x, next_horizontal_y):
                found_horizontal_wall = True
                horizontal_hit_x = next_horizontal_x
                hortizontal_hit_y = next_horizontal_y
                break
            else:
                next_horizontal_x += xa
                next_horizontal_y += ya
        
        # testing horizontal cheking
        # self.wall_hit_x = horizontal_hit_x
        # self.wall_hit_y = hortizontal_hit_y

        found_vertical_wall = False
        vertical_hit_x = 0
        vertical_hit_y = 0

        if self.is_facing_right:
            first_intersection_x = ((self.player.x // TILESIZE) * TILESIZE) + TILESIZE
        elif self.is_facing_left:
            first_intersection_x = ((self.player.x // TILESIZE) * TILESIZE) - 0.001

        first_intersection_y = self.player.y + (first_intersection_x - self.player.x) * math.tan(self.rayAngle)

        next_verticle_x = first_intersection_x
        next_verticle_y = first_intersection_y

        if self.is_facing_right:
            xa = TILESIZE
        elif self.is_facing_left:
            xa = -TILESIZE
        
        ya = xa * math.tan(self.rayAngle)

        # While inside the window grab the hits for verticle walls
        while (next_verticle_x <= WINDOW_WIDTH and next_verticle_x >= 0 and next_verticle_y <= WINDOW_HEIGHT
               and next_verticle_y >= 0):
            if self.map.has_wall_at(next_verticle_x, next_verticle_y):
                found_vertical_wall = True
                vertical_hit_x = next_verticle_x
                vertical_hit_y = next_verticle_y
                break
            else:
                next_verticle_x += xa
                next_verticle_y += ya

        # Distance Calcutation

        # testing vertical cheking
        # self.wall_hit_x = horizontal_hit_x
        # self.wall_hit_y = hortizontal_hit_y
        
        
        horizontal_distance = 0
        vertical_distance = 0

        if found_horizontal_wall:
            horizontal_distance = distance_between(self.player.x, self.player.y, horizontal_hit_x, hortizontal_hit_y)
        else:
            horizontal_distance = 9999
            
        if found_vertical_wall:
            vertical_distance = distance_between(self.player.x, self.player.y, vertical_hit_x, vertical_hit_y)
        else:
            vertical_distance = 9999


        if horizontal_distance < vertical_distance:
            self.wall_hit_x = horizontal_hit_x
            self.wall_hit_y = hortizontal_hit_y
            self.distance = horizontal_distance
            self.color = 160
        else:
            self.wall_hit_x = vertical_hit_x
            self.wall_hit_y = vertical_hit_y
            self.distance = vertical_distance
            self.color = 255
        
        self.distance *= math.cos(self.player.rotationAngle - self.rayAngle)

        self.color *= (LIGHT_LEVEL / self.distance)
        if (self.color > 255):
            self.color = 255
        elif (self.color < 0):
            self.color = 0
        
    # Method for rending ray into screen
    # Returns nothing
    def render(self, screen):
        #TEMP
        pygame.draw.line(screen, (255, 0, 0), (self.player.x, self.player.y), (self.wall_hit_x, self.wall_hit_y))