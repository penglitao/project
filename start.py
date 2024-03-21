import sys
import pygame
from setting import Settings
from button import Button
class Start:
    def __init__(self) :
        pygame.init()
        # self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width , self.settings.screen_height))
        pygame.display.set_caption(self.settings.game_title)

        self.game_active = False
        self.play_button = Button(self,'Play')

        

    def run_game(self):
        while True:
            self._check_events()
            self._update_events()
            # self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                
    def _update_events(self):
        self.screen.fill(self.settings.bg_color)

        if not self.game_active:
            self.play_button.draw_button()
        else:
            self.top_button = Button(self,'宋')
            self.top_button.draw_button()

        pygame.display.flip()

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.game_active = True



if __name__ == '__main__':
    ai = Start()
    ai.run_game()