from string import whitespace
from tkinter import image_names


def ts(x):
    for l in range(0, len(ts)):
        ts = [4, 6,17,31, 40,44, 50,57, 61, 62, 68, 85, 89, 91, 117,137, 152, 154,156, 177]
    with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
        lines = ts[l]
    if x < 20:
       X = 800
       Y = 600
       soundb = pygame.mixer.load(m[1])
       channel1 = pygame.mixer.Channel(0)
       channel1.play()
       image=background_image[x], 
       display_surface.fill(WHITE)
       display_surface .blit(image, (0, 0))
       nextbackground_btn = UIElement(
            center_position=(400, 700),
            font_size=30,
            bg_rgb=WHITE,
            text_rbg=green
            action=Gamestate.NEXT_Scence,
            )
       buttons = RenderUpdates(nextbackground_btn)
       return game_loop(display_surface, buttons)
def new_scence(s): 
       for x in range (0,len(sc)):
        s=x
        sc=[4,7,40,50,61,85,116,125,138,156]
        with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
            lines = [lines.rstrip() for lines in fl]
        if lines ==sc[x]:
            nextbackground_btn = UIElement(
             center_position=(400, 700),
             font_size=30,
             bg_rgb=white,
             text_rgb=red,
             action=Gamestate.NEXT_Level,
            )
       buttons = RenderUpdates(nextbackground_btn)
       return game_loop(display_surface, buttons)
def seal():
    for k in range(0, 3):
        seal = [17, 104, 128]
    with open("Cult_of_Seal_VN_lines_Final.docx", "r") as fl:
        lines = seal[k]
    if x == seal[k]:
        screen = display_surface
        GAME_DISPLAY.fill(WHITE)
        pygame.image.load(C[25])
        display_surface.blit(image, (400, 400))
        Layerdmove_to_front()