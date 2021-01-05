import sys,pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
import random
from time import sleep
from game_status import GameStatus
from button import Button
class AlienInvasion:
    def __init__(self,isfullscreen=False):
        pygame.init()
        self.settings=Settings()
        self.status=GameStatus(self)
        
        

        if not isfullscreen:
            self.screen=pygame.display.set_mode(
                (self.settings.width,self.settings.height))#character 
        else:
            self.screen=pygame.display.set_mode()
            self.settings.width=self.screen.get_rect().width
            self.settings.width=self.screen.get_rect().height

        self.screen_rect=self.screen.get_rect()
        self.button=Button(self,"Play")

        pygame.display.set_caption("外星人入侵 v1.0")

        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
        self.autofire=False
        self.aliens=pygame.sprite.Group()
       

        self.count=0
        


    def _check_events(self):#响应键鼠
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()  
            elif event.type==pygame.KEYDOWN:
                self._key_down_events(event)
            elif event.type==pygame.KEYUP:
                self._key_up_events(event)
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
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
            self.autofire=True
            #self._fire_bullet()
        elif event.key==pygame.K_p:
            self._check_by_K()
    
    def _key_up_events(self,event):
        if event.key==pygame.K_RIGHT:
            self.ship.ship_move_right=False
        elif event.key==pygame.K_LEFT:
            self.ship.ship_move_left=False
        elif event.key==pygame.K_UP:
            self.ship.ship_move_up=False
        elif event.key==pygame.K_DOWN:
            self.ship.ship_move_down=False
        elif event.key==pygame.K_SPACE:
            self.autofire=False
    
    def start_screen(self):
        
        if not self.status.game_active:
            self.screen.fill(self.settings.bg_color)
            self.button.draw_button()
            pygame.display.flip()   #刷新画面

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        #self.alien.blitme()

        self.aliens.draw(self.screen) 
        self._update_bullets()
        self._update_ufo_move()
        self._check_bullets_aliens_collision()
        self._check_aliens_ship_collision()
        self._check_aliens_arrive_bottom()
        pygame.display.flip()   #刷新画面

    def _fire_bullet(self):
        '发射子弹'
        #if len(self.bullets)<=self.settings.bullet_allowd:
        new_bullet=Bullet(self)      #新建子弹
        self.bullets.add(new_bullet) #编组增加元素
    
    def _is_ufo_to_drop(self):
        for alien in self.aliens.sprites():#对群组中每个成员
            if alien._check_edge():
                return True


    def _update_ufo_move(self):
        
        self.aliens.update()
        if self._is_ufo_to_drop():
            for alien in self.aliens.sprites():
                alien.rect.y+=self.settings.ailen_speed_y
            self.settings.ailen_move_direction*=-1
        #print(len(self.aliens))
        
    def _update_bullets(self):
        self.bullets.update()   #对每个精灵呼叫更新函数
        self.count+=1
        if self.autofire and self.count % self.settings.bullet_frequence==0:
            self._fire_bullet() #如果一直按着空格
            
        for bullet in self.bullets.copy():
            if bullet.rect.y<0:
                self.bullets.remove(bullet)
            #print(len(self.bullets))
        for bullet in self.bullets.sprites():
                bullet.draw_bullet()
           
    def _check_bullets_aliens_collision(self):
        collision=pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if len(self.aliens)==0:
            sleep(0.1)
            self.bullets.empty()
            self._creat_fleet()
    
    def _check_aliens_ship_collision(self):
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            print("Ship hit!!")
            self._ship_hit()
    
    def _check_aliens_arrive_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.top>=self.screen_rect.bottom:
                self._ship_hit()
                break

    def _check_play_button(self,mouse_pos):
        if self.button.rect.collidepoint(mouse_pos) and self.status.game_active==False:
            
            self.status.reset_status()
            self.status.game_active=True
            pygame.mouse.set_visible(False)
    
    def _check_by_K(self):
        if self.status.game_active==False:
            self.status.reset_status()
            self.status.game_active=True
            pygame.mouse.set_visible(False)



    def _ship_hit(self):
        self.status.ship_now_lifes-=1

        if not self.status.ship_now_lifes:
            self.status.game_active=False
            print("Game over!!!")
            pygame.mouse.set_visible(True)
           
        
        self.ship.back_original_pos()
        self.aliens.empty()
        self.bullets.empty()
        self._creat_fleet()
        sleep(0.5)

    def _creat_fleet(self):
        new_ufo=Alien(self)
        new_ufo_width=new_ufo.rect.width
        new_ufo_height=new_ufo.rect.height
        available_space_x=self.settings.width-new_ufo_width*2
        available_space_y=self.settings.height-new_ufo_height*2-self.ship.height*3
        numbers_ufo_x=available_space_x//(2*new_ufo_width)
        numbers_ufo_y=int(available_space_y/(2*new_ufo_height))
        for j in range(numbers_ufo_y):
            for i in range(numbers_ufo_x):    
                ufo=Alien(self) #创建一排ufo 
                ufo.rect.x=(1+i*2)*new_ufo_width
                ufo.x=ufo.rect.x
                ufo.rect.y=(2*j)*new_ufo_height
                ufo.y=ufo.rect.y
                self.aliens.add(ufo)#end

        
        

    def run_game(self):
        self.screen.fill(self.settings.bg_color)#设置背景颜色
        self._creat_fleet()
        while 1:#每次检查
            self.start_screen()
            self._check_events()
            
            if self.status.game_active:  
                self.ship.ship_move()

                self.update_screen()

    
if __name__=="__main__":
    ai=AlienInvasion()
    
    ai.run_game()