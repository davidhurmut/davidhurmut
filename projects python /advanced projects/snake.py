# prepei na katevasete to PYGAME apo ta paketa sto Thonny (an to exete eidh agnohste to)

import pygame
import random

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("-")

clock = pygame.time.Clock()
snake_block = 20
snake_speed = 8

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
gray = (200, 200, 200)

font_style = pygame.font.SysFont(None, 35)
score_font = pygame.font.SysFont(None, 30)

def display_score(score):
    value = score_font.render("Score: " + str(score), True, white)
    screen.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for i, x in enumerate(snake_list):
        color = (0, min(255, 50 + i*10), 0)
        pygame.draw.rect(screen, color, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1
    score = 0

    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    while not game_over:
        while game_close:
            screen.fill(blue)
            message("exases, C = Play Again | Q = quit", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_a]:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key in [pygame.K_UP, pygame.K_w]:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key in [pygame.K_DOWN, pygame.K_s]:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(blue)
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(screen, gray, [0, 0, width, height], 2)

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        display_score(score)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            length_of_snake += 1
            score += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()

