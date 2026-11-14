import random
from settings import *

class Bot:
    def __init__(self, banana, field, diff):
        self.banana = banana
        self.field = field
        self.cfg = BOT[diff]
        self.banana.speed = BANANA_SPEED * self.cfg["speed"]
        self.timer = 0.0
        self.target_x = banana.rect.centerx

    def choose_target(self):
        best = None
        for scoop in self.field.scoops:
            if self.cfg["avoid_gross"] and scoop.flavour == "gross":
                continue
            if scoop.rect.bottom > self.banana.rect.top:
                continue
            if best is None or scoop.rect.centery > best.rect.centery:
                best = scoop
        if best is None:
            self.target_x = self.banana.panel.centerx
        else:
            err = self.cfg["error"]
            self.target_x = best.rect.centerx + random.randint(-err,err)

    def update(self,dt):
        self.timer += dt
        if self.timer >= self.cfg["reaction"]:
            self.timer = 0.0
            self.choose_target()

        diff = self.target_x - self.banana.rect.centerx
        step = self.banana.speed * dt
        direction = max(-1.0,min(1.0,diff/step)) if step else 0
        self.banana.move(direction,dt)