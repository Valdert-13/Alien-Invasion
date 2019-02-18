class Settings():
    """Класс для хранения настроек игры"""

    def __init__(self):
        """Иницализирует настройки игры"""
        self.scree_width = 1200
        self.scree_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
#         создание настроек пули
        self.bullet_speed_factor = 1
        self.bullet_wight = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allower = 3
