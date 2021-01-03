import pygame

class Ship:
    def __init__(self,ai):
        self.screen=ai.screen
        self.screen_rect=self.screen.get_rect()#屏幕外接矩形
        self.settings=ai.settings

        self.width=35
        self.height=53

        self.speed=ai.settings.ship_speed 
        
        self.image=pygame.image.load("images/ship.bmp")
        self.rect=self.image.get_rect()

        self.rect.midbottom=self.screen_rect.midbottom #定飞机初始位置
        #print(self.rect.midbottom)
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)

        self.ship_move_right=False
        self.ship_move_left=False
        self.ship_move_up=False
        self.ship_move_down=False

    def blitme(self):
        self.screen.blit(self.image,self.rect)  #绘制飞机

    def ship_move(self):
        if self.ship_move_left and self.rect.centerx>=self.width:
            self.x-=self.speed
        if self.ship_move_right and self.rect.centerx<=self.screen_rect.right-self.width:
            self.x+=self.speed
        
        if self.ship_move_up and self.rect.centery>=self.height:
            self.y-=self.speed
        if self.ship_move_down and self.rect.centery<=self.screen_rect.bottom-self.height:
            self.y+=self.speed

        self.rect.centerx=self.x
        self.rect.centery=self.y


