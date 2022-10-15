class Player:
    """Stores information about a player"""

    def __init__(self, line: int = 0, current_level: int = 0, current_bg: int = 0):
        self.current_bg = current_bg
        self.line = line
        self.current_level = current_level
