import pygame
from pygame.sprite import LayeredUpdates, RenderUpdates

from GameState import GameState
from UIElement import UIElement
from constants import RED, GAME_DISPLAY, WHITE
from game_loop import game_loop
from main import background_images, background_music, chacter_imaages


def ts(x):
    for l in range(0, len(ts)):
        ts = [
            4,
            6,
            17,
            31,
            40,
            44,
            50,
            57,
            61,
            62,
            68,
            85,
            89,
            91,
            117,
            137,
            152,
            154,
            156,
            177,
        ]
    with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
        lines = [lines.rstrip() for lines in fl]
    if lines == ts[l]:
        for x in range(1, len(imaged())):
            x = l
            soundb = background_music[1]
            channel1 = pygame.mixer.Channel(0)
            channel1.play(soundb)
            image = (background_images[x],)
            GAME_DISPLAY.fill(WHITE)
            GAME_DISPLAY.blit(image, (0, 0))


def new_scence(s):
    for x in range(0, len(sc)):
        s = x
        sc = [4, 17, 40, 50, 61, 85, 116, 125, 138, 156]
        with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
            lines = [lines.rstrip() for lines in fl]
        if lines == sc[x]:
            nextlevel_btn = UIElement(
                center_position=(400, 700),
                font_size=30,
                bg_rgb=WHITE,
                text_rgb=RED,
                action=GameState.NEXT_LEVEL,
            )
    buttons = RenderUpdates(nextlevel_btn)
    return game_loop(buttons)


def seal():
    for k in range(0, 3):
        seal = [17, 104, 128]
    with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
        lines = [lines.rstrip() for lines in fl]
        if lines == seal[k]:
            image = chacter_imaages[25]
            GAME_DISPLAY.blit(image(400, 400))
            LayeredUpdates.move_to_front
