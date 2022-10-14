from pygame.sprite import RenderUpdates

from constants import MIDNIGHT_BLUE, WHITE
from game_loop import game_loop
from GameState import GameState
from UIElement import UIElement


def play_level():
    return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        bg_rgb=WHITE,
        text_rgb=MIDNIGHT_BLUE,
        text="Return to options",
        action=GameState.OPTIONS,
    )

    next_level_btn = UIElement(
        center_position=(400, 400),
        font_size=30,
        bg_rgb=WHITE,
        text="Next Level",
        text_rgb=MIDNIGHT_BLUE,
        action=GameState.NEXT_LEVEL,
    )

    buttons = RenderUpdates(return_btn, next_level_btn)
    return game_loop(buttons, "")
