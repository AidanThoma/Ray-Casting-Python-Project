import pygame
import math
from settings import *

class player:
    def __init__(self):
        self.x = WINDOW_WIDTH / 2
        self.y = WINDOW_HEIGHT / 2 - TILESIZE
        self.radius = 3
        self.turnDirection = 0
        self.walkDirection = 0
        self.rotationAngle = 0
        self.moveSpeed = 2.5
        self.rotationSpeed = 2 * (math.pi / 180)
    #Update method to change angle and position of player
    #Returns nothing
    def update (self):

        keys = pygame.key.get_pressed()

        self.turnDirection = 0
        self.walkDirection = 0

        if keys[pygame.K_RIGHT]:
            self.turnDirection = 1
        if keys[pygame.K_LEFT]:
            self.turnDirection = -1
        if keys[pygame.K_UP]:
            self.walkDirection = 1
        if keys[pygame.K_DOWN]:
            self.walkDirection = -1
        
        self.rotationAngle += self.turnDirection * self.rotationSpeed

        moveStep = self.walkDirection * self.moveSpeed

        self.x += math.cos(self.rotationAngle) * moveStep
        self.y += math.sin(self.rotationAngle) * moveStep

        if self.rotationAngle < 0:
            self.rotationAngle += 2 * math.pi
        if self.rotationAngle > 2 * math.pi:
            self.rotationAngle -= 2 * math.pi
        
    #Method to render player onto screen
    #Returns nothing
    def render(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)


class playerMapEditor:
    def __init__(self, map) -> None:
        self.x = WINDOW_WIDTH / 2
        self.y = WINDOW_HEIGHT / 2 - TILESIZE
        self.moveSpeed = 5
        self.radius = 3
        self.walkDirectionx = 0
        self.walkDirectiony = 0
        self.map = map

        self.old_cords = []
        
    def update (self):

        keys = pygame.key.get_pressed()

        self.walkDirectionx = 0
        self.walkDirectiony = 0

        if keys[pygame.K_UP]:
            self.walkDirectiony = -1
        if keys[pygame.K_DOWN]:
            self.walkDirectiony = 1
        if keys[pygame.K_RIGHT]:
            self.walkDirectionx = 1
        if keys[pygame.K_LEFT]:
            self.walkDirectionx = -1
        # Adding slowing down
        if keys[pygame.K_UP] and keys[pygame.K_LSHIFT]:
            self.walkDirectiony = -0.3
        if keys[pygame.K_DOWN] and keys[pygame.K_LSHIFT]:
            self.walkDirectiony = 0.3
        if keys[pygame.K_RIGHT] and keys[pygame.K_LSHIFT]:
            self.walkDirectionx = 0.3
        if keys[pygame.K_LEFT] and keys[pygame.K_LSHIFT]:
            self.walkDirectionx = -0.3

        # Move player
        self.x += self.walkDirectionx * self.moveSpeed
        self.y += self.walkDirectiony * self.moveSpeed

        # Method to change tile
        # Press space to change tile 
        if keys[pygame.K_SPACE]:

            mapx = int(self.x // TILESIZE)
            mapy = int(self.y // TILESIZE)

            # So I can hold constantly change tiles without needing to worry about them constantly changing
            if [mapx, mapy] not in self.old_cords:
                self.old_cords.append([mapx, mapy])
                self.map.changeTile(mapy, mapx)            

        # Meant to print [this will crash]
        if keys[pygame.K_p]:
            print(self.map)
            pygame.time.wait(500)
        if keys[pygame.K_e]:
            self.map.exportMap()

    # Method to render player onto screen
    # Returns nothing
    def render(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)