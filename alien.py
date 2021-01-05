import pygame
from pygame.sprite import Sprite
import random
class Alien(Sprite):
    def __init__(self,ai):
        super().__init__()
        self.screen=ai.screen
        self.screen_rect=self.screen.get_rect()
        self.settings=ai.settings
        self.settings.ailen_move_direction=self.settings.ailen_move_direction

        self.image=pygame.image.load("images/ufo.bmp")
        self.rect=self.image.get_rect()
        self.rect.topleft=self.screen_rect.topleft
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def _check_edge(self):
        if self.rect.right>self.screen_rect.right or self.rect.left<0:
            return True
    def update(self):
        self.x+=self.settings.ailen_speed_x*self.settings.ailen_move_direction
        self.rect.x=self.x