import animation
import pygame
import utils

class Warrior:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = 'idle'
        self.select = False
        self.targetx = 100
        self.targety = 100
        self.mustmove = False
        self.selectimg = utils.loadimg('images/UI Elements/UI Elements/Cursors/Cursor_04.png', 1)
        self.anims:dict[str, animation.Animation] = {}
        self.anims['attack1'] = animation.Animation('images/Units/Blue Units/Warrior/Warrior_Attack1.png', 1, 4, 6, True)
        self.anims['idle'] = animation.Animation('images/Units/Blue Units/Warrior/Warrior_Idle.png', 1, 8, 6, True)
        self.anims['run'] = animation.Animation('images/Units/Blue Units/Warrior/Warrior_Run.png', 1, 6, 6, True)
    def render(self, screen, xcamera, ycamera, scale=1):
        screen_x = (self.x - xcamera) * scale
        screen_y = (self.y - ycamera) * scale
        self.hitbox:pygame.Rect = self.anims[self.state].render(screen, screen_x, screen_y, 'right', scale)
        hitbox_shrink = round(90 * scale)
        self.hitbox = self.hitbox.inflate(-hitbox_shrink, -hitbox_shrink)
        if self.select == True:
            screen.blit(self.selectimg, [self.hitbox.centerx - self.selectimg.get_width() / 2, self.hitbox.centery - self.selectimg.get_height() / 2])
    def update(self, click):
        self.anims[self.state].update()
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if click == True:
                if self.select == True:
                    self.select = False
                else:
                    self.select = True
    def moving(self):
        size = self.anims[self.state].what_size_of_img()
        if self.targetx > self.x + size[0] / 2:
            self.x += 10
        else:
            self.x -= 10
        if self.targety > self.y + size[1] / 2:
            self.y += 10
        else:
            self.y -= 10
        if abs(self.targetx - self.x - size[0] / 2) < 10 and abs(self.targety - self.y - size[1] / 2) < 10:
            self.mustmove = False
    def gethitbox(self):
        return pygame.rect.Rect([self.x, self.y], self.anims[self.state].what_size_of_img())
        