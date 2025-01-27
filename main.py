# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame # type: ignore
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    game_loop(screen)
    pygame.display.fill()

def game_loop(screen):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    while True:
        screen.fill(1)

if __name__ == "__main__":
    main()