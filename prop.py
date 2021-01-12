import pygame
from pygame.sprite import Sprite
import random
class Prop(Sprite):
    def __init__(self,ai):
        super().__init__()
        self.ai=ai
        self.screen=ai.screen
        self.screen_rect=self.screen.get_rect()
        self.set_image()

    def set_image(self):
        random_int=random.randint(1,3)#
        self.flag=random_int
        if random_int==1:
            self.image=pygame.image.load("images/heart.bmp")
        elif random_int==2:
            self.image=pygame.image.load("images/speedup.bmp")
        else:
            self.image=pygame.image.load("images/bulletspeed.bmp")

        self.rect=self.image.get_rect()
        self.rect.x=random.random()*self.screen_rect.width
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
        if random.random()>=0.5:
            self.direct_flag=1
        else:
            self.direct_flag=-1
        
        self.speed=1.0

    def update(self):
        if self.rect.x>=self.screen_rect.width-self.rect.width :
            self.direct_flag=-1
        elif self.rect.x<=self.rect.width:
            self.direct_flag=1
        self.x+=self.speed*self.direct_flag
        self.y+=self.speed*0.5
        self.rect.x=self.x
        self.rect.y=self.y

