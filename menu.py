import pygame
import config

# Menu options
menu_options = ["New Game", "Settings", "Exit"]
menu_rects = []  # Initialize once

# Calculate menu option rectangles once
for index, option in enumerate(menu_options):
    option_text = config.OPTION_FONT.render(option, True, config.OPTION_COLOR)
    option_rect = option_text.get_rect(
        center=(config.WINDOW_SIZE[0] // 2, 300 + index * 60)
    )
    menu_rects.append(option_rect)


def draw_menu(screen):
    screen.fill(config.BACKGROUND_COLOR)

    # Draw the title
    title_text = config.TITLE_FONT.render("GAME OF NIM", True, config.TITLE_COLOR)
    title_rect = title_text.get_rect(center=(config.WINDOW_SIZE[0] // 2, 175))
    screen.blit(title_text, title_rect)

    # Draw the options
    for index, option in enumerate(menu_options):
        option_text = config.OPTION_FONT.render(option, True, config.OPTION_COLOR)
        option_rect = menu_rects[index]

        # Check if the mouse is over the option
        if option_rect.collidepoint(pygame.mouse.get_pos()):
            option_text = config.OPTION_FONT.render(
                option, True, config.HIGHLIGHT_COLOR
            )
        screen.blit(option_text, option_rect)

    pygame.display.flip()


def handle_menu_events(mouse_pos):
    # Check which menu option is clicked
    for index, option_rect in enumerate(menu_rects):
        if option_rect.collidepoint(mouse_pos):
            return menu_options[index]
    return None
