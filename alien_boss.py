import pygame
from alien import Alien
class AlienBoss(Alien):
    def __init__(self,ai):
        super().__init__(ai)
        self.status=ai.status
        self.image=pygame.image.load("images/rocketman.bmp")
        self.rect=self.image.get_rect()
        self.rect.top=self.screen_rect.top
        self.rect.x=self.screen_rect.centerx
        self.rect.y+=30
        self.skill_flag=0
        #self.HP=self.settings.alien_boss_HP*(self.status.level+1)/10
    
    def reset(self):
        
        self.HP=self.settings.alien_boss_HP*self.status.level/10
        self.totHP=self.HP
        self.settings.bullet_boss_speed_skill*=self.status.level/10
        self.settings.bullet_boss_speed*=self.status.level/10


    def update(self):
       
        num=self.HP%self.settings.alien_boss_skill_interval
        if self.skill_flag==False and num==0:
            self.HP-=1
            self.skill_flag=True
        if not self.skill_flag:
            self.x+=self.settings.alien_boss_speed_x*self.status.level/2*self.settings.ailen_move_direction
            self.rect.x=self.x
        