import pygame
from pygame.sprite import Sprite
class Shipflag(Sprite):
    def __init__(self,ai):
        super().__init__()
        self.screen=ai.screen
        self.screen_rect=self.screen.get_rect()#屏幕外接矩形
        self.settings=ai.settings
         
        self.image=pygame.image.load("images/shiplife.bmp")
        self.rect=self.image.get_rect()


    

    


