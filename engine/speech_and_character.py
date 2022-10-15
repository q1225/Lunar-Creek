
from ast import While
import pygame
from engine.GameState import GameState
from engine.constants import GAME_DISPLAY 
from main import character_images
from pygame.sprite import LayeredUpdates
from main_add import *
def dialogue (n,x,y):
     with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
         lines = [lines.rstrip() for lines in fl]
         x=lines
     while(x<y):
       textOutput(x)
       GAME_DISPLAY.blit(textTitle(500, 700))
       x+=1

def feeling(f, ch,n, x, y):
        # n==1 fannie f==cp==0-5
        # n==2 bea f==cp==6-11
        # n==3 innkeeper f==cp==13-19
        # n==4 musuem guide f==cp== 20
        # n==5 boss f==cp==12
        # n==6  f==cp==
      while (x<y): 
       for i in range (0,n):
        if (i%2!=0):
         for a in range(0, f):
            if f != 0:
             for n in range (1,n):
              image=(character_images[ch+i+a])
              X += 100
              LayeredUpdates.move_to_front()
              pygame.time.set_timer(5000)
             GAME_DISPLAY.blit(image, (X, 200))
                
        else: 
            LayeredUpdates.move_to_front()
            pygame.time.set_timer(5000)
            image=(character_images[ch+i+a])
            GAME_DISPLAY.blit(image(700, 400))
              # minor characters
        if ch == 5:
         sc = [127, 129]
        with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
            for x2 in range(0, len(sc)):
                lines = [lines.rstrip() for lines in fl]
                lines=sc[x2]
                return print(lines)
        if ch == 6:
         sc1= [128, 130]
         with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
            for x3 in range(0, len(sc1)):
                lines = [lines.rstrip() for lines in fl]
                lines=sc1[x3]
                return print(lines)
        if ch == 7:
         sc2 = [241, 243, 245, 247]
         with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
            for x4 in range(0, len(sc2)):
                lines = [lines.rstrip() for lines in fl]
                lines= sc2[x4]
                return print(lines)
        if ch == 8:
         sc3= [260, 264]
         with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
            for x5 in range(0, len(sc3)):
                lines = [lines.rstrip() for lines in fl]
                lines= sc3[x5]
            return print(lines)
