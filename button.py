import pygame

class Button:
    def __init__(self,ai,msg):
        self.screen=ai.screen
        self.screen_rect=self.screen.get_rect()

        self.width=200
        self.height=120
        self.button_color=(200,150,200)
        self.text_color="white"
        self.font=pygame.font.SysFont('arial',32)

        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center
        self._prepare_msg(msg)

    def _prepare_msg(self,msg):
        self.msg_image=self.font.render(msg,True,self.text_color,
            self.button_color)#渲染成图像
        self.msg_image_rect=self.msg_image.get_rect()#set pos
        self.msg_image_rect.center=self.rect.center
    
    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)#绘制一个颜色填充的按钮
        self.screen.blit(self.msg_image,self.msg_image_rect)#内容and边框




