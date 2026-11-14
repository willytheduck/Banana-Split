import pygame
from settings import SCALE

def load(path):
    img = pygame.image.load(path).convert_alpha()
    img = img.subsurface(img.get_bounding_rect()).copy() #trimmin the empty space
    w,h = img.get_size()
    return pygame.transform.scale(img, (w*SCALE, h*SCALE)) #crisp, no blur