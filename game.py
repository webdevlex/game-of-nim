import pygame
import sys
import config


def game_loop(screen):
    # "Exit Game" button setup using BODY_FONT
    exit_button_text = config.BODY_FONT.render("Exit Game", True, config.OPTION_COLOR)
    exit_button_rect = exit_button_text.get_rect(
        topright=(config.WINDOW_SIZE[0] - 20, 20)  # Top right with a margin
    )

    # Generate rows dynamically based on config.ROWS
    rows = [
        i * 2 - 1 for i in range(1, config.ROWS + 1)
    ]  # Generates [1, 3, 5, 7] for 4 rows
    object_size = 30  # Diameter of the circles representing objects
    row_spacing = 80  # Spacing between rows

    # Calculate vertical start position to center the rows
    total_height = len(rows) * row_spacing
    start_y = (config.WINDOW_SIZE[1] - total_height) // 2

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

        # Draw the "Exit Game" button with hover effect
        if exit_button_rect.collidepoint(pygame.mouse.get_pos()):
            exit_button_text = config.BODY_FONT.render(
                "Exit Game", True, config.HIGHLIGHT_COLOR
            )
        else:
            exit_button_text = config.BODY_FONT.render(
                "Exit Game", True, config.OPTION_COLOR
            )

        screen.blit(exit_button_text, exit_button_rect)

        # Draw rows of objects centered on the screen
        for row_index, num_objects in enumerate(rows):
            y_position = start_y + row_index * row_spacing  # Center vertically
            for i in range(num_objects):
                x_position = (
                    config.WINDOW_SIZE[0] // 2
                    - (num_objects - 1) * object_size
                    + i * 2 * object_size
                )  # Center horizontally
                pygame.draw.circle(
                    screen, config.OPTION_COLOR, (x_position, y_position), object_size
                )

        pygame.display.flip()
