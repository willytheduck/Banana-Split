import pygame
from settings import *
import assets
from player import Banana
from scoop import ScoopField

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Banana Split")
clock = pygame.time.Clock()
font= pygame.font.Font(None,48)

catcher_img = assets.load(CATCHER_FILE)
scoop_imgs = {name: assets.load(path) for name, path in FLAVOUR_FILES.items()}

left_panel = pygame.Rect(0,0,WIDTH//2, HEIGHT)
right_panel = pygame.Rect(WIDTH//2,0,WIDTH//2,HEIGHT)

p1 = Banana(left_panel, pygame.K_a, pygame.K_d, catcher_img)
p2 = Banana(right_panel, pygame.K_LEFT, pygame.K_RIGHT, catcher_img)
field1 = ScoopField(left_panel,p1,scoop_imgs)
field2 = ScoopField(right_panel,p2,scoop_imgs)

running = True
while running:
    dt = clock.tick(FPS)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    p1.update(keys, dt)
    p2.update(keys, dt)
    field1.update(dt)
    field2.update(dt)

    screen.fill(BG)
    pygame.draw.rect(screen,PANEL_LEFT,left_panel)
    pygame.draw.rect(screen, PANEL_RIGHT, right_panel)
    pygame.draw.line(screen, DIV, (WIDTH//2,0), (WIDTH//2, HEIGHT),4)

    field1.draw(screen)
    field2.draw(screen)
    p1.draw(screen)
    p2.draw(screen)

    screen.blit(font.render(f"P1: {field1.score}", True, TXT_COLOR), (20,15))
    screen.blit(font.render(f"P2: {field2.score}", True, TXT_COLOR), (WIDTH//2+20, 15))
    pygame.display.flip()
pygame.quit()