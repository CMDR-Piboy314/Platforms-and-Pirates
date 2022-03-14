# Programmed by Piboy314 for Constellation Games 🍝
import pygame, sys, engine, time, globals

from tiles import Tile
from level import Level
from settings import *
from globals import *

globals.init()

# Define Constants
FPS_MAX = 60

# Define variables
last_time = time.time()

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
    # Calculate Delta Time
    globals.dt = time.time() - last_time
    globals.dt *= 60 # Multiply our delta time by FPS_MAX so we can measure in pixels per second instead of pixels per frame which is frame rate dependant
    #print(globals.dt)
    last_time = time.time()

    # Get events (mouse click, keyboard press)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Cleanup pygame
            sys.exit() # Quit program

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                print(FPS_MAX)
                if FPS_MAX == 60:
                    print("It's 80")
                    FPS_MAX = 30
                elif FPS_MAX == 30:
                    print("It's 30")
                    FPS_MAX = 60


    screen.fill(colours.BLACK)
    level.run()

    pygame.display.update()
    clock.tick(FPS_MAX)
