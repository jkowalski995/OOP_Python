# Sound Effect from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=6222">Pixabay</a>
# Bounce from edges with Rect

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
NUMBER_PIXELS_TO_MOVE = 3
BASE_PATH = Path(__file__).resolve().parent  # For creating absolute path (if we want to run program from CLI absolute path is a must have)

# 3. Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4. Load assets - images, sounds, etc.
pathToImage = BASE_PATH / 'images/gitlab_original_logo_icon_146503_small.png'
player = pygame.image.load(pathToImage)
# Load sound FX for bounce !ONLY WAV or OGG!
pathToBounceSound = BASE_PATH / 'sounds/boing-6222.wav'
bounceSound = pygame.mixer.Sound(pathToBounceSound)
# Load sound for background music !ONLY MP3, WAV or OGG!
pathToMusic = BASE_PATH / 'sounds/relaxing-mountains-rivers-streams-running-water-18178.mp3'
pygame.mixer.music.load(pathToMusic)
pygame.mixer.music.play(-1, 0.0)  # -1 - loop forever, 0.0 - starting point


# 5. Initialize variables
playerRect = player.get_rect()
MAX_WIDTH = WINDOW_WIDTH - playerRect.width
MAX_HEIGHT = WINDOW_HEIGHT - playerRect.height
playerRect.left = random.randrange(MAX_WIDTH)
playerRect.right = random.randrange(MAX_HEIGHT)
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
    if (playerRect.left < 0) or (playerRect.right >= WINDOW_WIDTH):
        xSpeed = -xSpeed  # reverse X direction
        bounceSound.play()  # play bounce

    if (playerRect.top < 0) or (playerRect.bottom >= WINDOW_HEIGHT):
        ySpeed = -ySpeed  # reverse Y drection
        bounceSound.play()  # play bounce

    # Update the player rect using the speed in two directions
    playerRect.left = playerRect.left + xSpeed
    playerRect.top = playerRect.top + ySpeed

    # 9. Clear the window
    window.fill(BLACK)

    # 10. Draw all window elements
    window.blit(player, playerRect)

    # 11. Update the window
    pygame.display.update()

    # 12. Slow things down a bit
    clock.tick(FPS)
