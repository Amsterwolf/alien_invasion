
class GameStatus:
    def __init__(self,ai):
        self.settings=ai.settings
        self.game_active=False
        self.reset_status()
    
    def reset_status(self):#初始化信息

        self.ship_now_lifes=self.settings.ship_whole_lifes

        