import pygame
import sys
from menu import draw_menu, handle_menu_events
from game import game_loop
import config

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode(config.WINDOW_SIZE)
pygame.display.set_caption("Game Of Nim")


# Main loop
def main():
    running = True
    in_menu = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and in_menu:
                option_selected = handle_menu_events(event.pos, screen)
                if option_selected == "New Game":
                    in_menu = False
                    game_loop(screen)  # Start the game loop
                    in_menu = True  # Return to menu after the game
                elif option_selected == "Settings":
                    print("Settings are not implemented yet.")
                elif option_selected == "Exit":
                    running = False

        # Draw the menu if we're in the menu screen
        if in_menu:
            draw_menu(screen)

    # Quit Pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
