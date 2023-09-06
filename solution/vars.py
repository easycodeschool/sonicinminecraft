import pygame
import random
from global_ import levels


pygame.init()

from models import *
from functions import *

def generate(isRemove):
    # levels[-1] = 1
    global blocks
    global levels
    c_height = random.choice([max(levels[-1] - 1, 1), max(levels[-1] - 1, 1), levels[-1], levels[-1], levels[-1], min(levels[-1] + 1, 5), min(levels[-1] + 1, 5),  min(levels[-1] + 1, 5), min(levels[-1] + 2, 5)]) # 1, 2
    if levels[-1] < levels[-2] or levels[-1] - levels[-2] == 2:
        c_height = random.choice([max(levels[-1] - 1, 1), max(levels[-1] - 1, 1), levels[-1], levels[-1], levels[-1]]) # 1, 2
    right = blocks[-1].rect.right
    blocks = add_blocks(blocks, c_height)
    levels.append(c_height)
    if player.can_remove:
        levels.pop(0)

    isCoin = random.randint(1, 2)
    if isCoin == 1:
        isDown = random.randint(1, 2)
        coin_height = HEIGHT - c_height * 50 - 40
        if isDown == 2:
            coin_height -= 80
        coin = Sprite(coin1_img, right + 10, coin_height, 30, 30, anim_timing=15, images=[coin1_img, coin2_img, coin3_img, coin4_img])
        coins.append(coin)

    coord = blocks[0].rect.x
    while blocks[0].rect.x == coord:
        blocks.pop(0)

def collision():
    global coin_text
    for coin in coins:
        if player.rect.colliderect(coin.rect):
            coins.remove(coin)
            player.points += 1
            coin_text = update_score(font, player.points)


player = Player(sonic_default_img, 250, 301, 50, 54, 1, [sonic1_img, sonic2_img, sonic3_img, sonic4_img, sonic5_img, sonic6_img, sonic7_img, sonic8_img, sonic9_img, sonic10_img])
blocks = []
coins = []
for i in range(4):
    coin = Sprite(coin1_img, 310 + i * 50, 310, 30, 30, anim_timing=15, images=[coin1_img, coin2_img, coin3_img, coin4_img])
    coins.append(coin)

for i in range(17):
    block = Sprite(grass_img, i * 50, 350, 50, 50)
    blocks.append(block)


coin_score = Sprite(coin1_img, 10, 10, 30, 30, anim_timing=15, images=[coin1_img, coin2_img, coin3_img, coin4_img])
font = pygame.font.Font('EpilepsySansBold.ttf', 30)
coin_text = font.render(str(player.points), True, BLACK)
number_to_file = {
    1: dirt_bg_img,
    2: grass_bg_img,
    3: tree_bg_img,
    4: leaves_bg_img,
    5: wood_bg_img,
    6: coal_bg_img,
    7: diamond_bg_img,
    8: emerald_bg_img,
    9: gold_bg_img,
    10: iron_bg_img,
    11: lapis_bg_img,
    12: redstone_bg_img
}
file = open('field.txt', 'r')
block_numbers = file.read().split('\n')
rows = 8
columns = len(block_numbers[0])
background = []
for i in range(rows):
    for j in range(columns):
        number = int(block_numbers[i][j])
        if number > 0:
            block = Sprite(number_to_file[number], j * 50, i * 50, 50, 50)
            block.x_coord = j * 50
            background.append(block)

iterations = 0
seconds = 0
game_state = 0


def generate_initial():
    global blocks, coins, coin_text, background, iterations, seconds, game_state, levels
    player.rect.x = 250
    player.rect.y = 301
    player.points = 0
    player.offset = 0
    player.current_gravity = 0.25
    player.current_dy = 8
    player.jumping = 0
    player.can_jump = True
    player.can_remove = True
    player.moved = 0
    blocks = []
    coins = []
    for i in range(4):
        coin = Sprite(coin1_img, 310 + i * 50, 310, 30, 30, anim_timing=15, images=[coin1_img, coin2_img, coin3_img, coin4_img])
        coins.append(coin)

    for i in range(17):
        block = Sprite(grass_img, i * 50, 350, 50, 50)
        blocks.append(block)


    coin_text = font.render(str(player.points), True, BLACK)
    background = []
    for i in range(rows):
        for j in range(columns):
            number = int(block_numbers[i][j])
            if number > 0:
                block = Sprite(number_to_file[number], j * 50, i * 50, 50, 50)
                block.x_coord = j * 50
                background.append(block)

    iterations = 0
    seconds = 0
    game_state = 1
    for i in range(len(levels)):
        levels[i] = 1
    for i in range(len(levels) - 17):
        levels.pop(0)

def draw_everything():
    global iterations, seconds
    for block in background:
        block.draw()
        block.x_coord -= 0.5
        block.rect.x = block.x_coord


    player.draw()

    if player.jumping == 1:
        player.jump()
    else:
        player.gravity()

    for coin in coins:
        coin.draw()
        coin.rect.x -= 3

    for block in blocks:
        block.draw()
        block.rect.x -= 3
    
    if not player.can_remove:
        player.rect.x -= 3
        player.offset += 3
        if player.offset > 50:
            player.offset = player.offset % 50

    if blocks[0].rect.right < 0:
        generate(True)

    coin_score.draw()
    sc.blit(coin_text, (coin_score.rect.x + 40, coin_score.rect.y))

    collision()
    iterations += 1
    if iterations == 80:
        seconds += 1
        iterations = 0


button = pygame.Rect((WIDTH - 250) // 2, 320, 250, 66)
button_img = pygame.transform.scale(pygame.image.load('img/button.png').convert_alpha(), (250, 66))
def button_pressed(pos):
    if button.collidepoint(pos):
        return True
    return False


def draw_background(image):
    bg_img = pygame.image.load(image).convert_alpha()
    bg_img = pygame.transform.scale(bg_img, (800, 400))
    sc.blit(bg_img, (0, 0))