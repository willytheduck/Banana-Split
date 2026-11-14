import pygame
from settings import *
from player import Banana

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Banana Split")
clock = pygame.time.Clock()

left_panel = pygame.Rect(0,0,WIDTH//2, HEIGHT)
right_panel = pygame.Rect(WIDTH//2,0,WIDTH//2,HEIGHT)

p1 = Banana(left_panel,pygame.K_a, pygame.K_d, P1_COLOR)
p2 = Banana(right_panel, pygame.K_LEFT, pygame.K_RIGHT, P2_COLOR)

running = True
while running:
    dt = clock.tick(FPS)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    p1.update(keys,dt)
    p2.update(keys,dt)
    screen.fill(BG)
    pygame.draw.rect(screen, PANEL_LEFT, left_panel)
    pygame.draw.rect(screen, PANEL_RIGHT, right_panel)
    pygame.draw.line(screen, DIV, (WIDTH//2,0), (WIDTH//2,HEIGHT),4)
    p1.draw(screen)
    p2.draw(screen)
    pygame.display.flip()

pygame.quit()