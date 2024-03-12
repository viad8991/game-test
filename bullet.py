import pygame
from pygame.sprite import Sprite

from const import *


class Bullet(Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface((4, 4))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 10

        self.direction = direction

    def update(self, scaffolds):
        for scaffold in scaffolds:
            if self.rect.colliderect(scaffold.rect):
                self.kill()

        # TODO 1 left more right
        if self.direction == "right":
            self.rect.x += self.speed
            if self.rect.right == 1000:
                self.kill()
        else:
            self.rect.x -= self.speed
            if abs(self.rect.left) == 1000:
                self.kill()

