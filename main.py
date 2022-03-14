# Programmed by Piboy314 for Constellation Games 🍝
import pygame, sys, engine

from tiles import Tile
from level import Level
from settings import *

# Define Constants
MAX_FPS     = 80

# Define variables


# Create pygame stuff
pygame.init() # Initialize pygame
screen = pygame.display.set_mode(WINDOW_SIZE) # Create a window with the size being WINDOW_SIZE
pygame.display.set_caption("Platforms and Pirates")

# Create instances
clock = pygame.time.Clock() # Create a clock for framerate capping and ticks
colours = engine.Colours()
level = Level(level_map, screen)

# Game loop
while True:
    for event in pygame.event.get(): # Get events (mouse click, keyboard press)
        if event.type == pygame.QUIT:
            pygame.quit() # Cleanup pygame
            sys.exit() # Quit program

    screen.fill(colours.BLACK)
    level.run()

    pygame.display.update()
    clock.tick(MAX_FPS)
