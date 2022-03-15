# Programmed by Piboy314 for Constellation Games 🍝
import pygame, sys, engine, time

from tiles import Tile
from level import Level
from game_data import level_0
from settings import *

# Define Constants
FPS_MAX = 60

# Define variables


# Create pygame stuff
pygame.init() # Initialize pygame
screen = pygame.display.set_mode(WINDOW_SIZE) # Create a window with the size being WINDOW_SIZE
pygame.display.set_caption("Platforms and Pirates")

# Create instances
clock = pygame.time.Clock() # Create a clock for framerate capping and ticks
level = Level(level_0, screen)
colours = engine.Colours()

# Game loop
while True:
    # Get events (mouse click, keyboard press)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Cleanup pygame
            sys.exit() # Quit program


    screen.fill(colours.BLACK)
    level.run()

    pygame.display.update()
    clock.tick(FPS_MAX)
