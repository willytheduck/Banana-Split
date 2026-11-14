import pygame
from settings import *

class Banana:
    def __init__(self,panel,left_key,right_key,color):
        self.panel = panel
        self.left_key = left_key
        self.right_key = right_key
        self.color = color
        self.speed = BANAN_SPEED
        self.rect = pygame.Rect(0,0,BANANA_W, BANANA_H)
        self.rect.centerx = panel.centerx
        self.rect.bottom = panel.bottom - 20
        self.x = float(self.rect.x)

    def update(self,keys,dt):
        direction = 0
        if keys[self.left_key]:
            direction -= 1
        if keys[self.right_key]:
            direction += 1
        self.x += direction * self.speed * dt
        self.rect.x = round(self.x)
        self.rect.clamp_ip(self.panel)
        self.x = float(self.rect.x)

    def draw(self,screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=8)