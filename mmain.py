import sys,pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
class AlienInvasion:
    def __init__(self,isfullscreen=False):
        pygame.init()
        self.settings=Settings()
        if not isfullscreen:
            self.screen=pygame.display.set_mode(
                (self.settings.width,self.settings.height))#character 
        else:
            self.screen=pygame.display.set_mode()
            self.settings.width=self.screen.get_rect().width
            self.settings.width=self.screen.get_rect().height
        pygame.display.set_caption("外星人入侵 v1.0")

        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()


    def _check_events(self):#响应键鼠
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()  
            elif event.type==pygame.KEYDOWN:
                self._key_down_events(event)
            elif event.type==pygame.KEYUP:
                self._key_up_events(event)
    
    def _key_down_events(self,event):
        if event.key==pygame.K_RIGHT:
            self.ship.ship_move_right=True
        elif event.key==pygame.K_LEFT:
            self.ship.ship_move_left=True
        elif event.key==pygame.K_UP:
            self.ship.ship_move_up=True
        elif event.key==pygame.K_DOWN:
             self.ship.ship_move_down=True
        elif event.key==pygame.K_q:     #按Q退出
            sys.exit()
        elif event.key==pygame.K_SPACE: #空格射击
            self._fire_bullet()
    
    def _key_up_events(self,event):
        if event.key==pygame.K_RIGHT:
            self.ship.ship_move_right=False
        elif event.key==pygame.K_LEFT:
            self.ship.ship_move_left=False
        elif event.key==pygame.K_UP:
            self.ship.ship_move_up=False
        elif event.key==pygame.K_DOWN:
            self.ship.ship_move_down=False
    
    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
                bullet.draw_bullet()
        pygame.display.flip()

    def _fire_bullet(self):
        '发射子弹'
        new_bullet=Bullet(self)      #新建子弹
        self.bullets.add(new_bullet) #编组增加元素

    def run_game(self):
        self.screen.fill(self.settings.bg_color)#设置背景颜色
        while 1:#每次检查
            #print(pygame.event.get())
             
            #pygame.display.flip()#refresh
            #self.ship.blitme()
            self._check_events()  
            self.ship.ship_move()
            self.bullets.update()

            

            self.update_screen()

    
if __name__=="__main__":
    ai=AlienInvasion()
    ai.run_game()