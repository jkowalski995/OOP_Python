# Pygame - Drawing Image

# 1. Import
import pygame
from pygame.locals import *
import sys
from pathlib import Path

# 2. Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGTH = 480
FPS = 30
BASE_PATH = Path(__file__).resolve().parent  # For creating absolute path (if we want to run program from CLI absolute path is a must have)

# 3. Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
clock = pygame.time.Clock()

# 4. Load assets - images, sounds, etc.
pathToImage = BASE_PATH / 'images/gitlab_original_logo_icon_146503_small.png'
backgroundImage = pygame.image.load(pathToImage)

# 5. initializes variables

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
    # draw image on 100 on x and 200 on y
    window.blit(backgroundImage, (100, 200))

    # 11. Update the window
    pygame.display.update()

    # 12. Slow things down a bit
    clock.tick(FPS)