import pygame

from camera import Camera
from const import *
from enemy import Enemy
from player import Player
from utils import Utils
from scaffold import Scaffold

utils = Utils()

player = Player()
enemy = Enemy(player)
camera = Camera(GAME_WIDTH, GAME_HEIGHT)

skaffolds = [
    # top
    Scaffold(x=0, y=0, width=GAME_WIDTH, height=20),
    # bottom
    Scaffold(0, SCREEN_HEIGHT - 40, GAME_WIDTH, 40),
    # right
    # Scaffold(SCREEN_WIDTH - 20, 0, 20, SCREEN_HEIGHT),
    # left
    Scaffold(0, 0, 20, SCREEN_HEIGHT),
    # shelf
    Scaffold(0, SCREEN_HEIGHT - 150, 500, 20),
]

main_sprites = pygame.sprite.Group()
main_sprites.add(player, enemy, skaffolds)
enemy_sprites = pygame.sprite.Group()
enemy_sprites.add()

paused = False
running = True
while running:
    for event in pygame.event.get():
        Utils.quit(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
            elif event.key == pygame.K_r:
                player.reset_position()
            if event.key == pygame.K_SPACE:
                bullet = player.shot()
                main_sprites.add(bullet)

    if not paused:
        main_sprites.update(skaffolds + [enemy])
        camera.update(player)
        utils.screen.fill(WHITE)

        for sprite in main_sprites:
            utils.screen.blit(sprite.image, camera.apply(sprite))

        utils.update()
