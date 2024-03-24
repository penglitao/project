class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height=800
        self.game_title = '猜字游戏'
        self.font_path = 'resource/font/ALiMaMaFangYuanTi/AlimamaFangYuanTiVF-Thin-2.ttf'
        self.bg_color =(230,230,230)

        #top按键属性设置
        self.top_width,self.top_height = 150 ,150
        self.top_button_color = (0,135,0)
        self.top_text_color = (255,255,255)
        self.top_font_path = self.font_path
        self.top_font_size = 52

        #play按钮属性设置
        self.play_width ,self.play_height = 200 ,100
        self.play_button_color = (0,135,0)
        self.play_text_color = (255,255,255)
        self.play_font_size = 42
        self.play_font_path = self.font_path
        #end按钮属性设置
        self.end_width ,self.end_height = 200 ,100
        self.end_button_color = (255,0,0)
        self.end_text_color = (255,255,255)
        self.end_font_size = 42
        self.end_font_path = self.font_path
        #select 按键属性设置
        self.select_width,self.select_height = 100 ,50
        self.select_button_color = (0,135,0)
        self.select_text_color = (255,255,255)
        self.select_font_path = self.font_path
        self.select_font_size = 42

        #定义检测列表
        self.word_list = ['上','下','左','右','天','人','口','手','足','地','日','月','水','火','田','里','风','雨','雪','力','大','小','多','少','园']

        #积分设置
        self.points = 50

        #错误按钮颜色
        self.error_button_color = (255,0,0)
        #声音文件
        self.correct_wav = 'resource/wav/correct.wav'
        self.error_wav = 'resource/wav/error.wav'