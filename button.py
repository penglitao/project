import pygame.font
class Button:
    """定义button按钮"""
    def __init__(self, ai_game , msg):
        
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        self.width ,self.height = 200 ,50
        self.button_color = (0,135,0)
        self.text_color = (255,255,255)
        self.font_path = self.settings.font_path
        print(self.font_path)
        self.font = pygame.font.Font(self.font_path,42)

        #按键的位置
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    
    def _prep_msg(self,msg):
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        self.screen.fill(self.button_color ,self.rect)
        self.screen.blit(self.msg_image ,self.msg_image_rect)