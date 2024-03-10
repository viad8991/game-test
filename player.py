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


class PlayerOld(Sprite):
    def __init__(self, main, platforms, bullets):
        super().__init__()
        self.image = pygame.Surface([10, 20])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.up_speed = 15
        self.speed = 5

        self.gravity = 1
        self.vertical_speed = 0

        self.main = main
        self.platforms = platforms
        self.bullets = bullets

        self.direction = "right"

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.direction = "left"
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.direction = "right"
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= self.up_speed
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= self.up_speed

        self.vertical_speed += self.gravity
        self.rect.y += self.vertical_speed

        for platform in self.platforms:
            if pygame.sprite.spritecollide(self, self.platforms, False):
                self.rect.bottom = platform.rect.top
                self.vertical_speed = 0

        # mouse_x, mouse_y = pygame.mouse.get_pos()
        # dx = mouse_x - self.rect.centerx
        # dy = mouse_y - self.rect.centery
        # angle = math.atan2(dy, dx)
        # angle_deg = math.degrees(angle)
        # if angle_deg < 0:
        #     self.direction = "left"
        # else:
        #     self.direction = "right"

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def shoot(self, press):
        bullet = Bullet(self.rect.centerx, self.rect.centery, self.direction)
        self.main.add(bullet)
        self.bullets.add(bullet)
