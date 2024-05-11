import pygame
import random
import sys
from constants import *

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN
        self.score = 0

        self.food_position = self.random_food_position()

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (cur[0] + (x * GRID_SIZE), cur[1] + (y * GRID_SIZE))

        if len(self.positions) > 2 and new in self.positions[2:]:
            return True
        if new[0] < 0 or new[0] >= WIDTH or new[1] < 0 or new[1] >= HEIGHT:
            return True

        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()
        return False

    def reset(self):
        self.length = 1
        self.positions = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0
        self.food_position = self.random_food_position()

    def random_food_position(self):
        while True:
            x = random.randrange(0, GRID_WIDTH)
            y = random.randrange(0, GRID_HEIGHT)
            if (x, y) not in self.positions:
                return (x * GRID_SIZE, y * GRID_SIZE)

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, BLACK, r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if event.pos[0] >= WIDTH - 30 and event.pos[1] <= 30:
                    pygame.quit()
                    sys.exit()
