import os
from xml.sax.handler import feature_external_ges

import pygame
import pygame.freetype
import pygame.mixer
from pygame.sprite import RenderUpdates, LayeredUpdates, Sprite

from constants import GAME_DISPLAY, ORANGE, WHITE


def textOutput(line):
    fontTitle = pygame.font.SysFont("Gypsy_Curse", 32)
    textTitle = fontTitle.render(line, True, ORANGE)
    GAME_DISPLAY.blit(textTitle, (x, y))


pygame.display.update()
for line in inputedFile:
    text = line
    GAME_DISPLAY.fill(WHITE)
    fontTitle = pygame.font.SysFont("Gypsy_Curse", 32)
    textTitle = fontTitle.render(text, True, ORANGE)
    GAME_DISPLAY.blit(textTitle, (x, y))

    pygame.display.update()

inputedFile.close()


class Scence(Sprite):
    def Scence(imaged, dialogue):
        """
        Args:
         image - list (b[])
         sound-list (bm[])
         sounde-list(SE[])
         dialogue (txt) -list dialog ([n,x,y])
        """


def imaged(x, y):
    for i in range(0, len(FBG)):
        for x in range(x, y):
            pygame.image.load(FBG[x])
            screen = display_surface
            GAME_DISPLAY.fill(WHITE)
            X = 800
            Y = 600
            display_surface.blit(image, (0, 0))
            sound = pygame.mixer.load(bm[1])
            channel1 = pygame.mixer.Channel(0)
            pgyame.mixer.Channel.play()
            pygame.mixer.Channel.stop()


# 0
Scence.Scence(imaged(1, 2), dialog(2, 4, 15))
voice(5, 0, 4, 14)
vioce(4, 1, 4, 15)
feeling(0, 0, 6, 14)
feeling(10, 2, 8, 15)
sounde(5, True, 8)
sounde(0, True, 8)
# 1
Scence.Scence(imaged(3, 3), SE(8), dialog(2, 17, 43))
feeling(14, 2, 23, 25)
sounde(8, True, 23)
voice(6, 1, 17, 43)
voice(14, 0, 16, 43)
# 2
Scence.Scence(imaged(4, 6), dialog(1, 44, 49))
voice(6)
choice = input("Town Hall or Museum ?")
if choice == 1:
    # 3
    Scence.Scence(imaged(7, 7), dialog(1, 50, 60))
    voice(7, 0, 50, 60)
    feeling(5, 0, 54, 60)
    sounde(4, True, 54)
    sounde(5, True, 54)
    image = pygame.image.load(c[27])
    X = 400
    Y = 400
    display_surface.blit(image, (0, 0))
    move_to_front()
    move_to_bacK()
    for i in range(225):
        background.fill((0, 0, 0))
        image = pygame.image.load(c[28, 26])
        image.set_alpha(i)
        logoimage = GAME_DISPLAY.blit(image, (0, 0))
        pygame.display.flip()
        display_surface.blit(image, (0, 0))
        move_to_front()
        move_to_bacK()
elif choice == 2:
    # 4
    Scence.Scence(imaged(10, 15), dialog(2, 61, 84))
    sounde(2, True, 78)
    sounde(5, True, 78)
    voice(8, 1, 60, 83)
    voice(16, 0, 62, 84)
    feeling(5, 0, 76, 83)
    X = 700
    for t in range(0, 5):
        image = pygame.image.load(c[19])
        X -= 100
        Y = 400
        display_surface.blit(image, (0, 0))
        move_to_front()
        move_to_back()
    for i in range(225):
        background.fill((0, 0, 0))
        image = pygame.image.load(c[20])
        image.set_alpha(i)
        logoimage = GAME_DISPLAY.blit(image, (0, 0))
        pygame.display.flip()
        display_surface.blit(image, (0, 0))
        move_to_front()
# 5
Scence.Scence(imaged(16, 16), dialog(2, 85, 115))
voice(9, 0, 85, 114)
voice(1, 1, 85, 115)
sounde(4, True, 90)
# 114
if choice == 1 and x1 == 114 and "________":
    print("doll")
elif choice == 2 and x1 == 114 and "________":
    print("statue")
feeling(3, 0, 95, 106)
feeling(6, 1, 99, 106)
# 6
Scence.Scence(imaged(16, 16), dialog(3, 116, 123))
voice(10, 0, 116, 121)
voice(15, 1, 116, 122)
feeling(8, 1, 119, 122)
feeling(14, 4, 118, 122)
sounde(3, True, 119)
for p in range(0, 9):
    channel1 = pygame.mixer.Channel(p + 1)
    pygame.mixer.Channel.play()
    pygame.mixer.Channel.stop()
    voice(19, 2, 120, 123)
    feeling(16, 6, 128, 130)
    sounde(3, True, 127)
# 6_5
Scence.scence(imaged(16, 16), dialog(2, 125, 136))
feeling(15, 5, 127, 129)
voice(17, 1, 125, 135)
voice(11, 0, 125, 136)
# 7
Scence(imaged(3, 3), dialog([2, 138, 154]))
voice(12, 0, 138, 153)
voice(2, 1, 138, 154)
feeling(8, 1, 140, 154)
sounde(3, True, 140)
# 8
Scence.Scence(imaged(17, 19), dialog(3, 156, 270))
voice(13, 0, 156, 268)
voice(3, 1, 156, 269)
voice(18, 2, 156, 270)
feeling(8, 1, 160, 270)
feeling(5, 0, 192, 195)
feeling(18, 8, 160, 270)
sounde(3, True, 160)
