import sys

import pygame



# noinspection PyUnresolvedReferences
def run_game():
    # noinspection PyUnresolvedReferences
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)

    while True:
        #Отслеживание клавиатуры и мыши
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)

        pygame.display.flip()

run_game()
