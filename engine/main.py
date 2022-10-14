import os
from typing import Iterable

import pygame

from constants import ROOT
from GameState import GameState
from play_level import play_level
from Player import Player
from screens import credits_screen, options_screen, title_screen


def create_media_array(media_folder: str, valid_extensions: Iterable[str]) -> list[str]:
    return [
        os.path.join(ROOT, media_folder, file)
        for file in os.listdir(os.path.join(ROOT, media_folder))
        if os.path.splitext(file)[1].lower() in valid_extensions
    ]


def main():
    background_images = create_media_array("background_images", (".jpg", ".png"))
    background_music = create_media_array("background_music", (".wav",))
    sound_effects = create_media_array("sound_effects", (".wav",))
    character_images = create_media_array("character_images", (".jpg", ".png"))
    voice_acting = create_media_array("voice_acting", (".wav",))

    file = "Cult_of_Seal_VN_lines_Final.txt"

    pygame.init()

    game_state = GameState.TITLE
    pygame.display.set_caption("Lunar Creek")

    while True:
        if game_state == GameState.TITLE:
            game_state = title_screen(background_images[0])
        elif game_state == GameState.OPTIONS:
            game_state = options_screen()
        elif game_state == GameState.Credits:
            game_state = credits_screen()
        elif game_state == GameState.NEW_GAME:
            player = Player()
            game_state = play_level()
        elif game_state == GameState.NEXT_LEVEL:
            # noinspection PyUnboundLocalVariable
            player.current_level += 1
            game_state = play_level()

        elif game_state == GameState.QUIT:
            pygame.quit()
            return


if __name__ == "__main__":
    main()
