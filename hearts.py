import pygame
PATTERN = [
    ".XX.XX.",
    "XXXXXXX",
    "XXXXXXX",
    ".XXXXX.",
    "..XXX..",
    "...X...",
]
FULL = (224,48,72)
LIGHT = (255,200,205)
EMPTY = (200,190,200)

def make_hearts(px=5):
    full = pygame.Surface((7,6),pygame.SRCALPHA)
    empty = pygame.Surface((7,6),pygame.SRCALPHA)
    for y,row in enumerate(PATTERN):
        for x, ch in enumerate(row):
            if ch == "X":
                full.set_at((x,y),FULL)
                empty.set_at((x,y), EMPTY)
    full.set_at((1,1),LIGHT)
    size = (7*px,6*px)
    return pygame.transform.scale(full,size),pygame.transform.scale(empty,size)