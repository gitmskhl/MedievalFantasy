import pygame

def loadimg(path, scale):
    img = pygame.image.load(path)
    img = pygame.transform.scale(img, [img.get_width() * scale, img.get_height() * scale])
    return img
def loadimages(path, scale, countimg):
    spritesheet = loadimg(path, scale)
    images = []
    w = spritesheet.get_width() / countimg
    for i in range(0, countimg):
        image = spritesheet.subsurface(i * w, 0, w, spritesheet.get_height())
        images.append(image)
    return images
    

    