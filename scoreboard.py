import pygame.font

class Scoreboard:
    def __init__(self,ai_game) :
        """初始化显示得分涉及的属性"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #显示得分信息时使用的字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.Font(self.settings.font_path,26)

        #这边初始得分图像,最高分图像
        self.prep_score()
        self.prep_countdown(self.stats.countdown_count)


    def prep_score(self):
        """将得分渲染为图像"""
        rounded_score = round(self.stats.score,-1)
        score_str = f"得   分：{rounded_score:,}"
        self.score_image = self.font.render(score_str , True ,self.text_color , self.settings.bg_color)

        #在屏幕右上角显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_countdown(self , remaining_time):
        """将倒计时渲染为图像"""
        rounded_score = int(remaining_time)
        score_str = f"倒计时：{rounded_score}"
        self.countdown_image = self.font.render(score_str , True ,self.text_color , self.settings.bg_color)
        #在屏幕右上角显示得分
        self.countdown_rect = self.countdown_image.get_rect()
        self.countdown_rect.right =  150
        self.countdown_rect.top = 20


    def show_score(self):
        """在屏幕上显示得分 和 倒计时"""
        self.screen.blit(self.score_image , self.score_rect)
        self.screen.blit(self.countdown_image , self.countdown_rect)
        # self.screen.blit(self.high_score_image , self.high_score_rect)
        # self.screen.blit(self.level_image,self.level_rect)
        # self.ships.draw(self.screen)

