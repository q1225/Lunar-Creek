from enum import Enum
import pygame.mixer
import gypsy cuse.ttf
import pygame
import pygame.freetype
from pygame.rect import Rect
from pygame.sprite import RenderUpdates, Sprite
white = (255, 255, 255)
Orange = [255, 165, 0]
Red = [255, 0, 0]
Purple = [159, 43, 104]
MB = [199, 9, 70]
#C=pygame.surfarray.array2d():
B=pygame.surfarray.array2d():[D:/lunar creek/IMG_1535.jpg,]
M=pygame.surfarray.array2d():[D:/lunar creek/music1.zip,]
#def dilogue():
#class Scence ():
def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """Returns surface with text written on"""
    font = pygame.freetype.SysFont("GYPSY CRUSE", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()
def volume_btn ():
    mixer.init()
    mixer.music.load(M)
    mixer.music.set_volume(input("volume? 0-.1.0"))
    mixer.music.play()
class UIElement(Sprite):
    """A user interface element that can be added to a surface"""

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
        """
        Args:
            center_position - tuple (x, y)
            text - string of text to write
            font_size - int
            bg_rgb (background colour) - tuple (r, g, b)
            text_rgb (text colour) - tuple (r, g, b)
            action - the gamestate change associated with this button
        """
        self.mouse_over = False

        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        self.images = [default_image, highlighted_image]

        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        self.action = action

        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        """Updates the element's appearance depending on the mouse position
        and returns the button's action if clicked.
        """
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """Draws element onto a surface"""
        surface.blit(self.image, self.rect)

        # def __init__(self, center_position, text, font_size, text_rgb, action=None):
        #     self.action = action


class Player:
    """Stores information about a player"""

    def __init__(self, score=0, current_level=1):
        self.score = score
        self.current_level = current_level

image = pygame.image.load(r'D:/Lunar Creek/IMG_1535.JPG')
def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    game_state = GameState.TITLE
    pygame.display.set_caption("Lunar Creek")

    while True:
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)
        elif game_state == GameState.Options:
            game_state = opotions_screen(screen)
        
        elif game_state == GameState.NEW_GAME:
            player = Player()
            game_state = play_level(screen, player)

        elif game_state == GameState.NEXT_LEVEL:
            player.current_level += 1
            game_state = play_level(screen, player)

        elif game_state == GameState.QUIT:
            pygame.quit()
            return


def title_screen(screen):
 t = UIElement(
        center_position=(300, 300),
        font_size=30,
        bg_rgb=Red,
        text_rgb=Orange,
        text="Lunar Creek",
        )
    options_but = UIElement(
        center_position=(600, 500),
        font_size=30,
        bg_rgb=Red,
        text_rgb=Orange,
        text="Options",
        action=GameState.OPTIONS,
        )
    start_btn = UIElement(
        center_position=(600, 400),
        font_size=30,
        bg_rgb=Red,
        text_rgb=MB,
        text="Start",
        action=GameState.NEW_GAME,
        )
    quit_btn = UIElement(
        center_position=(600, 600),
        font_size=30,
        bg_rgb=Red,
        text_rgb=Purple,
        text="Quit",
        action=GameState.QUIT,
    )

    buttons = RenderUpdates(t,start_btn,option_butt, quit_btn)

    return game_loop(screen, buttons)
def options_screen(screen):
      volume_btn=UIElement(
        center_position=(400, 400),
        font_size=20,
        bg_rgb=Red,
        text_rgb=MB,
        text="To turn up /down volume",
        )
      Save_btn=UIElement(
        center_position=(400,500),
        font_size=20,
        bg_rgb=white,
        text_rgb=MB,
        text="Save game",
        )
      Load_btn=UIElement(
        center_position=(400, 600),
        font_size=20,
        bg_rgb=Red,
        text_rgb=MB,
        text="Load game",
       action=GameState.LOAD,
        )
    MM_btn=UIElement(
        center_position=(400,700),
        font_size=20,
        bg_rgb=Red,
        text_rgb=MB,
        text="main menu",
       action=GameState.TITLE,
        )
    buttons = RenderUpdates(MM_btn,volume_btn, save_btn,load_btn)

    return game_loop(screen, buttons)
def play_level(screen, player):
    return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        bg_rgb=white,
        text_rgb=MB,
        text="Return to options",
        action=GameState.OPTIONS,
    )
    )
    nextlevel_btn = UIElement(
        center_position=(400, 400),
        font_size=30,
        bg_rgb=white,
        text_rgb=Orange,
        text=f"Next level ({player.current_level + 1})",
        action=GameState.NEXT_LEVEL,
    )

    buttons = RenderUpdates(return_btn, nextlevel_btn)

    return game_loop(screen, buttons)
X = 400
Y = 400

def game_loop(screen, buttons):
    """Handles game loop until an action is return by a button in the
    buttons sprite renderer.
    """
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
                screen.fill(white)
                  display_surface.blit(image, (0, 0)) 
        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
             return ui_action
        buttons.draw(screen)
        pygame.display.flip()
        print("Press 'p' to pause, 'r' to resume")
        print("Press 'e' to exit the program")
        query = input("  ")
      
        if query == 'p':
  
        # Pausing the music
           mixer.music.pause()     
        elif query == 'r':
  
        # Resuming the music
            mixer.music.unpause()
        elif query == 'e':
  
        # Stop the mixer
         mixer.music.stop()
        break
    # buttons = RenderUpdates(return_btn, nextlevel_btn)

    # return game_loop(screen, buttons)


class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEW_GAME = 1
    NEXT_LEVEL = 2
    OPTIONS=3
    Notebook=4
if __name__ == "__main__":
    main()
