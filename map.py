import pygame
from settings import *

class Map:
    #1 means black space 0 means white space
    def __init__(self) -> None:

        self.grid = []
        self.load_grid_file()

    # Trying to load from file

    def load_grid_file(self):
        with open("map.txt", 'r') as file:
            for line in file:
                row = list(map(int, line.split()))
                self.grid.append(row)    
    #Checks if tile space is a 1 or 0
    #Returns either 0 or 1
    def has_wall_at(self, x, y):
        return self.grid[int( y // TILESIZE)][int (x //TILESIZE)]

    #Method for rendering map into pygame
    #Returns nothing
    def render(self, screen):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                #pixel coordinates
                tile_x = j * TILESIZE
                tile_y = i * TILESIZE

                if self.grid[i][j] == 0:
                    pygame.draw.rect(screen, (255, 255, 255), (tile_x, tile_y, TILESIZE, TILESIZE))
                elif self.grid[i][j] == 1:
                    pygame.draw.rect(screen, (40, 40, 40), (tile_x, tile_y, TILESIZE-1, TILESIZE-1))
    
    # Updates the tile
    def changeTile(self, x, y):
        if self.grid[x][y] == 1:
            self.grid[x][y] = 0
        elif self.grid[x][y] == 0:
            self.grid[x][y] = 1  
    
    # Used to print to consol
    def __str__(self) -> str:
        for i in range(len(self.grid)):
                print(self.grid[i])
    
    # Used to export map to file
    # Returns a file called map.txt
    def exportMap(self):
        with open("map.txt", "w") as file:
            for i in range(len(self.grid)):
                # file.write("[")
                for j in range(len(self.grid[0])):
                    file.write(f"{self.grid[i][j]} ")
                # file.write("],")
                file.write("\n")