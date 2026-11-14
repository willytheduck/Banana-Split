import pygame
from settings import *

SLOT = (170,150,160)
TOP = 180
BOTTOM = HEIGHT - 70
DISH_OVERLAP = 0.3

_cache = {}

def _scaled(surface, key, size):
    if key not in _cache:
        _cache[key] = pygame.transform.scale(surface,size)
    return _cache[key]

def rows_for(target):
    n = 1
    while n * (n+1)//2 < target:
        n+= 1
    return n

def layout(rows,panel_w,dish_w, dish_h):
    cell, f = 4,1
    for cell in range(28,3,-1):
        f = max(1,round((rows*cell + 80)/dish_w))
        total = rows * cell + dish_h * f *(1-DISH_OVERLAP)
        if total <= BOTTOM - TOP and dish_w * f <= panel_w - 20:
            break
    return cell, f

def draw_result(screen,panel,caught,imgs,target,dish_img):
    rows = rows_for(target)
    dw,dh=dish_img.get_size()
    cell,f = layout(rows,panel.w,dw,dh)
    dish= _scaled(dish_img, ("dish", f), (dw*f,dh*f))
    dish_rect = dish.get_rect(midbottom=(panel.centerx, BOTTOM))
    base_y = dish_rect.top + round(dish_rect.h *DISH_OVERLAP)
    cx = panel.centerx
    k=0
    for r in range(rows):
        n = rows - r
        y = base_y - (r+1)*cell
        x0=cx-n*cell//2
        for i in range(n):
            if k>=target:
                break
            rect = pygame.Rect(x0+i *cell, y, cell, cell)
            if k < len(caught):
                flavour = caught[k]
                img = _scaled(imgs[flavour], (flavour,cell), (cell,cell))
                screen.blit(img,rect)
            else:
                pygame.draw.rect(screen,SLOT,rect,1)
            k += 1
    screen.blit(dish, dish_rect)