#Aidan Thoma 11/14/2024
#All raytracing credit go to Pythonista_ and this youtube video https://www.youtube.com/watch?v=E18bSJezaUE
import pygame
from settings import *
from map import *
from player import *
from raycaster import *
from Renderers import *

#Initilize mode from user input

print("modes\n 2d: 1\n 3d: 2\n MapEditor: 3")

user_input = 0

while user_input != 1 and user_input != 2 and user_input != 3:
    try:
        user_input = int(input("Choose mode: "))
    except ValueError:
        print("Invalid input. Please enter a number.")

#Initilize screen, map, player, and background image
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
map = Map()
background_image = pygame.image.load("background.png")


# Used to play in view in 2d
if user_input == 1:
    pygame.display.set_caption("2D Raytracing")
    renderer = TwoD_render(map)
    renderer.render()

# Used to play in 3d
if user_input == 2:
    pygame.display.set_caption('"3D" Raytracing')
    renderer = ThreeD_render(map, background_image)
    renderer.render()

# Used for MapEditing
# Enter to change create/destroy wall
# P to Print to console (will crash)
# E to export to file
if user_input == 3:
    pygame.display.set_caption("Map Editor")
    renderer = mapEditor(map)
    renderer.render()