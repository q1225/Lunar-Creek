import os

import pygame
import pygame.freetype
import pygame.mixer
from pygame.sprite import RenderUpdates, Sprite

from engine.constants import ORANGE, GAME_DISPLAY, WHITE


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


def dialog(n, x2, y2):
    with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
        speech = textOutput(line)
    for x in range(x + n, y, +2):
        lines = [line.rstrip() for line in fl]
    if n % 2 != 0:
        pygame.image.load(C[ch])
        X = 700
        Y = 400
        move_to_front()
        pygame.time.set_timer(5000)
        display_surface.blit(image, (0, 0))
        sound = pygame.mixer.load(vc[ch[i]])
        channel3 = pygame.mixer.Channel(n)
        pygame.mixer.Channel.play()
        pygame.mixer.Channel.stop()
        return print(lines)
        with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
            speech = textOutput(line)
            for x1 in range(x1 + 1, y1, +2):
                line = [line.rstrip() for line in fl]
    else:
        pygame.image.load(C[ch + 1])
        X += 100
        Y = 400
        move_to_front()
        pygame.time.set_timer(5000)
        display_surface.blit(image, (0, 0))
        sound = pygame.mixer.load(vc[ch[i]])
        channel3 = pygame.mixer.Channel(n)
        pygame.mixer.Channel.play()
        pygame.mixer.Channel.stop()
        return print(line)
        with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
            speech = textOutput(line)
            for x1 in range(x1 + 1, y1, +2):
                line = [line.rstrip() for line in fl]

    def feeling(f, ch, x1, y1):
        # n==1 fannie f==cp==0-5
        # n==2 bea f==cp==6-11
        # n==3 innkeeper f==cp==13-19
        # n==4 musuem guide f==cp== 20
        # n==5 boss f==cp==12
        # n==6  f==cp==
        for a in range(0, f):
            if f != 0:
                pygame.image.load(C[ch + f])
            if n % 2 != 0:
                X += 100
                Y = 200
                move_to_front()
                pygame.time.set_timer(5000)
                display_surface.blit(image, (0, 0))
                sound = pygame.mixer.load(vc[i])
            else:
                X = 700
                Y = 200
                move_to_front()
                pygame.time.set_timer(5000)
                display_surface.blit(image, (0, 0))


def voice(scence, n, x, y):
    scence = vc
    for i in range(0, len(vc)):
        sound = pygame.mixer.load(vc[i])
    for c in range(0, n):
        channel3 = pygame.mixer.Channel(c)
        pygame.mixer.Channel.play()
        pygame.mixer.Channel.stop()
        return print(lines)
    with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
        speech = create_surface_with_text(
            "Cult_of_Seal_VN_lines Final.docx", 32, ORANGE, MB
        )
    for x in range(x + n, y, +2):
        lines = [line.rstrip() for line in fl]
    else:
        pygame.image.load(C[ch + 1])
        X += 100
        Y = 400
        move_to_front()
        pygame.time.set_timer(5000)
        display_surface.blit(image, (0, 0))
        sound = pygame.mixer.load(vc[ch[i]])
        channel3 = pygame.mixer.Channel(n)
        pygame.mixer.Channel.play()
        pygame.mixer.Channel.stop()
        return print(lines)
    with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
        speech = create_surface_with_text(
            "Cult_of_Seal_VN_lines_Final.docx", 32, ORANGE, MB
        )
    for x1 in range(x1 + 1, y1, +2):
        lines = [line.rstrip() for line in fl]

    for cp in range(0, n):
        ch = input("who")
        f = input("How is the charater feeling")
        feeling(f, ch, x, y)
        # minor characters
    if ch == 5:
        sc = [127, 129]
        return print(lines)
        with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
            for x2 in range(0, len(sc1)):
                lines = [line.rstrip() for line in fl]
    if ch == 6:
        sc1 = [128, 130]
        return print(lines)
        with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
            for x3 in range(0, len(sc2)):
                lines = [line.rstrip() for line in fl]
    if ch == 7:
        sc = [241, 243, 245, 247]
        return print(lines)
        with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
            for x4 in range(0, len(sc3)):
                lines = [line.rstrip() for line in fl]
    if ch == 8:
        sc = [260, 264]
        return print(lines)
        with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
            for x2 in range(0, len(sc4)):
                lines = [line.rstrip() for line in fl]


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


def seal():
    for k in range(0, 3):
        seal = [17, 104, 128]
    with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
        lines = seal[k]
    if x == seal[k]:
        screen = display_surface
        GAME_DISPLAY.fill(WHITE)
        pygame.image.load(C[25])
        X = 400
        Y = 400
        display_surface.blit(image, (0, 0))
        move_to_front()


def ts(x):
    for l in range(0, 13):
        ts = [4, 31, 40, 57, 61, 62, 68, 85, 89, 91, 137, 152, 154, 177]
    with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
        lines = ts[l]
    if x < 20:
        screen = display_surface
        GAME_DISPLAY.fill(WHITE)
        nextlevel_btn = UIElement(
            center_position=(400, 400),
            font_size=30,
            bg_rgb=WHITE,
            image=pygame.image.load(FBG[x]),
            action=Gamewstate.NEXT_LEVEL,
        )
        buttons = RenderUpdates(nextlevel_btn)
        return game_loop(GAME_DISPLAY, buttons)
        X = 800
        Y = 600
        display_surface.blit(image, (0, 0))
        self.soundb = pygame.mixer.load(m[1])
        channel1 = pygame.mixer.Channel(0)
        pygame.mixer.Channel.play()
        pygame.mixer.Channel.stop()


def sounde(n, soundeffect, x4):
    if soundeffect == True:
        self.sound = pygame.mixer.load(SE[n])
        channel2 = pygame.mixer.Channel(4)
        pygame.mixer.Channel.play()
        pygame.mixer.Channel.stop()
        with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
            lines = ts1[i]
    for i in range(0, 3):
        ts1 = [44, 31, 40]
    if sounde(n, True, x == ts1[i]):
        sounde(2, True, ts1[i])
        sounde(5, True, ts1[i])
    for xs in range(4, 270):
        with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
            lines = xs
    self.sound = pygame.mixer.load(m(1))
    channel1 = pygame.mixer.Channel(0)
    pygame.mixer.Channel.play()
    pygamee.mixer.Channel.stop()
    self.dialogue = dialog(n, x, y)


def notebook(scence):
    if scence == 4:
        pygame.time.set_timer(5000)
        gamestate.notebook
        pygame.display.text("News is different on the island")
        pygame.time.set_timer(3000)


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
vioce(1, 1, 85, 115)
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
Scence.Scence(image(17, 19), dialog(3, 156, 270))
voice(13, 0, 156, 268)
voice(3, 1, 156, 269)
voice(18, 2, 156, 270)
feeling(8, 1, 160, 270)
feeling(5, 0, 192, 195)
feeling(18, 8, 160, 270)
sounde(3, True, 160)


def save_btn(self, data, name):
    data_file = open(self.save_folder + "/" + name + self.file_extension, "wb")
    pickle.dump(data, data_file)
    return os.path.exists(self.save_folder + "/" + name + self.file_extension)
    if len(variables) > 1:
        return tuple(variables)
    else:
        return variables[0]
    for index, file in enumerate(data_to_save):
        self.save_data(file, file_names[index])


def load_btn(self, name):
    data_file = open(self.save_folder + "/" + name + self.file_extension, "rb")
    data = pickle.load(data_file)
    return data
    variables = []
    for index, file in enumerate(files_to_load):
        if self.check_for_file(file):
            variables.append(self.load_data(file))
        else:
            variables.append(default_data[index])
        if len(variables) > 1:
            return tuple(variables)
        else:
            return variables[0]


def volume_btn():
    mixer.init()
    mixer.music.load(M)
    mixer.music.set_volume(input("volume? 0-.1.0"))
    mixer.music.play()
