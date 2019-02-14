import sys

import pygame

from settеings import Settings



def run_game():
    # Инициализирует pygame, settigs и объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.scree_width, ai_settings.scree_height))
    pygame.display.set_caption("Alien Invasion")


    while True:
        #Отслеживание клавиатуры и мыши
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)

        pygame.display.flip()

run_game()
