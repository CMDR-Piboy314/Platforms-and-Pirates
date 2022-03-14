import pygame, player, settings, globals

from tiles import Tile
from globals import *

class Level():
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.tile_size = settings.tile_size
        self.setup_level(level_data)
        self.scroll = [0, 0]

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * self.tile_size
                y = row_index * self.tile_size

                if cell == 'X':
                    tile = Tile((x, y), self.tile_size)
                    self.tiles.add(tile)

                elif cell == 'P':
                    player_sprite = player.Player((x, y))
                    self.player.add(player_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < (settings.WINDOW_SIZE[0] / 4) and direction_x < 0:
            self.scroll[0] = settings.player_speed
            player.speed = 0

        elif player_x > (settings.WINDOW_SIZE[0] - (settings.WINDOW_SIZE[0] / 4)) and direction_x > 0:
            self.scroll[0] = -settings.player_speed
            player.speed = 0

        else:
            self.scroll[0] = 0
            player.speed = settings.player_speed

    def run(self):
        self.tiles.update(self.scroll)
        self.tiles.draw(self.display_surface)

        self.player.update()
        self.player.draw(self.display_surface)
        self.scroll_x()
