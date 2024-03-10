import pygame

from camera import Camera
from const import *
from levels import Level_01
from platform_sprite import Floor
from player_sprite import Player

pygame.init()
pygame.display.set_caption("Game")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

main_group_sprites = pygame.sprite.Group()
platforms_group_sprites = pygame.sprite.Group()
bullets_group_sprites = pygame.sprite.Group()

floor = Floor()
platforms_group_sprites.add(floor)

player = Player(main_group_sprites, platforms_group_sprites, bullets_group_sprites)

main_group_sprites.add(player, floor)

levels = []
levels.append(Level_01(player))

camera = Camera(GAME_WIDTH, GAME_HEIGHT)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_KP5:
                player.shoot(event.type == pygame.KEYDOWN)

    main_group_sprites.update()
    camera.update(player)
    screen.fill(WHITE)

    for entity in main_group_sprites:
        screen.blit(entity.image, camera.apply(entity))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
