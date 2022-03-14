import pygame, engine, settings, globals

colours = engine.Colours()

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.speed = settings.player_speed
        self.gravity = 0.8
        self.jump_speed = -16
        self.image = pygame.Surface((32, 64))
        self.image.fill(colours.RED)
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0, 0)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            #print(globals.dt)
            self.direction.x = 1 * globals.dt
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            #print(globals.dt)
            self.direction.x = -1 * globals.dt
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:
            self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity * globals.dt
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.apply_gravity()
