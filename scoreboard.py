import pygame

class ScoreBoard:
    def __init__(self,ai):
        self.screen=ai.screen
        self.screen_rect=self.screen.get_rect
        self.settings=ai.settings
        self.status=ai.status

        self.text_color="black"
        self.font=pygame.font.SysFont(None,48)

        self.prepare_score()
    
    def prepare_score(self):
        str_score=self.status.score
        self.image_score=self.font.render(str_score,True,self.text_color,
            self.settings.bg_color)

        self.score_rect=self.image_score.get_rect()
        self.score_rect.topright=self.screen_rect.topright
    
    def show_score(self):
        self.screen.blit(self.image_score,self.score_rect)
