#This file is the settings for our raycaster
import math

TILESIZE = 32


WALL_HEIGHT = 32
LIGHT_LEVEL = 30

ROWS = 10
COLM = 15

WINDOW_WIDTH = COLM * TILESIZE
WINDOW_HEIGHT = ROWS * TILESIZE

FOV = 60 * (math.pi / 180)

RES = 2  # Degree between each ray angle
NUM_RAYS = (WINDOW_WIDTH // RES)