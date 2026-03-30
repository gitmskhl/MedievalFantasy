import utils
import pygame
import pytmx
import player


class Level:
    def __init__(self):
        self.background = utils.loadimg('images/Maps/World.png', 1)
        self.backgroundorig = self.background
        self.scale = 1
        self.xcamera = 0
        self.ycamera = 0 
    def render(self, screen):
        screen.blit(self.background, [-self.xcamera, -self.ycamera])
    def resize_everything(self, sizing):
        if sizing == 1:
            self.scale *= 1.1
            self.background = pygame.transform.scale(self.backgroundorig, [self.backgroundorig.get_width() * self.scale, self.backgroundorig.get_height() * self.scale])
        if sizing == 0:
            self.scale *= 0.9
            self.background = pygame.transform.scale(self.backgroundorig, [self.backgroundorig.get_width() * self.scale, self.backgroundorig.get_height() * self.scale])
    def load(self, warriors):
        data = pytmx.load_pygame('Tiled/World.tmx')
        for x, y, gid in data.get_layer_by_name('Spawners'):
            warrior = player.Warrior(x, y)
            warriors.append(warrior)