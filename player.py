import pygame
from settings import *


class Banana:
    def __init__(self, panel, left_key, right_key, img):
        self.panel = panel
        self.left_key = left_key
        self.right_key = right_key
        self.img = img
        self.speed = BANAN_SPEED
        self.rect = img.get_rect()
        self.rect.centerx = panel.centerx
        self.rect.bottom = panel.bottom - 20
        self.x = float(self.rect.x)

    def update(self, keys, dt):
        direction = 0
        if keys[self.left_key]:
            direction -= 1
        if keys[self.right_key]:
            direction += 1
        self.x += direction * self.speed * dt
        self.rect.x = round(self.x)
        self.rect.clamp_ip(self.panel)
        self.x = float(self.rect.x)

    @property
    def catch_rect(self):
        inset = round(self.rect.w * CATCH_INSET)
        return pygame.Rect(
            self.rect.x + inset,
            self.rect.y,
            self.rect.w - 2 * inset,
            round(self.rect.h * CATCH_HEIGHT),
        )

    def draw(self, screen):
        screen.blit(self.img, self.rect)
        if DEBUG:
            pygame.draw.rect(screen, (255, 0, 0), self.catch_rect, 1)
