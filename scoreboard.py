import pygame
from pygame.sprite import Group
from shipflag import Shipflag
class ScoreBoard:
    def __init__(self,ai):
        self.ai=ai
        self.screen=ai.screen
        self.screen_rect=self.screen.get_rect()
        self.settings=ai.settings
        self.status=ai.status
        
        self.text_color="black"
        self.font=pygame.font.SysFont(None,48)

        #self.prepare_score()
        self.prepare_ships()

    def prepare_score(self):
        str_score="{:,}".format((int)(self.status.score))
        self.image_score=self.font.render(str_score,True,self.text_color,
            self.settings.bg_color)

        self.score_rect=self.image_score.get_rect()
        self.score_rect.topright=self.screen_rect.topright
        self.score_rect.y+=50
        self.score_rect.x-=30

        str_high_score="top score: "+"{:,}".format((int)(self.status.high_score))
        self.image_high_score=self.font.render(str_high_score,True,self.text_color,
            self.settings.bg_color)

        self.score_rect2=self.image_high_score.get_rect()
        self.score_rect2.topright=self.screen_rect.topright
        self.score_rect2.y+=10
        self.score_rect2.x-=30
        
    def prepare_level(self):
        str_level="level: "+str(self.status.level)
        self.image_level=self.font.render(str_level,True,self.text_color,
            self.settings.bg_color)

        self.score_rect3=self.image_level.get_rect()
        self.score_rect3.topright=self.screen_rect.topright
        self.score_rect3.y+=90
        self.score_rect3.x-=30
        
    def prepare_ships(self):
        """显示剩余飞船"""
        self.ships=Group()
        for i in range(self.status.ship_now_lifes):
            ship=Shipflag(self.ai)
            ship.rect.x=10+i*(ship.rect.width+10)
            ship.rect.y=10
            self.ships.add(ship)
    def prepare_boss_life(self):
        left_life=self.ai.alien_boss.HP
        total_life=self.ai.alien_boss.totHP
        str_left_life="["
        for i in range(int(left_life*10/total_life)):
            str_left_life+="█"
        for j in range(10-int(left_life*10/total_life)):
            str_left_life+=" "
        str_left_life+="]"
        self.image_life=self.font.render(str_left_life,True,self.text_color,
            self.settings.bg_color)

        self.score_rect4=self.image_life.get_rect()
        self.score_rect4.midtop=self.screen_rect.midtop
        self.score_rect4.y+=0
        #self.score_rect4.x-=0
    
    def prepare_tip(self):
        str_tip="space:shoot    direction key:move    q:exit    p:start"
        self.image_tip=self.font.render(str_tip,True,self.text_color,
            self.settings.bg_color)

        self.score_rect5=self.image_tip.get_rect()
        self.score_rect5.topleft=self.screen_rect.topleft
        self.score_rect5.y+=30
        self.score_rect5.x+=30

    def show_score(self):
        self.prepare_score()
        #self.prepare_level()
        self.screen.blit(self.image_score,self.score_rect)
        self.screen.blit(self.image_high_score,self.score_rect2)
        self.screen.blit(self.image_level,self.score_rect3)
        self.ships.draw(self.screen)
        if self.ai.isboss_flag:
            self.prepare_boss_life()
            self.screen.blit(self.image_life,self.score_rect4)

    def show_tip(self):
        self.prepare_tip()
        self.screen.blit(self.image_tip,self.score_rect5)
