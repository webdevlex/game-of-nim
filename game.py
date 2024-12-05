import pygame
import sys
import config
from bot.game_of_nim import GameOfNim
from bot.games import depth_limited_alpha_beta_search
from helpers.get_circle_dimensions import get_circle_dimensions
import time


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
    play_button_text = config.BODY_FONT.render(
        "Confirm Move", True, config.OPTION_COLOR
    )
    play_button_rect = play_button_text.get_rect(
        center=(config.WINDOW_SIZE[0] // 2, config.WINDOW_SIZE[1] - 50)
    )

    replay_button_text = config.BODY_FONT.render("Replay", True, config.OPTION_COLOR)
    replay_button_rect = replay_button_text.get_rect(
        center=(config.WINDOW_SIZE[0] // 2, config.WINDOW_SIZE[1] - 50)
    )

    dimensions = get_circle_dimensions(config.ROWS)
    object_size = dimensions.get("object_size")
    row_spacing = dimensions.get("row_spacing")
    row_vertical_offset = dimensions.get("row_vertical_offset")

    # Calculate vertical start position to center the rows
    total_height = len(rows) * row_spacing
    start_y = (config.WINDOW_SIZE[1] - total_height) // 2 + row_vertical_offset

    def bot_turn():
        """Simulate the bot's turn with an animation of three dots."""
        nonlocal game_over, winner, current_player, rows

        # Show the "thinking" animation
        start_time = time.time()
        dot_texts = [".", "..", "..."]
        dot_index = 0

        while time.time() - start_time < 2:
            # Clear and redraw screen
            screen.fill(config.BACKGROUND_COLOR)

            # Redraw static elements (e.g., exit button, rows, player indicators)
            screen.blit(exit_button_text, exit_button_rect)
            for row_index, num_objects in enumerate(rows):
                y_position = start_y + row_index * row_spacing
                for i in range(num_objects):
                    x_position = (
                        config.WINDOW_SIZE[0] // 2
                        - (num_objects - 1) * object_size
                        + i * 2 * object_size
                    )
                    pygame.draw.circle(
                        screen,
                        config.OPTION_COLOR,
                        (x_position, y_position),
                        object_size,
                    )

            # Redraw "Human" text
            player_1_text = config.BODY_FONT.render("Human", True, config.OPTION_COLOR)
            player_1_rect = player_1_text.get_rect(
                topleft=(20, config.WINDOW_SIZE[1] - 50)
            )
            screen.blit(player_1_text, player_1_rect)

            # Redraw "Bot" text
            bot_text = config.BODY_FONT.render("Bot", True, config.HIGHLIGHT_COLOR)
            bot_rect = bot_text.get_rect(
                topright=(config.WINDOW_SIZE[0] - 20, config.WINDOW_SIZE[1] - 50)
            )
            screen.blit(bot_text, bot_rect)

            # Display the "thinking" dots below the "Bot" text
            dots_text = config.BODY_FONT.render(
                dot_texts[dot_index], True, config.HIGHLIGHT_COLOR
            )
            dots_rect = dots_text.get_rect(
                midtop=(bot_rect.centerx, bot_rect.bottom - 10)
            )
            screen.blit(dots_text, dots_rect)

            pygame.display.flip()

            # Update the dots every 0.5 seconds
            time.sleep(0.5)
            dot_index = (dot_index + 1) % len(dot_texts)

        # Bot calculates the move after 3 seconds
        game = GameOfNim(board=rows)
        state = game.initial
        best_move = depth_limited_alpha_beta_search(
            state, game, max_depth=config.MAX_DEPTH
        )

        # Apply the move returned by the bot
        if best_move:
            selected_row, items_to_remove = best_move
            rows[selected_row] -= items_to_remove
            print(f"Bot removed {items_to_remove} item(s) from row {selected_row}.")
        # Check if the game is over
        if sum(rows) == 1:  # Only 1 item left
            game_over = True
            winner = "Bot"
        else:
            # Switch to the human's turn
            current_player = config.Players.PLAYER_1

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
                elif not game_over and current_player == config.Players.PLAYER_1:
                    if play_button_rect.collidepoint(mouse_pos) and selection_made:
                        # Remove selected items from the row
                        for row, items in selected_items.items():
                            if items:
                                rows[row] -= len(items)
                                print(
                                    f"Human removed {len(items)} item(s) from row {row}."
                                )
                                break
                        # Check for game over
                        if sum(rows) == 1:  # Only 1 item left
                            game_over = True
                            winner = "Human"
                        else:
                            # Switch to bot's turn
                            current_player = config.Players.PLAYER_2
                            bot_turn()
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

        # Simulate bot turn if it's the bot's turn and the game isn't over
        if not game_over and current_player == config.Players.PLAYER_2:
            bot_turn()

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
        if (
            not game_over
            and current_player == config.Players.PLAYER_1
            and selection_made
        ):
            if play_button_rect.collidepoint(mouse_pos):
                play_button_text = config.BODY_FONT.render(
                    "Confirm Move", True, config.HIGHLIGHT_COLOR
                )
            else:
                play_button_text = config.BODY_FONT.render(
                    "Confirm Move", True, config.OPTION_COLOR
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
