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

    # Initialize selection and turn state
    selected_items = {i: [] for i in range(len(rows))}  # Tracks selected items per row
    current_row = None  # Row being interacted with
    mouse_down = False
    selection_made = False  # Tracks if a selection has been made
    current_player = config.DEFAULT_PLAYER  # Tracks whose turn it is

    # Play button setup
    play_button_text = config.BODY_FONT.render("Play", True, config.OPTION_COLOR)
    play_button_rect = play_button_text.get_rect(
        center=(config.WINDOW_SIZE[0] // 2, config.WINDOW_SIZE[1] - 50)
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
                elif play_button_rect.collidepoint(event.pos) and selection_made:
                    # Print the row and count of selected items
                    for row, items in selected_items.items():
                        if items:  # Only print rows with selections
                            print(
                                (row, len(items))
                            )  # Row index and count of selected items
                else:
                    # Start selecting items, clear previous selections
                    mouse_down = True
                    selected_items = {
                        i: [] for i in range(len(rows))
                    }  # Clear selections
                    selection_made = False  # Reset selection state
            elif event.type == pygame.MOUSEBUTTONUP:
                # Save selected items
                mouse_down = False
                current_row = None  # Reset row lock after selection is done
                if any(selected_items[row] for row in selected_items):
                    selection_made = True  # Mark selection as made

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
        mouse_pos = pygame.mouse.get_pos()
        for row_index, num_objects in enumerate(rows):
            y_position = start_y + row_index * row_spacing  # Center vertically
            for i in range(num_objects):
                x_position = (
                    config.WINDOW_SIZE[0] // 2
                    - (num_objects - 1) * object_size
                    + i * 2 * object_size
                )  # Center horizontally

                # Check if the mouse is over this object
                distance = (
                    (mouse_pos[0] - x_position) ** 2 + (mouse_pos[1] - y_position) ** 2
                ) ** 0.5
                is_hovered = distance <= object_size

                # Determine color based on selection state
                if i in selected_items[row_index]:
                    color = config.HIGHLIGHT_COLOR  # Selected items
                elif (
                    mouse_down
                    and is_hovered
                    and (current_row is None or current_row == row_index)
                ):
                    color = config.HIGHLIGHT_COLOR  # Currently hovered during selection
                    current_row = row_index  # Lock to this row
                    if i not in selected_items[row_index]:
                        selected_items[row_index].append(i)  # Add to selection
                else:
                    color = config.OPTION_COLOR  # Default color

                pygame.draw.circle(screen, color, (x_position, y_position), object_size)

        # Draw Player Indicators
        player_1_color = (
            config.HIGHLIGHT_COLOR
            if current_player == config.Players.PLAYER_1
            else config.OPTION_COLOR
        )
        player_2_color = (
            config.HIGHLIGHT_COLOR
            if current_player == config.Players.PLAYER_2
            else config.OPTION_COLOR
        )

        player_1_text = config.BODY_FONT.render("Human", True, player_1_color)
        player_1_rect = player_1_text.get_rect(topleft=(20, config.WINDOW_SIZE[1] - 50))
        screen.blit(player_1_text, player_1_rect)

        player_2_text = config.BODY_FONT.render("Bot", True, player_2_color)
        player_2_rect = player_2_text.get_rect(
            topright=(config.WINDOW_SIZE[0] - 20, config.WINDOW_SIZE[1] - 50)
        )
        screen.blit(player_2_text, player_2_rect)

        # Draw Play Button if selection is made
        if selection_made:
            if play_button_rect.collidepoint(mouse_pos):
                play_button_text = config.BODY_FONT.render(
                    "Play", True, config.HIGHLIGHT_COLOR
                )
            else:
                play_button_text = config.BODY_FONT.render(
                    "Play", True, config.OPTION_COLOR
                )
            screen.blit(play_button_text, play_button_rect)

        pygame.display.flip()
