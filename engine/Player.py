class Player:
    """Stores information about a player"""

    def __init__(self, score: int = 0, current_level: int = 1):
        self.score = score
        self.current_level = current_level
