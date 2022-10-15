import pygame

from GameState import GameState


def notebook(scene):
    if scene == 4:
        pygame.time.set_timer(5000)
        GameState.NOTEBOOK
        pygame.display.text("News is different on the island")
        pygame.time.set_timer(3000)


def volume_btn(background_music: str):
    pygame.mixer.init()
    pygame.mixer.music.load(background_music)
    pygame.mixer.music.set_volume(float(input("volume? 0.0 - 1.0")))
    pygame.mixer.music.play()
