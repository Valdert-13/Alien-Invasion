class Settings():
    """Класс для хранения настроек игры"""

    def __init__(self):
        """Иницализирует настройки игры"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
#         создание настроек пули
        self.bullet_speed_factor = 1
        self.bullet_wight = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allower = 3
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1