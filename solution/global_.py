import pygame

WIDTH = 800
HEIGHT = 400
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
levels = [1 for _ in range(17)]
start_bg = pygame.transform.scale(pygame.image.load('img/backgrounds/start_bg.png').convert_alpha(), (WIDTH, HEIGHT))

# images
coin1_img = pygame.image.load('img/coin/coin1.png').convert_alpha()
coin2_img = pygame.image.load('img/coin/coin2.png').convert_alpha()
coin3_img = pygame.image.load('img/coin/coin3.png').convert_alpha()
coin4_img = pygame.image.load('img/coin/coin4.png').convert_alpha()

sonic_default_img = pygame.image.load('img/sonic.png').convert_alpha()
sonic_standing_img = pygame.image.load('img/sonic_standing.png').convert_alpha()
sonic_up_img = pygame.image.load('img/sonic/sonic_up.png').convert_alpha()
sonic_down_img = pygame.image.load('img/sonic/sonic_down.png').convert_alpha()
sonic1_img = pygame.image.load('img/sonic/sonic1.png').convert_alpha()
sonic2_img = pygame.image.load('img/sonic/sonic2.png').convert_alpha()
sonic3_img = pygame.image.load('img/sonic/sonic3.png').convert_alpha()
sonic4_img = pygame.image.load('img/sonic/sonic4.png').convert_alpha()
sonic5_img = pygame.image.load('img/sonic/sonic5.png').convert_alpha()
sonic6_img = pygame.image.load('img/sonic/sonic6.png').convert_alpha()
sonic7_img = pygame.image.load('img/sonic/sonic7.png').convert_alpha()
sonic8_img = pygame.image.load('img/sonic/sonic8.png').convert_alpha()
sonic9_img = pygame.image.load('img/sonic/sonic9.png').convert_alpha()
sonic10_img = pygame.image.load('img/sonic/sonic10.png').convert_alpha()

# bg_textures
coal_bg_img = pygame.transform.scale(pygame.image.load('img/bg_textures/coal_bg.png').convert_alpha(), (50, 50))
diamond_bg_img = pygame.transform.scale(pygame.image.load('img/bg_textures/diamond_bg.png').convert_alpha(), (50, 50))
dirt_bg_img = pygame.transform.scale(pygame.image.load('img/bg_textures/dirt_bg.png').convert_alpha(), (50, 50))
emerald_bg_img = pygame.transform.scale(pygame.image.load('img/bg_textures/emerald_bg.png').convert_alpha(), (50, 50))
gold_bg_img = pygame.transform.scale(pygame.image.load('img/bg_textures/gold_bg.png').convert_alpha(), (50, 50))
grass_bg_img = pygame.transform.scale(pygame.image.load('img/bg_textures/grass_bg.png').convert_alpha(), (50, 50))
iron_bg_img = pygame.transform.scale(pygame.image.load('img/bg_textures/iron_bg.png').convert_alpha(), (50, 50))
lapis_bg_img = pygame.transform.scale(pygame.image.load('img/bg_textures/lapis_bg.png').convert_alpha(), (50, 50))
leaves_bg_img = pygame.transform.scale(pygame.image.load('img/bg_textures/leaves_bg.png').convert_alpha(), (50, 50))
redstone_bg_img = pygame.transform.scale(pygame.image.load('img/bg_textures/redstone_bg.png').convert_alpha(), (50, 50))
tree_bg_img = pygame.transform.scale(pygame.image.load('img/bg_textures/tree_bg.png').convert_alpha(), (50, 50))
wood_bg_img = pygame.transform.scale(pygame.image.load('img/bg_textures/wood_bg.png').convert_alpha(), (50, 50))

# textures
coal_img = pygame.transform.scale(pygame.image.load('img/textures/coal.png').convert_alpha(), (50, 50))
diamond_img = pygame.transform.scale(pygame.image.load('img/textures/diamond.png').convert_alpha(), (50, 50))
dirt_img = pygame.transform.scale(pygame.image.load('img/textures/dirt.png').convert_alpha(), (50, 50))
emerald_img = pygame.transform.scale(pygame.image.load('img/textures/emerald.png').convert_alpha(), (50, 50))
gold_img = pygame.transform.scale(pygame.image.load('img/textures/gold.png').convert_alpha(), (50, 50))
grass_img = pygame.transform.scale(pygame.image.load('img/textures/grass.png').convert_alpha(), (50, 50))
iron_img = pygame.transform.scale(pygame.image.load('img/textures/iron.png').convert_alpha(), (50, 50))
lapis_img = pygame.transform.scale(pygame.image.load('img/textures/lapis.png').convert_alpha(), (50, 50))
redstone_img = pygame.transform.scale(pygame.image.load('img/textures/redstone.png').convert_alpha(), (50, 50))
tree_img = pygame.transform.scale(pygame.image.load('img/textures/tree.png').convert_alpha(), (50, 50))
wood_img = pygame.transform.scale(pygame.image.load('img/textures/wood.png').convert_alpha(), (50, 50))