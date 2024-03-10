import pygame
from const import *
from player import Player
from utils import Utils
from scaffold import Scaffold

utils = Utils()

player = Player()

skaffolds = [
    # top
    Scaffold(x=0, y=0, width=SCREEN_WIDTH, height=20),
    # bottom
    Scaffold(0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40),
    # right
    Scaffold(SCREEN_WIDTH - 20, 0, 20, SCREEN_HEIGHT),
    # left
    Scaffold(0, 0, 20, SCREEN_HEIGHT),
    # shelf
    Scaffold(0, SCREEN_HEIGHT - 150, 500, 20),
]

main_sprites = pygame.sprite.Group()
main_sprites.add(player, skaffolds)

paused = False
running = True
while running:
    for event in pygame.event.get():
        Utils.quit(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused

    if not paused:
        main_sprites.update(skaffolds)
        utils.screen.fill(WHITE)
        main_sprites.draw(utils.screen)
        utils.update()
