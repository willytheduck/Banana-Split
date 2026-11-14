import pygame
from settings import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Banana Split")
clock = pygame.time.Clock()

left_panel = pygame.Rect(0,0,WIDTH//2, HEIGHT)
right_panel = pygame.Rect(WIDTH//2, 0, WIDTH//2, HEIGHT)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BG)
    pygame.draw.rect(screen, PANEL_LEFT, left_panel)
    pygame.draw.rect(screen, PANEL_RIGHT, right_panel)
    pygame.draw.line(screen, DIV, (WIDTH//2,0), (WIDTH//2, HEIGHT),4)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()