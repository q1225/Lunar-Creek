import pygame
from pygame.sprite import RenderUpdates

from engine.constants import WHITE, GAME_DISPLAY


def game_loop(buttons: RenderUpdates, image_path: str) -> None:
    """Handles game loop until an action is return by a button in the
    buttons sprite renderer.
    """
    image = pygame.image.load(image_path)

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        GAME_DISPLAY.fill(WHITE)
        GAME_DISPLAY.blit(image, (0, 0))
        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
        buttons.draw(GAME_DISPLAY)
        pygame.display.flip()
        pygame.mixer.music.stop()
        break
