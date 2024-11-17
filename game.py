import pygame
import sys
import config


def game_loop(screen):
    # "Exit Game" button setup using BODY_FONT
    exit_button_text = config.BODY_FONT.render("Exit Game", True, config.OPTION_COLOR)
    exit_button_rect = exit_button_text.get_rect(
        topright=(config.WINDOW_SIZE[0] - 20, 20)
    )

    # Initialize game variables
    def reset_game():
        nonlocal rows, selected_items, current_row, mouse_down, selection_made
        nonlocal current_player, game_over, winner
        rows = [i * 2 - 1 for i in range(1, config.ROWS + 1)]
        selected_items = {i: [] for i in range(len(rows))}
        current_row = None
        mouse_down = False
        selection_made = False
        current_player = config.DEFAULT_PLAYER
        game_over = False
        winner = None
        return (
            rows,
            selected_items,
            current_row,
            mouse_down,
            selection_made,
            current_player,
            game_over,
            winner,
        )

    (
        rows,
        selected_items,
        current_row,
        mouse_down,
        selection_made,
        current_player,
        game_over,
        winner,
    ) = reset_game()

    # Button setups
    play_button_text = config.BODY_FONT.render("Play", True, config.OPTION_COLOR)
    play_button_rect = play_button_text.get_rect(
        center=(config.WINDOW_SIZE[0] // 2, config.WINDOW_SIZE[1] - 50)
    )

    replay_button_text = config.BODY_FONT.render("Replay", True, config.OPTION_COLOR)
    replay_button_rect = replay_button_text.get_rect(
        center=(config.WINDOW_SIZE[0] // 2, config.WINDOW_SIZE[1] - 50)
    )

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
                mouse_pos = event.pos
                if exit_button_rect.collidepoint(mouse_pos):
                    print("Exiting game...")
                    running = False
                elif game_over and replay_button_rect.collidepoint(mouse_pos):
                    # Reset the game
                    (
                        rows,
                        selected_items,
                        current_row,
                        mouse_down,
                        selection_made,
                        current_player,
                        game_over,
                        winner,
                    ) = reset_game()
                elif not game_over:
                    if play_button_rect.collidepoint(mouse_pos) and selection_made:
                        # Remove selected items from the row
                        for row, items in selected_items.items():
                            if items:
                                rows[row] -= len(items)
                                print(f"Removed {len(items)} items from row {row}.")
                                break
                        # Check for game over
                        if sum(rows) == 1:  # Only 1 item left
                            game_over = True
                            winner = (
                                "Human"
                                if current_player == config.Players.PLAYER_1
                                else "Bot"
                            )
                        else:
                            # Switch players
                            current_player = (
                                config.Players.PLAYER_2
                                if current_player == config.Players.PLAYER_1
                                else config.Players.PLAYER_1
                            )
                        # Reset selection
                        selected_items = {i: [] for i in range(len(rows))}
                        selection_made = False
                    else:
                        # Start selecting items
                        mouse_down = True
                        selected_items = {i: [] for i in range(len(rows))}
                        selection_made = False
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False
                current_row = None
                if any(selected_items[row] for row in selected_items):
                    selection_made = True

        # Draw game state
        screen.fill(config.BACKGROUND_COLOR)

        # Draw the "Exit Game" button
        if exit_button_rect.collidepoint(pygame.mouse.get_pos()):
            exit_button_text = config.BODY_FONT.render(
                "Exit Game", True, config.HIGHLIGHT_COLOR
            )
        else:
            exit_button_text = config.BODY_FONT.render(
                "Exit Game", True, config.OPTION_COLOR
            )
        screen.blit(exit_button_text, exit_button_rect)

        # Display winner message if the game is over
        if game_over:
            winner_text = f"{winner} wins!"
            winner_rendered = config.TITLE_FONT.render(
                winner_text, True, config.HIGHLIGHT_COLOR
            )
            winner_rect = winner_rendered.get_rect(
                center=(config.WINDOW_SIZE[0] // 2, 50)
            )
            screen.blit(winner_rendered, winner_rect)

        # Draw rows of objects
        mouse_pos = pygame.mouse.get_pos()
        for row_index, num_objects in enumerate(rows):
            y_position = start_y + row_index * row_spacing
            for i in range(num_objects):
                x_position = (
                    config.WINDOW_SIZE[0] // 2
                    - (num_objects - 1) * object_size
                    + i * 2 * object_size
                )
                distance = (
                    (mouse_pos[0] - x_position) ** 2 + (mouse_pos[1] - y_position) ** 2
                ) ** 0.5
                is_hovered = distance <= object_size

                # Determine color
                if i in selected_items[row_index]:
                    color = config.HIGHLIGHT_COLOR
                elif (
                    mouse_down
                    and is_hovered
                    and (current_row is None or current_row == row_index)
                ):
                    color = config.HIGHLIGHT_COLOR
                    current_row = row_index
                    if i not in selected_items[row_index]:
                        selected_items[row_index].append(i)
                else:
                    color = config.OPTION_COLOR

                pygame.draw.circle(screen, color, (x_position, y_position), object_size)

        # Draw Player Indicators
        player_1_color = (
            config.HIGHLIGHT_COLOR
            if current_player == config.Players.PLAYER_1 and not game_over
            else config.OPTION_COLOR
        )
        player_2_color = (
            config.HIGHLIGHT_COLOR
            if current_player == config.Players.PLAYER_2 and not game_over
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

        # Draw Play Button if selection is made and game isn't over
        if not game_over and selection_made:
            if play_button_rect.collidepoint(mouse_pos):
                play_button_text = config.BODY_FONT.render(
                    "Play", True, config.HIGHLIGHT_COLOR
                )
            else:
                play_button_text = config.BODY_FONT.render(
                    "Play", True, config.OPTION_COLOR
                )
            screen.blit(play_button_text, play_button_rect)

        # Draw Replay Button if game is over
        if game_over:
            if replay_button_rect.collidepoint(mouse_pos):
                replay_button_text = config.BODY_FONT.render(
                    "Replay", True, config.HIGHLIGHT_COLOR
                )
            else:
                replay_button_text = config.BODY_FONT.render(
                    "Replay", True, config.OPTION_COLOR
                )
            screen.blit(replay_button_text, replay_button_rect)

        pygame.display.flip()
