import pygame
from pygame.sprite import Sprite

from const import *


class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 20])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2

        self.face_direction = "right"

        self.speed = 5
        self.jump_height = 100
        self.gravity = 0.6
        self.jump_velocity = -12
        self.vertical_speed = 0

        self.on_ground = False

    def update(self, scaffolds):
        keys = pygame.key.get_pressed()

        dx = 0
        dy = 0

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx -= self.speed
            self.face_direction = "left"
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx += self.speed
            self.face_direction = "right"
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and self.on_ground:
            self.vertical_speed = self.jump_velocity
            self.on_ground = False
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy += self.speed

        self.vertical_speed += self.gravity
        dy += self.vertical_speed

        # работа с коллизиями
        new_rect = self.rect.move(dx, dy)
        for scaffold in scaffolds:
            if new_rect.colliderect(scaffold.rect):
                # collision_rect = new_rect.clip(scaffold.rect)
                if self.vertical_speed > 0:
                    self.rect.bottom = scaffold.rect.top
                    self.on_ground = True
                    self.vertical_speed = 0
                elif self.vertical_speed < 0:
                    self.rect.top = scaffold.rect.bottom
                    self.vertical_speed = 0

        self.rect.move_ip(dx, dy)
