import pygame
import sys
import time
import random

from pygame.locals import *

# Set window size value
WINDOW_WIDTH = 800
WINDOW_HEIGTH = 600

WHITE = (255, 255, 255)

# main 처럼
if __name__ == '__main__':
    pygame.init() # Initialize game
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH), 0, 32) # Set window size
    pygame.display.set_caption('Python Game')
    surface = pygame.Surface.convert()
    surface.fill(WHITE)
    clock = pygame.time.Clock()
    pygame.key_set_repeat(1, 40)
    window.blit(surface, (0, 0))