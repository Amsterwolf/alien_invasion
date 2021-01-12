class Settings:
    def __init__(self,width=1200,height=800):
        self.width=width
        self.height=height
        self.bg_color=(250,250,250)
        
        self.ship_speed=1.7
        self.ship_whole_lifes=3

        self.bullet_speed=2.8
        self.bullet_width=3#*1200
        self.bullet_height=10
        self.bullet_color=(0,0,0)
        self.bullet_frequence=8
        #self.bullet_allowd=30

        self.bullet_boss_speed=0.8
        self.bullet_boss_width=8
        self.bullet_boss_height=10
        self.bullet_boss_color="purple"
        self.bullet_boss_frequence=200

        self.bullet_boss_speed_skill=2
        self.bullet_boss_color_skill="black"
        self.bullet_boss_width_skill=250
        self.bullet_boss_height_skill=25
        self.bullet_boss_frequence_skill=30
        self.bullet_boss_skill_num=1
        self.ailen_speed_x=0.8
        self.ailen_speed_y=50.0
        self.ailen_move_direction=1
        self.alien_point=1.0
        self.speedup_scale=1.05
        #self.init_dynamic_settings()
        self.alien_HP=1
        self.alien_boss_HP=1000-1
        self.alien_boss_speed_x=0.5
        self.alien_boss_skill_interval=int(0.1*self.alien_boss_HP)
        

    def init_dynamic_settings(self):
        self.ship_speed=1.5
        self.ship_whole_lifes=3

        self.bullet_speed=2.5
        self.bullet_frequence=8

        self.ailen_speed_x=0.8
        self.ailen_speed_y=50
        self.alien_point=1.0
        self.hard_level=1.0
        self.alien_HP=1
        self.alien_boss_HP=1000-1

        self.bullet_boss_speed=0.8
        self.bullet_boss_speed_skill=2

    def increase_dynamic_settings(self):
        self.ailen_speed_x*=self.speedup_scale
        self.ship_speed*=self.speedup_scale
        self.alien_point*=self.speedup_scale
        
        #print(self.alien_point)
        
        

        

