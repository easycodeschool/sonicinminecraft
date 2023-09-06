import pygame
import sys
import random
from vars import *

# В этой строке хранится список всех доступных фонов
backgrounds = ['img/backgrounds/bg1.png', 'img/backgrounds/bg2.png', 'img/backgrounds/bg3.png', 'img/backgrounds/bg4.png']
background = 'img/backgrounds/bg1.png'
while True:
    # Эта команда рисует фон
    draw_background(background)
    if game_state == 0:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if button_pressed(e.pos):
                    game_state = 1

        sc.blit(start_bg, (0, 0))
        sc.blit(button_img, (button.x, button.y))
    elif game_state == 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    if player.can_jump:
                        player.jumping = 1
                        player.can_jump = False

        draw_everything()

        if player.rect.right < 0:
            game_state = 2

    elif game_state == 2:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    generate_initial()
                    game_state = 1
                    

    pygame.display.update()
    clock.tick(80)
