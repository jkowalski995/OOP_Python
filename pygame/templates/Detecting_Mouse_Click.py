# Pygame - Detecting Mouse Click

# 1. Import packages
import pygame
from pygame.locals import *
import sys
import random
from pathlib import Path

# 2. Define Constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FPS = 30
IMAGE_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - IMAGE_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - IMAGE_WIDTH_HEIGHT
BASE_PATH = Path(__file__).resolve().parent  # For creating absolute path (if we want to run program from CLI absolute path is a must have)

# 3. Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4. Load assets - images, sounds, etc.
pathToImage = BASE_PATH / 'images/gitlab_original_logo_icon_146503_small.png'
backgroundImage = pygame.image.load(pathToImage)

# 5. Initializes variables
imageX = random.randrange(MAX_WIDTH)
imageY = random.randrange(MAX_HEIGHT)
imageRect = pygame.Rect(imageX, imageY, IMAGE_WIDTH_HEIGHT, IMAGE_WIDTH_HEIGHT)

# 6. Loop forever
while True:
    # 7. Check for and handle events
    for event in pygame.event.get():
        # Quit if Close button was clicked
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # See if user clicked
        if event.type == pygame.MOUSEBUTTONUP:
            # mouseX, mouseY = event.pos  # could do this if we need it

            # Check if user clicked in image area
            # If yes, choose random new position for the image
            if imageRect.collidepoint(event.pos):
                imageX = random.randrange(MAX_WIDTH)
                imageY = random.randrange(MAX_HEIGHT)
                imageRect = pygame.Rect(imageX, imageY, IMAGE_WIDTH_HEIGHT, IMAGE_WIDTH_HEIGHT)

    # 8. Do any per frame actions

    # 9. Clear the window
    window.fill(BLACK)

    # 10. Draw all window elements
    # Draw image in random location
    window.blit(backgroundImage, (imageX, imageY))

    # 11. Update the window
    pygame.display.update()

    # 12. Slow things down a bit
    clock.tick(FPS)
