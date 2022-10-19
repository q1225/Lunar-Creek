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
voice(0, 5, 4, 14)
voice(0,4, 4, 15)
feeling(1,0,0,4,6)
feeling(0, 0,0, 6, 14)
feeling(5,5,2,8, 15)
sounde(5, True, 8)
sounde(0, True, 8)
# 1
Scence(imaged(3, 3), dialog( 18,33))
feeling(0,0,0,18,22)
feeling(1,3,8,18,23)
feeling(5,0,0,22,32)
feeling(5,3,9,22,33)
sounde(8, True, 23)
voice(1, 6, 17, 33)
voice(1,13, 16, 33)
# 2
Scence(imaged(4, 6), dialog( 34, 37))
voice(2,4,34,37)
choice = input("Town Hall or Museum ?")
if choice == 1:
    # 3
    Scence(imaged(7, 9), dialog( 40, 50))
    voice(3,4,40,50)
    feeling(5,0,0,44,50)
    sounde(4, True, 44)
    sounde(5, True, 44)
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
    Scence(imaged(10, 15), dialog( 51, 74))
    sounde(2, True, 68)
    sounde(5, True, 68)
    voice(4, 4, 60, 73)
    voice(4,12, 62, 74)
    feeling(3,0,0,51,65)
    feeling(5,0,0, 66, 73)
    feeling(0,4,15,51,74)
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
Scence(imaged(16, 16), dialog( 75, 105))
voice(9,0 , 85, 114)
voice(1, 1, 85, 115)
sounde(4, True, 90)
# 114
if choice == 1 and x == 114 and "________":
    print("doll")
elif choice == 2 and x == 114 and "________":
    print("statue")
feeling(0,0,0, 75, 96)
feeling(1,2,5, 75, 98)
feeling(0,0,3, 95, 106)
feeling(6,2,4, 99, 106)
# 6
Scence(imaged(16, 16), dialog( 106, 113))
voice(6, 4, 116, 112)
voice(0,6, 116, 113)
feeling(0,7,17,119, 112)
feeling(0,6,23,117, 113)
sounde(3, True, 109)
for p in range(0, 9):
    channel1 = pygame.mixer.Channel(p + 1)
    pygame.mixer.Channel.play()
    pygame.mixer.Channel.stop()
    voice(19, 2, 110, 113)
    
    feeling(0,0,0,108, 113)
    
    sounde(3, True, 127)
# 6_5
Scence(imaged(16, 16), dialog( 115, 126))
feeling (0,0,0,115,126)
feeling(6,3,9,115,116)
feeling(5,3,9,117, 119)
feeling (0,3,10,120,126)
voice(7,3, 115, 125)
voice(7,8, 115, 126)
# 7
Scence(imaged(3, 3), dialog(128, 144))
voice(8, 0, 128, 143)
voice(0,0, 128, 144)
feeling(0,1,129,140)
feeling(7,1,128,131)
feeling(8, 1, 130, 144)
sounde(3, True, 130)
# 8
Scence(imaged(17, 19), dialog(146, 260))
voice(9,3 , 146, 258)
voice(0,1, 146, 259)
voice(9,9, 146, 260)
feeling(0,0,0, 160, 260)
feeling(1,1,6,182, 185)
feeling(0,8,18, 150, 260)
feeling(5,0,0, 160, 260)
feeling(0,1,5, 182, 185)
feeling(0,8,18, 150, 260)
feeling(6,0,0, 185, 260)
sounde(3, True, 150)

