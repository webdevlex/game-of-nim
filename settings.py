import pygame
import config


def settings_menu(screen):
    # Fonts and initial settings
    header_text = config.TITLE_FONT.render("Settings", True, config.TITLE_COLOR)
    header_rect = header_text.get_rect(center=(config.WINDOW_SIZE[0] // 2, 50))

    # Options text
    player_text = config.BODY_FONT.render(
        f"Player to go first: {config.DEFAULT_PLAYER.replace('_', ' ').title()}",
        True,
        config.OPTION_COLOR,
    )
    player_rect = player_text.get_rect(center=(config.WINDOW_SIZE[0] // 2, 150))

    rows_text = config.BODY_FONT.render(
        f"Number of rows: {config.ROWS}", True, config.OPTION_COLOR
    )
    rows_rect = rows_text.get_rect(center=(config.WINDOW_SIZE[0] // 2, 250))

    # Instructions for changing settings
    instructions_text = config.BODY_FONT.render(
        "Press P to toggle player, Up/Down to change rows", True, config.OPTION_COLOR
    )
    instructions_rect = instructions_text.get_rect(
        center=(config.WINDOW_SIZE[0] // 2, 350)
    )

    # Back button
    back_text = config.BODY_FONT.render("Back to Menu", True, config.OPTION_COLOR)
    back_rect = back_text.get_rect(center=(config.WINDOW_SIZE[0] // 2, 500))

    running = True
    current_player = config.DEFAULT_PLAYER
    current_rows = config.ROWS

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if back button is clicked
                if back_rect.collidepoint(event.pos):
                    # Update the config settings
                    config.DEFAULT_PLAYER = current_player
                    config.ROWS = current_rows
                    return  # Exit settings menu
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    # Toggle player between player_1 and player_2
                    current_player = (
                        config.Players.PLAYER_2
                        if current_player == config.Players.PLAYER_1
                        else config.Players.PLAYER_1
                    )
                elif event.key == pygame.K_UP:
                    # Increase rows (limit to 10 for example)
                    if current_rows < 10:
                        current_rows += 1
                elif event.key == pygame.K_DOWN:
                    # Decrease rows (minimum of 1)
                    if current_rows > 1:
                        current_rows -= 1

        # Update settings display
        player_text = config.BODY_FONT.render(
            f"Player to go first: {current_player.replace('_', ' ').title()}",
            True,
            config.OPTION_COLOR,
        )
        rows_text = config.BODY_FONT.render(
            f"Number of rows: {current_rows}", True, config.OPTION_COLOR
        )

        # Draw the settings menu
        screen.fill(config.BACKGROUND_COLOR)
        screen.blit(header_text, header_rect)
        screen.blit(player_text, player_rect)
        screen.blit(rows_text, rows_rect)
        screen.blit(instructions_text, instructions_rect)

        # Back button hover effect
        if back_rect.collidepoint(pygame.mouse.get_pos()):
            back_text = config.BODY_FONT.render(
                "Back to Menu", True, config.HIGHLIGHT_COLOR
            )
        else:
            back_text = config.BODY_FONT.render(
                "Back to Menu", True, config.OPTION_COLOR
            )

        screen.blit(back_text, back_rect)
        pygame.display.flip()
