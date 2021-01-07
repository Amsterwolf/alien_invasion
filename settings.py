class Settings:
    def __init__(self,width=1200,height=800):
        self.width=width
        self.height=height
        self.bg_color=(250,250,250)
        
        self.ship_speed=1.7
        self.ship_whole_lifes=3

        self.bullet_speed=2.8
        self.bullet_width=3
        self.bullet_height=10
        self.bullet_color=(0,0,0)
        self.bullet_frequence=8
        #self.bullet_allowd=30

        self.ailen_speed_x=0.8
        self.ailen_speed_y=50.0
        self.ailen_move_direction=1

        self.speedup_scale=1.1
        #self.init_dynamic_settings()
    
    def init_dynamic_settings(self):
        self.ship_speed=1.7
        self.ship_whole_lifes=3

        self.bullet_speed=2.8
        self.bullet_frequence=8

        self.ailen_speed_x=1.2
        self.ailen_speed_y=50
        self.hard_level=1.0

    def increase_dynamic_settings(self):
        self.ailen_speed_x*=self.speedup_scale
        

