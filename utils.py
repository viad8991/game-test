import sys

from pygame import Surface
from pygame.time import Clock

from const import *

import pygame


class Utils:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Game v0.0.1")

        self.clock: Clock = pygame.time.Clock()
        self.screen: Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # fps and global update screen
    def update(self):
        self.clock.tick(60)
        pygame.display.flip()

    @staticmethod
    def quit(event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
