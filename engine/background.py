import pygame
from constants import GAME_DISPLAY, WHITE
from media import background_images, background_music, character_images
from pygame.sprite import LayeredUpdates
from scence import imaged


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
    from play_level import play_level  # deferred: play_level imports ts from here

    for x in range(0, len(sc)):
        s = x
        sc = [4, 7, 40, 50, 61, 85, 116, 125, 138, 156]
        with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
            lines = [lines.rstrip() for lines in fl]
        if lines == sc[x]:
            play_level()


def seal():
    from play_level import play_level  # deferred: play_level imports ts from here

    for k in range(0, 3):
        seal = [17, 104, 128]
    with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
        lines = [lines.rstrip() for lines in fl]
        if lines == seal[k]:
            play_level()
            image = character_images[25]
            GAME_DISPLAY.blit(image(400, 400))
            LayeredUpdates.move_to_front
