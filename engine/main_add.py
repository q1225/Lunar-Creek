import os
from xml.sax.handler import feature_external_ges
from scence import*
import pygame
import pygame.freetype
import pygame.mixer
from pygame.sprite import RenderUpdates,LayeredUpdates, Sprite
from scence import*
from constants import GAME_DISPLAY, ORANGE, WHITE
from speech_and_character import* 
from sound import*
x=0
y=0
def textOutput(line):
    fontTitle = pygame.font.SysFont("Gypsy_Curse", 32)
    textTitle = fontTitle.render(line, True, ORANGE)
    GAME_DISPLAY.blit(textTitle, (x, y))

inputedFile= open("Cult_of_Seal_VN_lines_Final.docx", "r")
pygame.display.update()
for line in inputedFile:
    text = line
    GAME_DISPLAY.fill(WHITE)
    fontTitle = pygame.font.SysFont("Gypsy_Curse", 32)
    textTitle = fontTitle.render(text, True, ORANGE)
    GAME_DISPLAY.blit(textTitle(x, y))

    pygame.display.update()

inputedFile.close()





# 0
Scence(imaged(1, 2),dialog(4,16) )
voice(5, 0, 4, 14)
voice(4, 1, 4, 15)
feeling(0,1,4,6)
feeling(0, 0, 6, 14)
feeling(2, 10, 8, 15)
sounde(5, True, 8)
sounde(0, True, 8)
# 1
Scence(imaged(3, 3), dialog( 17, 43))
feeling(2, 14, 23, 25)
sounde(8, True, 23)
voice(6, 1, 17, 43)
voice(14, 0, 16, 43)
# 2
Scence(imaged(4, 6), dialog( 44, 49))
voice(6)
choice = input("Town Hall or Museum ?")
if choice == 1:
    # 3
    Scence(imaged(7, 9), dialog( 50, 60))
    voice(7, 0, 50, 60)
    feeling(0, 5, 54, 60)
    sounde(4, True, 54)
    sounde(5, True, 54)
    image = pygame.image.load(character_images[27])
    X = 400
    Y = 400
    GAME_DISPLAY.blit(image, (X, Y))
    LayeredUpdates.move_to_front()
    LayeredUpdates.move_to_bacK()
    for i in range(225):
        image = character_images[28, 26]
        image.set_alpha(i)
        logoimage = GAME_DISPLAY.blit(image, (0, 0))
        pygame.display.flip()
        GAME_DISPLAY.blit(image, (400, 400))
        LayeredUpdates.move_to_front()
    LayeredUpdates.move_to_bacK()
elif choice == 2:
    # 4
    Scence(imaged(10, 15), dialog( 61, 84))
    sounde(2, True, 78)
    sounde(5, True, 78)
    voice(8, 1, 60, 83)
    voice(16, 0, 62, 84)
    feeling(0, 5, 76, 83)
    x= 700
    for t in range(0, 5):
        image = character_images[19]
        x-=100
        GAME_DISPLAY .blit(image, (x, 400))
        LayeredUpdates.move_to_front()
    LayeredUpdates.move_to_back()
    for i in range(225):
        image = character_images[20]
        image.set_alpha(i)
        pygame.display.flip()
        GAME_DISPLAY.blit(image, (400, 400))
        LayeredUpdates.move_to_front()
    LayeredUpdates.move_to_back()
# 5
Scence(imaged(16, 16), dialog( 85, 115))
voice(9,0 , 85, 114)
voice(1, 1, 85, 115)
sounde(4, True, 90)
# 114
if choice == 1 and x == 114 and "________":
    print("doll")
elif choice == 2 and x == 114 and "________":
    print("statue")
feeling(0, 3, 95, 106)
feeling(1, 6, 99, 106)
# 6
Scence(imaged(16, 16), dialog( 116, 123))
voice(10, 0, 116, 121)
voice(15, 1, 116, 122)
feeling(1, 8, 119, 122)
feeling(4,14 , 118, 122)
sounde(3, True, 119)
for p in range(0, 9):
    channel1 = pygame.mixer.Channel(p + 1)
    pygame.mixer.Channel.play()
    pygame.mixer.Channel.stop()
    voice(19, 2, 120, 123)
    feeling(6,16 , 128, 130)
    sounde(3, True, 127)
# 6_5
Scence(imaged(16, 16), dialog( 125, 136))
feeling (0,0,125,136)
feeling(2, 20, 127, 129)
voice(17, 1, 125, 135)
voice(11, 0, 125, 136)
# 7
Scence(imaged(3, 3), dialog(138, 154))
voice(12, 0, 138, 153)
voice(2, 1, 138, 154)
feeling(0,1,139,150)
feeling(7,1,138,141)
feeling(8, 1, 140, 154)
sounde(3, True, 140)
# 8
Scence(imaged(17, 19), dialog(156, 270))
voice(13, 0, 156, 268)
voice(3, 1, 156, 269)
voice(2, 18, 156, 270)
feeling(1, 8, 160, 270)
feeling(0, 5, 192, 195)
feeling(8, 18, 160, 270)
sounde(3, True, 160)

