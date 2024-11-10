import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Game Of Nim")

# Colors
background_color = (30, 30, 30)  # Dark grey
title_color = (255, 255, 255)  # White
option_color = (200, 200, 200)  # Light grey
highlight_color = (255, 0, 0)  # Red for hover

# Font settings
title_font = pygame.font.Font(None, 74)
option_font = pygame.font.Font(None, 56)

# Menu options
menu_options = ["New Game", "Settings", "Exit"]
menu_rects = []  # Initialize outside to avoid adding multiple times

# Pre-calculate menu option rectangles once
for index, option in enumerate(menu_options):
    option_text = option_font.render(option, True, option_color)
    option_rect = option_text.get_rect(center=(window_size[0] // 2, 300 + index * 60))
    menu_rects.append(option_rect)


# Define a function to draw the menu
def draw_menu():
    screen.fill(background_color)

    # Draw the title
    title_text = title_font.render("Game Of Nim", True, title_color)
    title_rect = title_text.get_rect(center=(window_size[0] // 2, 150))
    screen.blit(title_text, title_rect)

    # Draw the options
    for index, option in enumerate(menu_options):
        option_text = option_font.render(option, True, option_color)
        option_rect = menu_rects[index]

        # Check if the mouse is over the option
        if option_rect.collidepoint(pygame.mouse.get_pos()):
            option_text = option_font.render(option, True, highlight_color)
        screen.blit(option_text, option_rect)

    pygame.display.flip()


# Game loop function with an "Exit Game" button
def game_loop():
    exit_button_text = option_font.render("Exit Game", True, option_color)
    exit_button_rect = exit_button_text.get_rect(center=(window_size[0] // 2, 500))

    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the exit button is clicked
                if exit_button_rect.collidepoint(event.pos):
                    print("Exiting game...")
                    running = False  # Exit the game loop and return to the main menu

        # Draw game state
        screen.fill(background_color)

        # Draw the "Exit Game" button
        if exit_button_rect.collidepoint(pygame.mouse.get_pos()):
            exit_button_text = option_font.render("Exit Game", True, highlight_color)
        else:
            exit_button_text = option_font.render("Exit Game", True, option_color)

        screen.blit(exit_button_text, exit_button_rect)

        pygame.display.flip()


# Main loop
running = True
in_menu = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and in_menu:
            # Check which menu option is clicked
            for index, option_rect in enumerate(menu_rects):
                if option_rect.collidepoint(event.pos):
                    if menu_options[index] == "New Game":
                        print("Starting a new game...")
                        in_menu = False
                        game_loop()  # Start the game loop
                        in_menu = True  # Return to menu after the game
                    elif menu_options[index] == "Settings":
                        print("Opening settings...")
                        # Add settings handling here
                    elif menu_options[index] == "Exit":
                        running = False

    # Draw the menu if we're in the menu screen
    if in_menu:
        draw_menu()

# Quit Pygame
pygame.quit()
sys.exit()
