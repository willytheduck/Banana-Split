import pygame
from settings import *
from player import Banana
from scoop import ScoopField
from bot import Bot
from pyramid import draw_result
from hearts import make_hearts

def banner(screen, surf, center):
    rect = surf.get_rect(center=center)
    pygame.draw.rect(screen,BG,rect.inflate(30,16), border_radius=10)
    screen.blit(surf,rect)

class Game:
    def __init__(self, catcher_img, scoop_imgs, ft, big_ft, diff, vs_bot):
        self.ft= ft
        self.big_ft = big_ft
        self.catcher_img = catcher_img
        self.scoop_imgs = scoop_imgs
        self.heart_full, self.heart_empty = make_hearts(5)
        self.left_panel = pygame.Rect(0,0,WIDTH//2, HEIGHT)
        self.right_panel = pygame.Rect(WIDTH//2,0,WIDTH//2, HEIGHT)
        self.p1 = Banana(self.left_panel, pygame.K_a, pygame.K_d, catcher_img)
        self.p2 = Banana(self.right_panel, pygame.K_LEFT, pygame.K_RIGHT, catcher_img)
        self.field1 = ScoopField(self.left_panel, self.p1, scoop_imgs, diff)
        self.field2 = ScoopField(self.right_panel, self.p2, scoop_imgs, diff)
        self.bot= Bot(self.p2, self.field2, diff) if vs_bot else None

        self.players = [
            (self.left_panel, "P1", self.p1, self.field1),
            (self.right_panel, "BOT" if vs_bot else "P2", self.p2, self.field2),
        ]
    @property
    def over(self):
        return self.field1.done and self.field2.done

    def winner_txt(self):
        a,b = self.field1, self.field2
        n1,n2=self.players[0][1],self.players[1][1]
        if a.score != b.score:
            return f"{n1 if a.score > b.score else n2} WINS! GG"
        if a.complete and b.complete and a.elapsed != b.elapsed:
            return f"{n1 if a.elapsed<b.elapsed else n2} WINS! GG"
        return "IT'S A TIE"

    def update(self, dt,keys):
        if not self.field1.done:
            self.p1.update(keys,dt)
            self.field1.update(dt)
        if not self.field2.done:
            if self.bot:
                self.bot.update(dt)
            else:
                self.p2.update(keys,dt)
            self.field2.update(dt)

    def draw_hud(self,screen,panel,name,field):
        target = field.cfg["target"]
        screen.blit(self.ft.render(f"{name}: {field.score}/{target}", True,TXT_COLOR),(panel.left + 20, 15))
        w = self.heart_full.get_width()
        for i in range(field.cfg["lives"]):
            heart = self.heart_full if i < field.lives else self.heart_empty
            screen.blit(heart, (panel.left+20+i*(w+8),68))
        if field.done:
            txt = "PYRAMID DONE! YIPPEE" if field.complete else "OUT OF LIVES (RIP)"
            surf = self.big_ft.render(txt, True, TXT_COLOR)
            screen.blit(surf, surf.get_rect(center=(panel.centerx, 130)))

    def draw(self,screen):
        screen.fill(BG)
        pygame.draw.rect(screen, PANEL_LEFT, self.left_panel)
        pygame.draw.rect(screen, PANEL_RIGHT, self.right_panel)
        pygame.draw.line(screen, DIV, (WIDTH//2,0), (WIDTH//2,HEIGHT),4)

        for panel, name, banana, field in self.players:
            if field.done:
                draw_result(screen, panel, field.caught, self.scoop_imgs, field.cfg["target"], self.catcher_img)
            else:
                field.draw(screen)
                banana.draw(screen)
            self.draw_hud(screen, panel, name, field)

        if self.over:
            banner(screen, self.big_ft.render(self.winner_txt(), True, TXT_COLOR), (WIDTH//2,40))
            banner(screen, self.ft.render("ENTER: back to menu", True, TXT_COLOR), (WIDTH//2,HEIGHT-35))