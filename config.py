import pygame

# Initialize fonts
pygame.font.init()

# Colors
BACKGROUND_COLOR = (30, 30, 30)
TITLE_COLOR = (255, 255, 255)
OPTION_COLOR = (200, 200, 200)
HIGHLIGHT_COLOR = (255, 0, 0)

# Fonts
TITLE_FONT = pygame.font.Font(None, 74)  # For titles
OPTION_FONT = pygame.font.Font(None, 56)  # For menu options
BODY_FONT = pygame.font.Font(None, 36)  # Smaller font for body text

# Window settings
WINDOW_SIZE = (800, 600)

# Game settings
ROWS = 5  # Number of rows in the game


class Players:
    PLAYER_1 = "player_1"
    PLAYER_2 = "player_2"


DEFAULT_PLAYER = Players.PLAYER_1  # Who goes first: player_1 or player_2
