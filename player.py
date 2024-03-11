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
        self.max_vertical_speed = 10

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
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.on_ground:
            dy += self.speed

        if not self.on_ground:
            self.vertical_speed += self.gravity
            dy += min(max(self.vertical_speed, -self.max_vertical_speed), self.max_vertical_speed)
        else:
            self.vertical_speed = 0

        self.rect.x += dx
        self.collide(dx, 0, scaffolds)

        self.rect.y += dy
        self.collide(0, dy, scaffolds)

    def collide(self, dx, dy, scaffolds):
        on_ground_temp = False
        for scaffold in scaffolds:
            if self.rect.colliderect(scaffold.rect):
                if dy > 0:
                    self.rect.bottom = scaffold.rect.top
                    on_ground_temp = True
                    self.vertical_speed = 0
                if dy < 0:
                    self.rect.top = scaffold.rect.bottom
                    self.vertical_speed = 0
                if dx > 0:
                    self.rect.right = scaffold.rect.left
                if dx < 0:
                    self.rect.left = scaffold.rect.right
        self.on_ground = on_ground_temp

    def reset_position(self):
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
