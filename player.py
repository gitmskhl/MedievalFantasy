import animation

class Warrior:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = 'attack1'
        self.anims:dict[str, animation.Animation] = {}
        self.anims['attack1'] = animation.Animation('images/Units/Blue Units/Warrior/Warrior_Attack1.png', 1, 4, 6, True)
    def render(self, screen):
        self.anims[self.state].render(screen, self.x, self.y, 'right')
    def update(self):
        self.anims[self.state].update()
