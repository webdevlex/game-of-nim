import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
window_size = (800, 600)  # Width, Height
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Basic Pygame Window")

# Colors
background_color = (30, 30, 30)  # Dark grey background

# Main loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(background_color)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
