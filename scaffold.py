import pygame
from const import *
from player import Player


class Scaffold(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def check_collision(self, player: Player):
        return self.rect.collidedict(player)
