import pygame
import sys
import config


def game_loop(screen):
    exit_button_text = config.OPTION_FONT.render("Exit Game", True, config.OPTION_COLOR)
    exit_button_rect = exit_button_text.get_rect(
        center=(config.WINDOW_SIZE[0] // 2, 500)
    )

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
        screen.fill(config.BACKGROUND_COLOR)

        # Draw the "Exit Game" button
        if exit_button_rect.collidepoint(pygame.mouse.get_pos()):
            exit_button_text = config.OPTION_FONT.render(
                "Exit Game", True, config.HIGHLIGHT_COLOR
            )
        else:
            exit_button_text = config.OPTION_FONT.render(
                "Exit Game", True, config.OPTION_COLOR
            )

        screen.blit(exit_button_text, exit_button_rect)
        pygame.display.flip()
