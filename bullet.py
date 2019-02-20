import pygame
from pygame.sprite import Sprite

class Bullet (Sprite):
    """класс для управления пулями, выпушенными кораблем"""
    def __init__(self, ai_settings, screen, ship):
        """создание пули в текущей позтции коробля"""
        super().__init__()
        self.screen = screen

        # создание пули в позиции (0, 0) и насзначение правильной позиции
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_wight, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # позиция пули хранится в вещественном формате
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # обновление позтции пули в вещественном формате
        self.y -=self.speed_factor

        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
