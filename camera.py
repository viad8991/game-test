import pygame

from const import *


class Camera:
    def __init__(self, width, height):
        super().__init__()
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, player):
        x = -player.rect.centerx + int(SCREEN_WIDTH / 2)
        y = -player.rect.centery + (SCREEN_HEIGHT - int(SCREEN_HEIGHT / 5))

        x = min(0, x)                               # Левая граница
        y = min(0, y)                               # Верхняя граница
        x = max(-(self.width - SCREEN_WIDTH), x)    # Правая граница
        y = max(-(self.height - SCREEN_HEIGHT), y)  # Нижняя граница

        self.camera = pygame.Rect(x, y, self.width, self.height)

        # health_font = pygame.font.Font(None, 36)
        # health_text = health_font.render(f"<3: {player.health}", True, BLACK)
        # health_text_rect = health_text.get_rect()
        # health_text_rect.topleft = (10, 10)
        # self.camera.blit(health_text, health_text_rect)

