import pygame
from pygame.sprite import Sprite

from bullet import Bullet
from const import *
from enemy import Enemy
from scaffold import Scaffold


class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 20])
        self.image.fill(GREEN)

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

        self.health = 100

    def update(self, objects):
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
        self.collide(dx, 0, objects)

        self.rect.y += dy
        self.collide(0, dy, objects)

    def collide(self, dx, dy, objects):
        on_ground_temp = False
        for object in objects:
            if self.rect.colliderect(object.rect):
                if isinstance(object, Enemy):
                    self.health -= 5
                elif isinstance(object, Scaffold):
                    if dy > 0:
                        self.rect.bottom = object.rect.top
                        on_ground_temp = True
                        self.vertical_speed = 0
                    if dy < 0:
                        self.rect.top = object.rect.bottom
                        self.vertical_speed = 0
                    if dx > 0:
                        self.rect.right = object.rect.left
                    if dx < 0:
                        self.rect.left = object.rect.right
        self.on_ground = on_ground_temp

    def shot(self):
        return Bullet(self.rect.centerx, self.rect.centery, self.face_direction)

    def reset_position(self):
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
