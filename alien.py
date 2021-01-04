import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,ai):
        super().__init__()
        self.screen=ai.screen
        self.screen_rect=self.screen.get_rect()

        self.image=pygame.image.load("images/ufo.bmp")
        self.rect=self.image.get_rect()
        self.rect.topleft=self.screen_rect.topleft
        self.x=float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)
