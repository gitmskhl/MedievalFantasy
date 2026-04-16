import utils
import pytmx

imgtrees = utils.loadimages('images/Terrain/Resources/Wood/Trees/Tree3.png', 1, 8)
trees = []

def loadtrees():
    map = pytmx.load_pygame('Tiled/World.tmx')
    for x, y, gid in map.get_layer_by_name('Tree3'):
        if gid != 0:
            tree = Tree(x * 64, (y - 2) * 64,)
            trees.append(tree)
            
class Tree:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def render(self, screen, xcamera, ycamera, scale):
        screen.blit(imgtrees[0], ((self.x - xcamera) * scale, (self.y - ycamera) * scale))