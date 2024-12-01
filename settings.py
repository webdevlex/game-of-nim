import pygame
import config
import sys

PLAYER_1 = config.Players.PLAYER_1
PLAYER_2 = config.Players.PLAYER_2


def settings_menu(screen):
    # Fonts and initial settings
    header_text = config.TITLE_FONT.render("SETTINGS", True, config.TITLE_COLOR)
    header_rect = header_text.get_rect(center=(config.WINDOW_SIZE[0] // 2, 100))

    # Button dimensions and spacing
    button_width, button_height = 100, 50
    rows_button_width, rows_button_height = 50, 50
    spacing = 10

    # Starting player layout
    label_text = config.BODY_FONT.render("Starting player:", True, config.OPTION_COLOR)
    label_rect = label_text.get_rect(center=((config.WINDOW_SIZE[0] // 4) + 75, 225))

    human_button_rect = pygame.Rect(
        (config.WINDOW_SIZE[0] // 2 - button_width - spacing // 2) + 125,
        200,
        button_width,
        button_height,
    )
    bot_button_rect = pygame.Rect(
        (config.WINDOW_SIZE[0] // 2 + spacing // 2) + 125,
        200,
        button_width,
        button_height,
    )

    # Number of rows layout
    rows_label_text = config.BODY_FONT.render(
        "Number of rows:", True, config.OPTION_COLOR
    )
    rows_label_rect = rows_label_text.get_rect(
        center=((config.WINDOW_SIZE[0] // 4) + 75, 300)
    )

    rows_text_pos = (config.WINDOW_SIZE[0] // 2 - 25, 300)
    minus_button_rect = pygame.Rect(
        rows_text_pos[0] + rows_button_width + 30,
        275,
        rows_button_width,
        rows_button_height,
    )
    plus_button_rect = pygame.Rect(
        minus_button_rect.right + spacing, 275, rows_button_width, rows_button_height
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
                mouse_pos = event.pos

                # Back button logic
                if back_rect.collidepoint(mouse_pos):
                    config.DEFAULT_PLAYER = current_player
                    config.ROWS = current_rows
                    return

                # Starting player buttons
                if human_button_rect.collidepoint(mouse_pos):
                    current_player = PLAYER_1
                elif bot_button_rect.collidepoint(mouse_pos):
                    current_player = PLAYER_2

                # Adjust rows
                if plus_button_rect.collidepoint(mouse_pos) and current_rows < 10:
                    current_rows += 1
                elif minus_button_rect.collidepoint(mouse_pos) and current_rows > 2:
                    current_rows -= 1

        # Draw settings menu
        screen.fill(config.BACKGROUND_COLOR)
        screen.blit(header_text, header_rect)

        # Draw starting player layout
        screen.blit(label_text, label_rect)
        pygame.draw.rect(
            screen,
            (
                config.HIGHLIGHT_COLOR
                if current_player == PLAYER_1
                else config.OPTION_COLOR
            ),
            human_button_rect,
        )
        pygame.draw.rect(
            screen,
            (
                config.HIGHLIGHT_COLOR
                if current_player == PLAYER_2
                else config.OPTION_COLOR
            ),
            bot_button_rect,
        )
        human_text = config.BODY_FONT.render("HUMAN", True, config.TITLE_COLOR)
        bot_text = config.BODY_FONT.render("BOT", True, config.TITLE_COLOR)
        screen.blit(
            human_text,
            human_text.get_rect(center=human_button_rect.center),
        )
        screen.blit(
            bot_text,
            bot_text.get_rect(center=bot_button_rect.center),
        )

        # Draw number of rows layout
        screen.blit(rows_label_text, rows_label_rect)

        # Display current number of rows
        rows_text = config.BODY_FONT.render(str(current_rows), True, config.TITLE_COLOR)
        screen.blit(
            rows_text,
            rows_text.get_rect(
                center=(rows_text_pos[0] + button_width // 2, rows_text_pos[1])
            ),
        )

        # Draw minus and plus buttons
        pygame.draw.rect(screen, config.OPTION_COLOR, minus_button_rect)
        pygame.draw.rect(screen, config.OPTION_COLOR, plus_button_rect)
        minus_text = config.BODY_FONT.render("-", True, config.TITLE_COLOR)
        plus_text = config.BODY_FONT.render("+", True, config.TITLE_COLOR)
        screen.blit(minus_text, minus_text.get_rect(center=minus_button_rect.center))
        screen.blit(plus_text, plus_text.get_rect(center=plus_button_rect.center))

        # Draw back button
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
