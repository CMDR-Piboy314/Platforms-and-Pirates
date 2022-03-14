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

        elif player_x >= settings.WINDOW_SIZE[0] - (settings.WINDOW_SIZE[0] / 4) and direction_x > 0:
            print(player_x)
            if player_x > settings.WINDOW_SIZE[0] - (settings.WINDOW_SIZE[0] / 4):
                print("Setting it back")
                player_x = settings.WINDOW_SIZE[0] - (settings.WINDOW_SIZE[0] / 4)
            self.scroll[0] = -settings.player_speed
            player.speed = 0

        else:
            self.scroll[0] = 0
            player.speed = settings.player_speed

    def horiz_movement_coll(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right

                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vert_movement_coll(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.top = sprite.rect.bottom

                elif player.direction.y < 0:
                    player.rect.bottom = sprite.rect.top

    def run(self):
        # Tiles stuff
        self.tiles.update(self.scroll)
        self.scroll_x()
        self.tiles.draw(self.display_surface)

        # Player stuff
        self.player.update()
        self.horiz_movement_coll()
        self.vert_movement_coll()
        self.player.draw(self.display_surface)
