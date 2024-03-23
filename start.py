import sys
import pygame
from setting import Settings
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
import random
import time
class Start:
    def __init__(self) :
        pygame.init()
        pygame.mixer.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width , self.settings.screen_height))
        pygame.display.set_caption(self.settings.game_title)

        # 假设你想要按钮居中在屏幕上  
        self.game_active = 'play'

        #设置倒计时开始
        self.game_start = False

        #初始化 top_botton 的汉字
        self._create_top_button_text()
        self._create_select_button_text()

        #创建一个用于存储游戏统计信息的实例，并创建计分牌
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.sb.prep_score()
        

    def run_game(self):
        while True:
            self._update_events()
            self._check_events()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                
    def _update_events(self):
        self.screen.fill(self.settings.bg_color)

        if self.game_active == 'play':
            self._create_play_button()
            self.play_button.draw_button()
            self.sb.show_score()
        elif self.game_active == 'end':
            self._create_end_button()        
        else:
            #top按钮
            self._create_top_button()
            #select按钮
            self._create_select_button()

            if self.game_start :
                self.stats.start_time = time.time()
                self.game_start = False

            # 更新并显示倒计时  
            current_time = time.time()  
            # print(current_time)
            elapsed_time = current_time - self.stats.start_time  # 已经过去的时间（秒） 
            # print(elapsed_time) 
            remaining_time = self.stats.countdown_count - elapsed_time  # 剩余时间（秒）  
            if remaining_time > 0 :
                self.sb.prep_countdown(remaining_time)
                self.sb.show_score()
            else:
                #倒计时结束
                self.sb.show_score()
                self.game_active = 'end'
            
            
        pygame.display.flip()

        clock = pygame.time.Clock()
        clock.tick(60)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and self.game_active == 'play':
            self.game_active = 'runing'
            self.sb.prep_score()
            self.game_start = True
        elif self.game_active == 'end':
            for end_button in self.end_buttons:
                if end_button.rect.collidepoint(mouse_pos):
                    if end_button.text =='End':
                        sys.exit()
                    else:
                        self.game_active = 'runing'
                        #重置top_button 文字
                        self._create_top_button_text()
                        #重置top_button 按钮
                        self._create_top_button()
                        #重置select_button 文字
                        self._create_select_button_text()
                        #重置select_button 按钮
                        self._create_select_button()
                        self.stats.score =0
                        self.stats.level =0
                        self.sb.prep_score()
                        self.stats.start_time = time.time()
                        self.sb.prep_countdown(self.stats.countdown_count)
        else:
            for select_button in self.select_buttons:
                if select_button.rect.collidepoint(mouse_pos):
                    if select_button.text == self.top_text :
                            
                            select_button.correct_wav.play()
                            #重置top_button 文字
                            self._create_top_button_text()
                            #重置top_button 按钮
                            self._create_top_button()
                            #重置select_button 文字
                            self._create_select_button_text()
                            #重置select_button 按钮
                            self._create_select_button()

                            self.stats.score += self.settings.points
                            self.stats.level +=1
                            self.sb.prep_score()
                            self.stats.start_time = time.time()
                            self.sb.prep_countdown(self.stats.countdown_count)

                    else:
                        select_button.error_wav.play()



    def _create_top_button(self):
        """创建 top 按钮"""
        self.top_button = Button(self,self.top_text,(self.settings.screen_width -self.settings.top_width)//2,
                                  50,
                                  self.settings.top_width,
                                  self.settings.top_height,
                                  self.settings.top_text_color,
                                  self.settings.top_button_color,
                                  self.settings.top_font_path,
                                  self.settings.top_font_size
                                  )
        self.top_button.draw_button()

    def _create_top_button_text(self):
        """创建top按钮文字"""
        self.top_text = random.choice(self.settings.word_list)

    def _create_select_button(self):
        self.select_buttons = []
        for i in range(len(self.select_texts)):
            select_button = Button(self,self.select_texts[i],(i + 1) * (self.settings.select_width + 110),
                                  400,
                                  self.settings.select_width,
                                  self.settings.select_height,
                                  self.settings.select_text_color,
                                  self.settings.select_button_color,
                                  self.settings.select_font_path,
                                  self.settings.select_font_size
                                  )
            select_button.draw_button()
            self.select_buttons.append(select_button)

    def _create_select_button_text(self):
        self.copy_word_list = self.settings.word_list[:]
        self.copy_word_list.remove(self.top_text)
        self.select_texts = random.sample(self.copy_word_list,3)
        self.select_texts.append(self.top_text)
        random.shuffle(self.select_texts)

    def _create_play_button(self):
        self.play_button = Button(self,'Play',self.settings.screen_width // 2 - self.settings.play_width // 2,
                                  self.settings.screen_height // 2 - self.settings.play_height // 2,
                                  self.settings.play_width,
                                  self.settings.play_height,
                                  self.settings.play_text_color,
                                  self.settings.play_button_color,
                                  self.settings.play_font_path,
                                  self.settings.play_font_size
                                  )
    
    def _create_end_button(self):
        self.end_text = ['End','Reset']
        self.end_buttons = []
        for i in range(len(self.end_text)):
            end_button = Button(self,self.end_text[i],(i + 1) * (self.settings.end_width + 140),
                                  self.settings.screen_height // 2 - self.settings.end_height // 2,
                                  self.settings.end_width,
                                  self.settings.end_height,
                                  self.settings.end_text_color,
                                  self.settings.end_button_color,
                                  self.settings.end_font_path,
                                  self.settings.end_font_size
                                  )
            end_button.draw_button()
            self.end_buttons.append(end_button)


if __name__ == '__main__':
    ai = Start()
    ai.run_game()