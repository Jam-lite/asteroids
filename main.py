import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # === GAME LOOP ===
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fill the screen with black (RGB: 0, 0, 0)
        screen.fill((0, 0, 0))

        # Update (flip) the display
        pygame.display.flip()

if __name__ == "__main__":
    main()