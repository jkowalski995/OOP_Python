# Bounce from edges

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
NUMBER_PIXELS_TO_MOVE = 3
BASE_PATH = Path(__file__).resolve().parent  # For creating absolute path (if we want to run program from CLI absolute path is a must have)

# 3. Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4. Load assets - images, sounds, etc.
pathToImage = BASE_PATH / 'images/gitlab_original_logo_icon_146503_small.png'
player = pygame.image.load(pathToImage)

# 5. Initialize variables
MAX_WIDTH = WINDOW_WIDTH - IMAGE_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - IMAGE_WIDTH_HEIGHT
playerX = random.randrange(MAX_WIDTH)
playerY = random.randrange(MAX_HEIGHT)
xSpeed = NUMBER_PIXELS_TO_MOVE
ySpeed = NUMBER_PIXELS_TO_MOVE

# 6. Loop forever
while True:
    # 7. Check for and handle events
    for event in pygame.event.get():
        # Quit if Close button was clicked
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8. Do any per frame actions
    if (playerX < 0) or (playerX >= MAX_WIDTH):
        xSpeed = -xSpeed  # reverse X direction

    if (playerY < 0) or (playerY >= MAX_HEIGHT):
        ySpeed = -ySpeed  # reverse Y direction

    # Update the ball's location using the speed in two directions
    playerX = playerX + xSpeed
    playerY = playerY + ySpeed

    # 9. Clear the window
    window.fill(BLACK)

    # 10. Draw all window elements
    window.blit(player, (playerX, playerY))

    # 11. Update the window
    pygame.display.update()

    # 12. Slow things down a bit
    clock.tick(FPS)
