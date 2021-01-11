import pygame
from bullet import Bullet

class BulletBoss(Bullet):
    def __init__(self,ai):
        super().__init__(ai)
        self.ai=ai
        self.color=self.settings.bullet_boss_color
        self.rect=pygame.Rect(0,0,self.settings.bullet_boss_width,
            self.settings.bullet_boss_height)
        self.rect.midbottom=ai.alien_boss.rect.midbottom    #传递坐标
        self.rect.x-=ai.alien_boss.rect.width*0.35
        self.y=float(self.rect.y)

    def set_skill_size(self):
        self.color=self.settings.bullet_boss_color_skill
        self.rect=pygame.Rect(0,0,self.settings.bullet_boss_width_skill,
            self.settings.bullet_boss_height_skill)
        self.rect.midtop=self.ai.alien_boss.rect.midbottom    #传递坐标
        self.rect.x+=self.rect.width*0.25
        self.y=float(self.rect.y)

    def update(self):
        self.y+=self.settings.bullet_boss_speed
        self.rect.y=self.y
