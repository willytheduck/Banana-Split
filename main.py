import pygame
from settings import *
import assets
from menu import Menu
from game import Game

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Banana Split")
clock = pygame.time.Clock()
ft= pygame.font.Font(None,48)
big_ft = pygame.font.Font(FONT_FILE, 56)

catcher_img = assets.load(CATCHER_FILE)
scoop_imgs = {name: assets.load(path) for name, path in FLAVOUR_FILES.items()}

menu = Menu(ft,big_ft)
game = None

running = True
while running:
    dt = clock.tick(FPS)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif game is None:
            if menu.handle_evt(event):
                game = Game(catcher_img, scoop_imgs,ft,big_ft,menu.diff, menu.vs_bot)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or (event.key == pygame.K_RETURN and game.over):
                game = None
    if game is None:
        menu.draw(screen)
    else:
        game.update(dt,pygame.key.get_pressed())
        game.draw(screen)

    pygame.display.flip()
pygame.quit()