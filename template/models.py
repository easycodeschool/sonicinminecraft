import pygame
from global_ import *

class Sprite:
    def __init__(self, img_path, x, y, w, h, anim_timing=15, images=[]):
        self.rect = pygame.Rect(x, y, w, h)
        if type(img_path) is str:
            self.img = pygame.image.load(img_path).convert_alpha()
        else:
            self.img = img_path
        self.img = pygame.transform.scale(self.img, (w, h))
        self.cycle = 0
        self.images = images
        self.anim_timing = anim_timing
        for i in range(len(self.images)):
            self.images[i] = pygame.transform.scale(self.images[i], (w, h))
        self.current_image = 0

    def draw(self):
        sc.blit(self.img, (self.rect.x, self.rect.y))
        if len(self.images) > 0:
            self.animate()

    def animate(self):
        self.cycle += 1
        if self.cycle == self.anim_timing:
            self.current_image += 1
            if self.current_image >= len(self.images):
                self.current_image = 0
            self.img = self.images[self.current_image]
            self.cycle = 0

class Player(Sprite):
    def __init__(self, img_path, x, y, w, h, anim_timing=15, images=[]):
        super().__init__(img_path, x, y, w, h, anim_timing, images)
        self.current_gravity = 0.25
        self.current_dy = 8
        self.jumping = 0
        self.can_jump = True
        self.can_remove = True
        self.points = 0
        self.moved = 0
        self.offset = 0

    def gravity(self):
        global levels
        if self.jumping == 0:
            if self.rect.bottom < HEIGHT - levels[5 if levels[6] < levels[5] else 6] * 50:
                self.rect.y += self.current_dy
                self.current_dy += self.current_gravity
                self.can_jump = False
                self.img = sonic_down_img
            else:
                if levels[6] - levels[5] <= 1:
                    self.rect.bottom = HEIGHT - levels[5 if levels[6] < levels[5] else 6] * 50
                    self.current_gravity = 0.25
                    self.current_dy = 8
                else:
                    self.can_remove = False
                
                if self.rect.bottom <= HEIGHT - (levels[6] - 1) * 50:
                    self.can_remove = True

                self.can_jump = True

    def jump(self):
        self.rect.y -= self.current_dy
        self.current_dy -= self.current_gravity
        self.img = sonic_up_img
        if self.rect.bottom <= HEIGHT - (levels[6] - 1) * 50:
            self.can_remove = True
        if self.current_dy <= 0:
            self.jumping = 0
            self.current_gravity = 0.25
            self.current_dy = 0
            self.can_jump = True
            if self.offset != 0:
                self.rect.x += self.offset
            self.offset = 0

    def animate(self):
        if not self.can_remove:
            self.img = sonic_standing_img
        else:
            super().animate()

    


class Platform(Sprite):
    def __init__(self, x, y, w, h, speed):
        super().__init__(x, y, w, h)
        self.speed = speed

    def move(self):
        self.rect.x -= self.speed