import pygame
import time

"""
This program simulates an eraser effect on a canvas.
The canvas consists of a grid of blue 'cells'.
An eraser is created, which removes the cells when dragged.
"""

# Initialize pygame
pygame.init()

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

# Colors
BLUE = (0, 0, 225)
WHITE = (255, 255, 255)
PINK = (225, 182, 193)

# Set up the display
screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
pygame.display.set_caption("Eraser Effect in Pygame")

# Create grid of cells
grid = []
for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):
        rect = pygame.Rect(col, row, CELL_SIZE, CELL_SIZE)
        grid.append(rect)

# Eraser setup (initially hidden)
eraser = pygame.Rect(200, 200, ERASER_SIZE, ERASER_SIZE)
eraser_active = False  # Eraser only activates on click

# Set up the clock for smooth performance
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    # Draw grid
    for rect in grid:
        pygame.draw.rect(screen, BLUE, rect)

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Activate eraser on click
    mouse_pressed = pygame.mouse.get_pressed()
    if mouse_pressed[0]:  # Left mouse button
        eraser_active = True

    # If eraser is active, move it with the mouse
    if eraser_active:
        eraser.topleft = (mouse_x, mouse_y)

        # Remove cells that eraser touches
        grid = [rect for rect in grid if not eraser.colliderect(rect)]

    # Draw eraser
    pygame.draw.rect(screen, PINK, eraser)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Quit if close button clicked
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Quit if Escape key pressed
                running = False

    pygame.display.flip()
    clock.tick(60)  # 60 FPS for smooth performance

pygame.quit()
