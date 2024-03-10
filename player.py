import pygame
from pygame.sprite import Sprite

from bullet_sprite import Bullet
from const import *
from datetime import datetime


class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 20])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2

        self.speed = 5
        self.up_speed = 15

        self.face_direction = "right"

        self.gravity = 0.35
        self.vertical_speed = 0
        self.vertical_speed_max = 5

        self.jump = False

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
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and not self.jump:
            self.jump = True
            dy -= self.up_speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy += self.speed

        self.vertical_speed = self.vertical_speed + self.gravity
        if self.vertical_speed > self.vertical_speed_max:
            self.vertical_speed = self.vertical_speed_max
        dy += self.vertical_speed

        # работа с коллизиями
        new_rect = self.rect.move(dx, dy)
        for scaffold in scaffolds:
            if new_rect.colliderect(scaffold.rect):
                collision_rect = new_rect.clip(scaffold.rect)
                if collision_rect.width < collision_rect.height:
                    dx = 0
                else:
                    self.jump = False
                    self.vertical_speed = 0
                    dy = 0

        self.rect.move_ip(dx, dy)
