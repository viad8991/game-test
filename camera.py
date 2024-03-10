import pygame

from const import *


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(SCREEN_WIDTH / 2)
        y = -target.rect.centery + int(SCREEN_HEIGHT / 2)

        x = min(0, x)  # Не двигаем камеру вправо, если игрок находится в левой части экрана
        y = min(0, y)  # Не двигаем камеру вниз, если игрок находится в верхней части экрана
        x = max(-(self.width - SCREEN_WIDTH), x)  # Не двигаем камеру влево за границы игрового мира
        y = max(-(self.height - SCREEN_HEIGHT), y)  # Не двигаем камеру вверх за границы игрового мира

        self.camera = pygame.Rect(x, y, self.width, self.height)
