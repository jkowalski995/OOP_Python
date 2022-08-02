# Pygame - Window Only

# 1. Import
import pygame
from pygame.locals import *
import sys

# 2. Define Constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGTH = 480
FPS = 30

# 3. Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
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

    # 11. Update the window
    pygame.display.update()

    # 12. Slow things down a bit
    clock.tick(FPS)
