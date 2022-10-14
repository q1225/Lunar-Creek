import pygame
from pygame.sprite import RenderUpdates

from engine.GameState import GameState
from engine.UIElement import UIElement
from engine.constants import RED, ORANGE, MIDNIGHT_BLUE, PURPLE, WHITE
from engine.game_loop import game_loop


def title_screen(background_image):
    t = UIElement(
        center_position=(300, 300),
        font_size=30,
        bg_rgb=RED,
        text_rgb=ORANGE,
        text="Lunar Creek",
    )
    options_btn = UIElement(
        center_position=(600, 500),
        font_size=30,
        bg_rgb=RED,
        text_rgb=ORANGE,
        text="Options",
        action=GameState.OPTIONS,
    )
    start_btn = UIElement(
        center_position=(600, 400),
        font_size=30,
        bg_rgb=RED,
        text_rgb=MIDNIGHT_BLUE,
        text="Start",
        action=GameState.NEW_GAME,
    )
    quit_btn = UIElement(
        center_position=(600, 600),
        font_size=30,
        bg_rgb=RED,
        text_rgb=PURPLE,
        text="Quit",
        action=GameState.QUIT,
    )
    buttons = RenderUpdates(t, start_btn, options_btn, quit_btn)
    return game_loop(buttons, background_image)


def options_screen():
    volume_btn = UIElement(
        center_position=(400, 400),
        font_size=20,
        bg_rgb=RED,
        text_rgb=MIDNIGHT_BLUE,
        text="To turn up /down volume",
    )
    save_btn = UIElement(
        center_position=(400, 500),
        font_size=20,
        bg_rgb=WHITE,
        text_rgb=MIDNIGHT_BLUE,
        text="Save game",
    )
    load_btn = UIElement(
        center_position=(400, 600),
        font_size=20,
        bg_rgb=RED,
        text_rgb=MIDNIGHT_BLUE,
        text="Load game",
        action=GameState.LOAD,
    )
    main_menu_btn = UIElement(
        center_position=(400, 700),
        font_size=20,
        bg_rgb=RED,
        text_rgb=MIDNIGHT_BLUE,
        text="main menu",
        action=GameState.TITLE,
    )
    credits_btn = UIElement(
        center_position=(400, 800),
        font_size=20,
        bg_rgb=RED,
        text_rgb=MIDNIGHT_BLUE,
        text="credits",
        action=GameState.Credits,
    )

    buttons = RenderUpdates(main_menu_btn, volume_btn, credits_btn, save_btn, load_btn)
    return game_loop(buttons, "")


def credits_screen():
    sound = pygame.mixer.load(m[2])
    channel0 = pygame.mixer.Channel(0)
    channel0.play(sound)
    channel0.stop()
    with open("Credits.docx", "r") as fl:
        lines = [line.rstrip() for line in fl]
