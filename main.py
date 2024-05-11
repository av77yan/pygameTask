import pygame
import sys
from snake import Snake
from food import Food
from constants import *

def draw_grid(surface):
    for y in range(0, HEIGHT, GRID_SIZE):
        for x in range(0, WIDTH, GRID_SIZE):
            r = pygame.Rect((x, y), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, BLACK, r, 1)

def game_over(screen, score):
    font = pygame.font.SysFont(None, 50)
    game_over_text = font.render("Game Over", True, WHITE)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    screen.blit(score_text, (WIDTH // 2 - 80, HEIGHT // 2))
    restart_text = font.render("'Enter' zum Neustart", True, WHITE)
    screen.blit(restart_text, (WIDTH // 2 - 150, HEIGHT // 2 + 50))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake')

    snake = Snake()
    food = Food()

    game_over_flag = False

    while not game_over_flag:
        screen.fill(BLACK)
        draw_grid(screen)
        snake.handle_keys()
        game_over_flag = snake.move()

        if not game_over_flag and snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()

        snake.draw(screen)
        food.draw(screen)

        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"Score: {snake.score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(FPS)

    restart_game = game_over(screen, snake.score)
    if restart_game:
        main()

if __name__ == '__main__':
    main()
