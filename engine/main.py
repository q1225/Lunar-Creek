import pygame
from GameState import GameState
from media import background_images, background_music
from play_level import play_level
from Player import Player
from screens import credits_screen, options_screen, title_screen


def main():
    pygame.init()

    game_state = GameState.TITLE
    pygame.display.set_caption("Lunar Creek")

    while True:
        if game_state == GameState.TITLE:
            title_screen(background_images[0])
        elif game_state == GameState.OPTIONS:
            options_screen()
        elif game_state == GameState.Credits:
            credits_screen(background_music[0])
        elif game_state == GameState.NEW_GAME:
            player = Player()
            play_level()
        elif game_state == GameState.NEXT_LEVEL:
            # noinspection PyUnboundLocalVariable
            player.current_level += 1
            play_level()
        elif game_state == GameState.NEXT_BACKGROUND:
            player.current_bg += 1
            play_level()
        elif game_state == GameState.NEXT_LINE:
            player.line += 1
            play_level()
        elif game_state == GameState.QUIT:
            pygame.quit()
            return


if __name__ == "__main__":
    main()
