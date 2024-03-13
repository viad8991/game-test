import random

import pygame

from bullet import Bullet
from const import *
from scaffold import Scaffold


class Enemy(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.Surface([20, 40])
        self.image.fill(RED)

        self.rect = self.image.get_rect()

        self.face_direction = "right"

        self.speed = 3

        self.gravity = 0.6
        self.jump_velocity = -12
        self.vertical_speed = 0
        self.max_vertical_speed = 10

        self.on_ground = False

        self.health = 100

        # TODO temp
        self.player = player
        if random.choice(["left", "right"]) == "left":
            self.rect.x = player.rect.x - 300
        else:
            self.rect.x = player.rect.x + 300
        self.rect.y = player.rect.y

    def update(self, objects):
        if self.health <= 0:
            self.kill()

        dx = 0
        dy = 0

        if self.rect.x < self.player.rect.x:
            dx += self.speed
        else:
            dx -= self.speed

        if not self.on_ground:
            self.vertical_speed += self.gravity
            dy += min(max(self.vertical_speed, -self.max_vertical_speed), self.max_vertical_speed)
        else:
            self.vertical_speed = 0

        self.rect.x += dx
        self.collide(dx, 0, objects)

        self.rect.y += dy
        self.collide(0, dy, objects)

    def collide(self, dx, dy, objects):
        on_ground_temp = False
        for object in objects:
            if self.rect.colliderect(object.rect):
                if isinstance(object, Scaffold):
                    scaffold = object
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
                elif isinstance(object, Bullet):
                    print("object is bullet", "enemy health", self.health, type(object), len(objects), objects)
                    bullet = object
                    self.health -= bullet.damage

        self.on_ground = on_ground_temp
