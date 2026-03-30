import pygame
import utils


class Animation:
    def __init__(self, path, scale, countimg, period, repeat):
        self.images = utils.loadimages(path, scale, countimg)
        self.index = 0
        self.period = period
        self.startperiod = period
        self.repeat = repeat
    def render(self, screen, x, y, dir):
        if dir == 'right':
            screen.blit(self.images[self.index], [x, y])
        else:
            i = pygame.transform.flip(self.images[self.index], True, False)
            screen.blit(i, [x, y])
    def update(self):
        self.period -= 1
        if self.period == 0:
            self.index += 1
            self.period = self.startperiod
        if self.index == len(self.images):
            if self.repeat == True:
                self.index = 0 
            else:
                self.index = len(self.images) - 1
    def reset(self):
        self.index = 0
        self.period = self.startperiod
        
        