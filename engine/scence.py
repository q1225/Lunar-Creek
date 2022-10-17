import pygame
from pygame.sprite import*
from main import WHITE,background_images,background_music,GAME_DISPLAY
from background import ts 
from main_add import textOutput,textTitle
class Scence(Sprite):  
 def Scence(imaged,dialog):
        """
        Args:
         image - list (b[])
         sound-list (bm[])
         sounde-list(SE[])
         dialogue (txt) -list dialog ([n,x,y])
        """
def dialog(x,y):
     with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
         lines = [lines.rstrip() for lines in fl]
         x=lines
     while(x<y):
       textOutput(x)
       GAME_DISPLAY.blit(textTitle(500, 700))
       x+=1
def imaged(x, y):
     for i in range(0, len(background_images)):
        ts(i)
        for x in range(x, y):
            image=(background_images[x])
            GAME_DISPLAY.fill(WHITE)
            GAME_DISPLAY.blit(image (0, 0))
            sound = pygame.mixer.load(background_music[1])
            channel1 = pygame.mixer.Channel(0)
            channel1.play(sound)
            channel1.stop()
