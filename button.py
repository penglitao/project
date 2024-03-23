import pygame
class Button:
    """定义button按钮"""
    def __init__(self, ai_game ,text,x,y,width,height,color,bg_color,font_path,font_size):
        
        self.text = text
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.text_color = color
        self.button_color = bg_color

        self.font = pygame.font.Font(font_path,font_size)

        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.correct_wav = pygame.mixer.Sound(self.settings.correct_wav)
        self.error_wav = pygame.mixer.Sound(self.settings.error_wav)

        #是否改变按钮颜色
        self.is_change = False
    
    def _prep_msg(self,text):
        self.msg_image = self.font.render(text,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        #按键的位置
        self._prep_msg(self.text)
        self.screen.fill(self.button_color if not self.is_change else self.settings.error_button_color ,self.rect)
        self.screen.blit(self.msg_image ,self.msg_image_rect)
        