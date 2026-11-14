import random
import pygame
from settings import *


class Scoop:
    def __init__(self,x,y,flavour,img,speed):
        self.flavour = flavour
        self.img = img
        self.speed = speed
        self.y = float(y)
        self.rect = img.get_rect(center=(x,round(self.y)))

    def update(self,dt):
        self.y += self.speed*dt
        self.rect.centery = round(self.y)

    def draw(self,screen):
        screen.blit(self.img, self.rect)

class ScoopField:
    # 1/player: spawn, move n catch scoop in 1 panel
    def __init__(self,panel,banana,imgs,diff):
        self.panel = panel
        self.banana = banana
        self.imgs = imgs
        self.cfg = DIFFS[diff]
        self.lives = self.cfg["lives"]
        self.scoops = []
        self.caught = []
        self.timer = 0.0
        self.done = False
        self.complete = False

    @property
    def score(self):
        return len(self.caught)

    def spwn(self):
        if random.random()<self.cfg["gross"]:
            flavour = "gross"
        else:
            flavour = random.choice(NORMAL_FLAVOURS)
        img = self.imgs[flavour]
        half = img.get_width()//2
        x = random.randint(self.panel.left + half, self.panel.right - half)
        y = self.panel.top - img.get_height()
        self.scoops.append(Scoop(x,y,flavour,img,self.cfg["speed"]))

    def update(self,dt):
        if self.done:
            return
        self.timer += dt
        if self.timer >= self.cfg["interval"]:
            self.timer = 0.0
            self.spwn()

        for scoop in self.scoops[:]:
            scoop.update(dt)
            if scoop.rect.colliderect(self.banana.catch_rect):
                self.scoops.remove(scoop)
                if scoop.flavour == "gross":
                    self.lives -= 1
                else:
                    self.caught.append(scoop.flavour)
            elif scoop.rect.top > self.panel.bottom:
                self.scoops.remove(scoop)
                if scoop.flavour != "gross":
                    self.lives -= 1
        if self.lives <= 0:
            self.lives = 0
            self.done = True
            self.scoops.clear()
        elif self.score >= self.cfg["target"]:
            self.done = True
            self.complete = True
            self.scoops.clear()
    def draw (self,screen):
        for scoop in self.scoops:
            scoop.draw(screen)