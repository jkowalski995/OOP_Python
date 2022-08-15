# Detect individual key press

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
TARGET_WIDTH_HEIGHT = 120
TARGET_X = 500
TARGET_Y = 320
NUMBER_PIXELS_TO_MOVE = 3

# 3. Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4. Load assets - images, sounds, etc.
pathToImage = BASE_PATH / 'images/gitlab_original_logo_icon_146503_small.png'
player = pygame.image.load(pathToImage)
pathToImage = BASE_PATH / 'images/Octocat_small.png'
target = pygame.image.load(pathToImage)

# 5. Initializes variables
playerX = random.randrange(MAX_WIDTH)
playerY = random.randrange(MAX_HEIGHT)
targetRec = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)

# 6. Loop forever
while True:
    # 7. Check for and ahndle events
    for event in pygame.event.get():
        # Quit if Close button was clicked
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8. Do any per frame actions
    # Check if key was clicked
    # We don't look for the event but check the keys
    # in every frame so this part was moved from for loop
    # to section 8
    keyPressedTuple = pygame.key.get_pressed()

    if keyPressedTuple[pygame.K_LEFT]:
        playerX = playerX - NUMBER_PIXELS_TO_MOVE

    if keyPressedTuple[pygame.K_RIGHT]:
        playerX = playerX + NUMBER_PIXELS_TO_MOVE

    if keyPressedTuple[pygame.K_UP]:
        playerY = playerY - NUMBER_PIXELS_TO_MOVE

    if keyPressedTuple[pygame.K_DOWN]:
        playerY = playerY + NUMBER_PIXELS_TO_MOVE

    # Check if ball is colliding with target
    playerRect = pygame.Rect(playerX, playerY, IMAGE_WIDTH_HEIGHT, IMAGE_WIDTH_HEIGHT)

    if playerRect.colliderect(targetRec):
        print('Ball reach the target')

    # 9. Clear the window
    window.fill(BLACK)

    # 10. Draw all window elements
    # Drawing the player and the target
    window.blit(target, (TARGET_X, TARGET_Y))
    window.blit(player, (playerX, playerY))

    # 11. Update the window
    pygame.display.update()

    # 12. Slow things down a bit
    clock.tick(FPS)
