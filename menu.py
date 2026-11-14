import pygame
from settings import *

DIFF_NAMES = ["easy", "normal", "hard"]
MODES = ["VS Bot", "2 players"]

class Menu:
    def __init__(self,ft,big_ft):
        self.ft = ft
        self.big_ft = big_ft
        self.row = 0
        self.diff_i = DIFF_NAMES.index(DIFF)
        self.mode_i = 0 if VS_BOT else 1

    @property
    def diff(self):
        return DIFF_NAMES[self.diff_i]

    @property
    def vs_bot(self):
        return self.mode_i == 0

    def change(self, step):
        if self.row == 0:
            self.diff_i = (self.diff_i + step)%len(DIFF_NAMES)
        else:
            self.mode_i = (self.mode_i+step)%len(MODES)

    def handle_evt(self, evt):
        if evt.type != pygame.KEYDOWN:
            return False
        if evt.key in (pygame.K_UP, pygame.K_w):
            self.row = (self.row -1)%2
        elif evt.key in (pygame.K_DOWN, pygame.K_s):
            self.row = (self.row +1)%2
        elif evt.key in (pygame.K_LEFT, pygame.K_a):
            self.change(-1)
        elif evt.key in (pygame.K_RIGHT, pygame.K_d):
            self.change(1)
        elif evt.key in (pygame.K_RETURN, pygame.K_SPACE):
            return True
        return False

    def draw(self, screen):
        screen.fill(BG)
        title = self.big_ft.render("BANANA SPLIT", True, TXT_COLOR)
        screen.blit(title, title.get_rect(center=(WIDTH//2, 150)))

        rows = [f"Difficulty: < {DIFF_NAMES[self.diff_i]} >", f"Mode: < {MODES[self.mode_i]} >"]
        for i, txt in enumerate(rows):
            color = (200,60,90) if i == self.row else TXT_COLOR
            surf = self.ft.render(txt,True,color)
            screen.blit(surf, surf.get_rect(center=(WIDTH//2,320+i*70)))

        hint = self.ft.render("W/S choose   A/D change  ENTER start", True, TXT_COLOR)
        screen.blit(hint, hint.get_rect(center=(WIDTH//2, HEIGHT-80)))
