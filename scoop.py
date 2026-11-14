import random
import pygame
from settings import *

class Scoop:
    def __init__(self,x,y,flavour):
        self.y = float(y)
        self.flavour = flavour
        self.rect = pygame.Rect(0,0,SCOOP_RAD*2, SCOOP_RAD*2)
        self.rect.center = (x, round(self.y))

    def update(self, dt):
        self.y += SCOOP_SPEED*dt
        self.rect.centery = round(self.y)

    def draw(self,screen):
        pygame.draw.circle(screen, FLAVOURS[self.flavour], self.rect.center,SCOOP_RAD)
        pygame.draw.circle(screen, (60,40,40), self.rect.center, SCOOP_RAD,2)

class ScoopField:
    #one/player: spawn, move n catch scoop in 1 panel
    def __init__(self,panel, banana):
        self.panel = panel
        self.banana = banana
        self.scoops = []
        self.caught = []
        self.timer = 0.0
    @property
    def score(self):
        return len(self.caught)

    def spwn(self):
        x = random.randint(self.panel.left + SCOOP_RAD, self.panel.right - SCOOP_RAD)
        flavour = random.choice(NORMAL_FLAVOURS)
        self.scoops.append(Scoop(x, self.panel.top - SCOOP_RAD, flavour))

    def update(self,dt):
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
    def draw(self,screen):
        for scoop in self.scoops:
            scoop.draw(screen)