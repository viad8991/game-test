from platform_sprite import *


class Level():
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving
            platforms collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

        self.world_shift = 0

    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """
        screen.fill(BLUE)
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right, and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x


class Level_01(Level):
    def __init__(self, player):
        Level.__init__(self, player)
        self.level_limit = -1000

        level = [
            {
                "x": 0,
                "y": SCREEN_HEIGHT - 70,
                "w": 7 * SCREEN_WIDTH,
                "h": SCREEN_HEIGHT,
                "type": None,
            }
        ]

        for platform in level:
            block = Platform(platform.get("w"), platform.get("h"))
            block.rect.x = platform.get("x")
            block.rect.y = platform.get("y")
            block.player = self.player
            self.platform_list.add(block)
