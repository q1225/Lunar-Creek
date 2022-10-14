from enum import Enum


class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEW_GAME = 1
    NEXT_LEVEL = 2
    NEXT_BACKGROUND = 7
    NEXT_LINE = 8
    OPTIONS = 3
    Notebook = 4
    Credits = 5
    LOAD = 6
