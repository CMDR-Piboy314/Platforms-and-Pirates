import pygame, engine, globals

colours = engine.Colours()

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill(colours.GREY)
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, scroll):
        self.rect.x += scroll[0]
