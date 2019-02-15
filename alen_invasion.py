import sys

import pygame

from settеings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Инициализирует pygame, settigs и объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.scree_width, ai_settings.scree_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)


    while True:
        gf.check_events(ship)
        ship.update()
        gf.updete_screen(ai_settings, screen, ship)
        pygame.display.flip()

run_game()
