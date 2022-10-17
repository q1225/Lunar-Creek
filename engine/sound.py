import pygame
from main import voice_acting,sound_effects
from scence import Scence
def voice(Scence, n, x, y):
    for i in range(0, len(voice_acting)):
        sound = voice_acting[i]
    for c in range(0, n):
        channel3 = pygame.mixer.Channel(c)
        channel3.play(sound)
        pygame.mixer.Channel.stop()
        return print(lines)
    with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
      for x in range(x + n, y):
        lines = [line.rstrip() for line in fl]

        
def sounde(n, soundeffect):
    if soundeffect == True:
        sound = sound_effects[n]
        channel2 = pygame.mixer.Channel(4)
        channel2.play( sound )
        channel2.stop()
        with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
            lines = [lines.rstrip() for lines in fl]
            lines = ts1[i]
    for i in range(0, 3):
        ts1 = [44, 31, 40]
    if sounde(n, True, i == ts1[i]):
        sounde(2, True, ts1[i])
        sounde(5, True, ts1[i])
    for xs in range(4, 270):
        with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
            lines = [lines.rstrip() for lines in fl]
            lines = xs

    
    