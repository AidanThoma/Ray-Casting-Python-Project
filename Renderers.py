import pygame
from settings import *
from map import *
from player import *
from raycaster import *

# All of thes classes serve as "Scenes" are refencred in main.py

# TwoD_render       Rendered in 2d
# ThreeD_render     Rendered in 3d
# maEditor          Used to create/change and export map

class TwoD_render:
    def __init__(self, map):
        #Initilize screen, map, player, and clock
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.map = map
        self.player1 = player()
        self.raycaster = Raycaster(self.player1, map)


        self.clock = pygame.time.Clock()
    
    def render(self):
        while True:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.player1.update()
            self.raycaster.castAllRays()

            self.map.render(self.screen)
            self.player1.render(self.screen)
            self.raycaster.render2d(self.screen)

            pygame.display.update()


class ThreeD_render:
    def __init__(self, map, image):
        #Initilize screen, map, player, and clock
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.map = map
        self.player1 = player()
        self.raycaster = Raycaster(self.player1, map)

        self.background_image = image

        self.clock = pygame.time.Clock()
    
    def render(self):
        while True:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.player1.update()
            self.raycaster.castAllRays()
            
            self.screen.blit(self.background_image, (0, 0))

            #map.render(screen)
            #player1.render(screen)
            self.raycaster.render(self.screen)
            
            pygame.display.update()


class mapEditor:
    def __init__(self, map) -> None:
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.map = map
        self.player1 = playerMapEditor(self.map)

        self.clock = pygame.time.Clock()

    def render(self):
        while True:
                self.clock.tick(60)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                self.player1.update()

                self.map.render(self.screen)
                self.player1.render(self.screen)
                
                # Checks if space bar is unpressed
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.player1.old_cords = []

                pygame.display.update()