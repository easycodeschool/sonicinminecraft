from models import Sprite
from global_ import *
import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def add_blocks(blocks, c_height):
    '''Функция получает существующий список блоков и высоту нового столбца.
    Возвращает список блоков с новыми блоками земли и одним блоком травы.'''
    right = blocks[-1].rect.right
    for i in range(c_height - 1):
        blocks.append(Sprite(dirt_img, right, HEIGHT - (i + 1) * 50, 50, 50))
        
    blocks.append(Sprite(grass_img, right, HEIGHT - c_height * 50, 50, 50))

    return blocks


def update_score(font, points):
    # Здесь генерируется текст чёрного цвета
    return font.render(str(points), True, BLACK)