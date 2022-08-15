# Drawing shapes

# 1. Import
import pygame
from pygame.locals import *
import sys

# 2. Define Constants
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
TEAL = (0, 128, 128)
WINDOW_WIDTH = 640
WINDOW_HEIGTH = 480
FPS = 30

# 3. Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGTH))
clock = pygame.time.Clock()

# 4. Load assets - images, sounds, etc.

# 5. Initializes variables

# 6. Loop forever
while True:
    # 7. Check for and handle events
    for event in pygame.event.get():
        # Quit if Close button was clicked
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # 8. Do any per frame actions

    # 9. Clear the window
    window.fill(BLACK)

    # 10. Draw all window elements
    # Draw a box
    pygame.draw.line(window, BLUE, (20, 20), (60, 20), 4)
    pygame.draw.line(window, BLUE, (20, 20), (20, 60), 4)
    pygame.draw.line(window, BLUE, (20, 60), (60, 60), 4)
    pygame.draw.line(window, BLUE, (60, 20), (60, 60), 4)
    # Draw an X in the box
    pygame.draw.line(window, BLUE, (20, 20), (60, 60), 4)
    pygame.draw.line(window, BLUE, (20, 60), (60, 20), 4)

    # Draw a filled and empty circle
    pygame.draw.circle(window, GREEN, (250, 50), 30, 0)  # filled
    pygame.draw.circle(window, GREEN, (400, 50), 30, 2)  # 2px edge

    # Draw a filled and empty rectangle
    pygame.draw.rect(window, RED, (250, 150, 100, 50), 0)  # filled
    pygame.draw.rect(window, RED, (400, 150, 100, 50), 1)  # 1px edge

    # Draw a filled and empty ellipse
    pygame.draw.ellipse(window, YELLOW, (250, 250, 80, 40), 0)  # filled
    pygame.draw.ellipse(window, YELLOW, (400, 250, 80, 40), 2)  # 2px edge

    # Draw a six-sided polygon
    pygame.draw.polygon(window, TEAL, ((240, 350), (350, 350),
                                       (410, 410), (350, 470),
                                       (240, 470), (170, 410)))

    # Draw an arc
    pygame.draw.arc(window, BLUE, (20, 400, 100, 100), 0, 2, 5)

    # Draw anti-alliased lines: single line and set of lines
    pygame.draw.aaline(window, RED, (500, 400), (540, 470), 1)
    pygame.draw.aalines(window, BLUE, True, ((580, 400), (587, 450), (595, 460), (600, 444)), 1)

    # 11. Update the window
    pygame.display.update()

    # 12. Slow things down a bit
    clock.tick(FPS)

