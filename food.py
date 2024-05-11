import pygame
import random
from constants import *

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH-1) * GRID_SIZE, random.randint(0, GRID_HEIGHT-1) * GRID_SIZE)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.position[0] + GRID_SIZE // 2, self.position[1] + GRID_SIZE // 2), GRID_SIZE // 2)
