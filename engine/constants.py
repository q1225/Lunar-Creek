import os

import pygame

# Colours
WHITE: tuple[int, int, int] = (255, 255, 255)
ORANGE: tuple[int, int, int] = (255, 165, 0)
RED: tuple[int, int, int] = (255, 0, 0)
PURPLE: tuple[int, int, int] = (159, 43, 104)
MIDNIGHT_BLUE: tuple[int, int, int] = (199, 9, 70)

ROOT: str = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
SAVE_FOLDER = os.path.join(ROOT, "saves")

GAME_DISPLAY = pygame.display.set_mode((800, 600))
