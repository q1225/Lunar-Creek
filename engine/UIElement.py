from typing import Optional

import pygame
from pygame.sprite import Sprite

from GameState import GameState
from constants import GAME_DISPLAY


def create_surface_with_text(
    text: str,
    font_size: float,
    text_rgb: tuple[int, int, int],
    bg_rgb: tuple[int, int, int],
):
    """Returns surface with text written on"""
    font = pygame.freetype.SysFont("GYPSY CRUSE", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


class UIElement(Sprite):
    """A user interface element that can be added to a surface"""

    def __init__(
        self,
        center_position: tuple[int, int],
        text: str,
        font_size: float,
        bg_rgb: tuple[int, int, int],
        text_rgb: tuple[int, int, int],
        action: Optional[GameState] = None,
    ):
        """
        Args:
         center_position - tuple (x, y)
         text - string of text to write
         font_size - int
         bg_rgb (background colour) - tuple (r, g, b)
         text_rgb (text colour) - tuple (r, g, b)
         action - the game state change associated with this button
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

    def update(self, mouse_pos: tuple[int, int], mouse_up: bool):
        """Updates the element's appearance depending on the mouse position
        and returns the button's action if clicked.
        """
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self):
        """Draws element onto a surface"""
        GAME_DISPLAY.blit(self.image, self.rect)
