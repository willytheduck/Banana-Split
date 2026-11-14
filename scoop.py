import random
import pygame
from settings import *


class Scoop:
    def __init__(self, x, y, flavour, img):
        self.flavour = flavour
        self.img = img
        self.y = float(y)
        self.rect = img.get_rect(center=(x, round(self.y)))

    def update(self, dt):
        self.y += SCOOP_SPEED * dt
        self.rect.centery = round(self.y)

    def draw(self, screen):
        screen.blit(self.img, self.rect)


class ScoopField:
    # 1/player: spawn, move n catch scoop in 1 panel
    def __init__(self, panel, banana, imgs):
        self.panel = panel
        self.banana = banana
        self.imgs = imgs  # flavour name -> surface
        self.scoops = []
        self.caught = []
        self.timer = 0.0

    @property
    def score(self):
        return len(self.caught)

    def spwn(self):
        flavour = random.choice(NORMAL_FLAVOURS)
        img = self.imgs[flavour]
        half = img.get_width() // 2
        x = random.randint(self.panel.left + half, self.panel.right - half)
        self.scoops.append(Scoop(x, self.panel.top - img.get_height(), flavour, img))

    def update(self, dt):
        self.timer += dt
        if self.timer >= SPWN_INTER:
            self.timer = 0.0
            self.spwn()
        for scoop in self.scoops[:]:
            scoop.update(dt)
            if scoop.rect.colliderect(self.banana.catch_rect):
                self.caught.append(scoop.flavour)
                self.scoops.remove(scoop)
            elif scoop.rect.top > self.panel.bottom:
                self.scoops.remove(scoop)

    def draw(self, screen):
        for scoop in self.scoops:
            scoop.draw(screen)
