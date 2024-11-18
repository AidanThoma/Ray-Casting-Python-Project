import pygame
from settings import *
from ray import Ray

class Raycaster:
    def __init__(self, player, map) -> None:
        self.rays = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        self.player = player
        self.map = map

    # Method for rending all of our rays
    # Periodicly adds ray and adds angle
    def castAllRays(self):
        self.rays = []
        rayAngle = (self.player.rotationAngle - FOV/2)
        for i in range(NUM_RAYS):
            ray = Ray(rayAngle, self.player, self.map)
            ray.cast()
            self.rays.append(ray)

            rayAngle += FOV / NUM_RAYS
    
    #Method for rendering a ray
    #Returns nothing
    def render(self, screen):

        i = 0
        for ray in self.rays:

            line_height = (WALL_HEIGHT / ray.distance) * 415

            draw_begin = (WINDOW_HEIGHT / 2) - (line_height / 2)
            draw_end = line_height

            pygame.draw.rect(screen, (ray.color, ray.color, ray.color), (i*RES, draw_begin, RES, draw_end))

            i += 1
    
    def render2d(self, screen):

        i = 0
        for ray in self.rays:
            ray.render(screen)