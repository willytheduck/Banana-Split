import pygame
from settings import *
import assets
from player import Banana
from scoop import ScoopField

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Banana Split")
clock = pygame.time.Clock()
ft= pygame.font.Font(None,48)
big_ft = pygame.font.Font(FONT_FILE, 56)

catcher_img = assets.load(CATCHER_FILE)
scoop_imgs = {name: assets.load(path) for name, path in FLAVOUR_FILES.items()}

left_panel = pygame.Rect(0,0,WIDTH//2, HEIGHT)
right_panel = pygame.Rect(WIDTH//2,0,WIDTH//2,HEIGHT)

p1 = Banana(left_panel, pygame.K_a, pygame.K_d, catcher_img)
p2 = Banana(right_panel, pygame.K_LEFT, pygame.K_RIGHT, catcher_img)
field1 = ScoopField(left_panel,p1,scoop_imgs, DIFF)
field2 = ScoopField(right_panel,p2,scoop_imgs, DIFF)
players = [(left_panel, "P1", p1, field1), (right_panel, "P2", p2, field2)]

def draw_hud(panel, name, field):
    target = field.cfg["target"]
    screen.blit(ft.render(f"{name}: {field.score}/{target}", True, TXT_COLOR), (panel.left + 20,15))
    screen.blit(ft.render(f"Lives: {field.lives}", True, TXT_COLOR), (panel.left + 20, 60))
    if field.done:
        txt = "PYRAMIND DONE! YIPPEE" if field.complete else "OUT OF LIVES (RIP)"
        surf = big_ft.render(txt,True,TXT_COLOR)
        screen.blit(surf, surf.get_rect(center=panel.center))

running = True
while running:
    dt = clock.tick(FPS)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    for panel, name, banana, field in players:
        if not field.done:
            banana.update(keys, dt)
            field.update(dt)

    screen.fill(BG)
    pygame.draw.rect(screen, PANEL_LEFT, left_panel)
    pygame.draw.rect(screen, PANEL_RIGHT, right_panel)
    pygame.draw.line(screen, DIV, (WIDTH//2,0), (WIDTH//2,HEIGHT), 4)

    for panel, name, banana, field in players:
        field.draw(screen)
        banana.draw(screen)
        draw_hud(panel,name,field)
    pygame.display.flip()
pygame.quit()