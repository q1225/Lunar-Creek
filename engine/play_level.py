from pygame.sprite import RenderUpdates
from background import ts
from constants import MIDNIGHT_BLUE, WHITE,LIME_GREEN,ORANGE
from engine.Player import Player
from game_loop import game_loop
from GameState import GameState
from UIElement import UIElement
from Player import*

def play_level():
   ts(Player.current_bg)
   return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        bg_rgb=WHITE,
        text_rgb=MIDNIGHT_BLUE,
        text="Return to options",
        action=GameState.OPTIONS,
    )
   nextbackground_btn = UIElement(
            center_position=(400, 700),
            font_size=30,
            bg_rgb=WHITE,
            text_rbg=LIME_GREEN,
            text="next bg",
            action=GameState.NEXT_BACKGROUND,
            )
   next_line_btn=UIElement(
        center_postion=(700,700),
        font_size=30,
         bg_rgb=WHITE,
        text_rgb=ORANGE,
        text="next line",
        action=GameState.NEXT_LINE,
        )
   next_level_btn = UIElement(
        center_position=(500, 700),
        font_size=30,
        bg_rgb=WHITE,
        text="Next Level",
        text_rgb=MIDNIGHT_BLUE,
        action=GameState.NEXT_LEVEL,
    )

   buttons = RenderUpdates(return_btn, nextbackground_btn, next_line_btn, next_level_btn)
   return game_loop(buttons, "")
