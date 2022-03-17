# Programmed by Piboy314 for Constellation Games 🍝
import pygame, sys, engine, time, overworld, game_data

from tiles import Tile
from level import Level
from settings import *

# Define Constants
FPS_MAX = 60

# Create pygame stuff
pygame.init() # Initialize pygame
screen = pygame.display.set_mode(WINDOW_SIZE) # Create a window with the size being WINDOW_SIZE
pygame.display.set_caption("Platforms and Pirates")
pygame.mixer.music.load("res/wav/Mario.wav")
pygame.mixer.music.set_volume(0.7)

# Create classes
class Game:
    def __init__(self):
        self.max_level = 3
        self.overworld = overworld.Overworld(0, self.max_level, screen)

    def run(self):
        #pass
        self.overworld.run()

# Create instances
clock = pygame.time.Clock() # Create a clock for framerate capping and ticks
level = Level(game_data.level_0_data, screen)
colours = engine.Colours()
game = Game()

pygame.mixer.music.play(-1)

# Game loop
while True:
    # Get events (mouse click, keyboard press)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Cleanup pygame
            sys.exit() # Quit program


    screen.fill(colours.BLACK)
    level.run()
    game.run()

    pygame.display.update()
    clock.tick(FPS_MAX)
