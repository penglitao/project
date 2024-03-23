import time
class GameStats:
    """跟踪游戏的统计信息"""
    def __init__(self ,aigame):
        """初始化统计信息"""
        self.settings = aigame.settings
        self.score = 0

        #在任何情况下都不应该 重置最高分
        self.high_score = 0
        self.level = 0

        #默认倒计时
        self.start_time = time.time()
        self.countdown_count = 10


    def reset_score(self):
        self.score = 0

    def reset_level(self):
        self.level = 0