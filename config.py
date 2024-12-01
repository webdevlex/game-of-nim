import pygame

# Initialize fonts
pygame.font.init()

# Colors
BACKGROUND_COLOR = (0, 0, 0)
TITLE_COLOR = (255, 255, 255)
OPTION_COLOR = (200, 200, 200)
HIGHLIGHT_COLOR = (16, 254, 76)

# Fonts
FONT_PATH = r".\assets\fonts\8-Bit Madness.ttf"
TITLE_FONT = pygame.font.Font(FONT_PATH, 100)  # For titles
OPTION_FONT = pygame.font.Font(FONT_PATH, 56)  # For menu options
BODY_FONT = pygame.font.Font(FONT_PATH, 36)  # Smaller font for body text

# Window settings
WINDOW_SIZE = (800, 600)

# Game settings
ROWS = 5  # Number of rows in the game

# Alpha beta purning settings
MAX_DEPTH = 4


class Players:
    PLAYER_1 = "player_1"
    PLAYER_2 = "player_2"


DEFAULT_PLAYER = Players.PLAYER_1  # Who goes first: player_1 or player_2
