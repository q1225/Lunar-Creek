from email.errors import InvalidMultipartContentTransferEncodingDefect
from re import X
import pygame
from constants import WHITE,LIME_GREEN,RED
from UIElement import*
from pygame.sprite import RenderUpdates,LayeredUpdates
from main import background_images,background_music,chacter_imaages 
from game_loop import*
from GameState import*
from main_add import*
X=800
Y=600
display_surface=(pygame.display.setmode(X,Y)) 
def ts(x):
   for l in range(0, len(ts)):
        ts = [4, 6,17,31, 40,44, 50,57, 61, 62, 68, 85, 89, 91, 117,137, 152, 154,156, 177]
   with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
         lines = [lines.rstrip() for lines in fl]
   if  lines == ts[l]:
      for x in range (1,len(imaged())):
       x=l
       soundb =(background_music[1])
       channel1 = pygame.mixer.Channel(0)
       channel1.play(soundb)
       image=background_images[x], 
       display_surface.fill(WHITE)
       display_surface .blit(image, (0, 0))
def new_scence(s): 
       for x in range (0,len(sc)):
        s=x
        sc=[4,7,40,50,61,85,116,125,138,156]
        with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
            lines = [lines.rstrip() for lines in fl]
        if lines ==sc[x]:
            nextlevel_btn = UIElement(
             center_position=(400, 700),
             font_size=30,
             bg_rgb=WHITE,
             text_rgb=RED,
             action=GameState.NEXT_Level,
            )
       buttons = RenderUpdates(nextlevel_btn)
       return game_loop(display_surface, buttons)
def seal():
    for k in range(0, 3):
        seal = [17, 104, 128]
    with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
       lines = [lines.rstrip() for lines in fl]
       if lines == seal[k]:
        image = display_surface
        image=(chacter_imaages[25])
        display_surface.blit(image (400, 400))
        LayeredUpdates.move_to_front