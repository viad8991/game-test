import pygame

from const import *


class Camera:
    def __init__(self, width, height, screen):
        super().__init__()
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

        self.screen = screen

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

        # font = pygame.font.Font(None, 36)
        # health_text = font.render(f"Жизни: {player.health}", True, BLACK)
        # health_text_rect = health_text.get_rect()
        # health_text_rect.topright = (SCREEN_WIDTH - 10, 40)
        # self.screen.blit(health_text, health_text_rect)
        # print("health_text_rect", health_text_rect.x, health_text_rect.y)

