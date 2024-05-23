import pygame as pg
import random

pg.init()
width = 1280
height = 720

FPS = 60
clock = pg.time.Clock()

state = True

main = True
menu = False

lvl1 = False
lvl2 = False
lvl3 = False
lvl4 = False


lvl1_complete = False
lvl2_complete = False
lvl3_complete = False
lvl4_complete = False

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 200, 0)
GREEN = (100, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# №1
cell_size = 40
# 0-пустое место, 1-стена, 2-финиш
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 2, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
player_pos = [1, 1]


# №2
paddle_width = 100
paddle_height = 20
paddle_speed = 10

ball_R = 10
ball_speed = 5

brick_rows = 0
brick_columns = 12
brick_space = 5
brick_width = (width - (brick_columns + 1) * brick_space) // brick_columns
brick_height = 30

# Платформа
paddle = pg.Rect(width // 2 - paddle_width // 2, height - paddle_height - 10, paddle_width, paddle_height)

# Мяч
ball = pg.Rect(width // 2, height // 2, ball_R * 2, ball_R * 2)
ball_dx = ball_speed * random.choice((1, -1))
ball_dy = ball_speed * random.choice((1, -1))

# Блоки
bricks = [pg.Rect(col * (brick_width + brick_space) + brick_space, row * (brick_height + brick_space) + brick_space, brick_width, brick_height) for row in range(brick_rows) for col in range(brick_columns)]

def level2():
    pg.draw.rect(window, RED, paddle)
    pg.draw.ellipse(window, WHITE, ball)

    for brick in bricks:
        pg.draw.rect(window, GREEN, brick)

def reset_ball():
    global ball_dx, ball_dy
    ball.x, ball.y = width // 2 - ball_R, height // 2 - ball_R
    ball_dx, ball_dy = 0, ball_speed
    pg.time.set_timer(pg.USEREVENT, 3000)


# №3
snake_block = 10
snake_speed = 15

def score(score):
    value = font.render("Score: " + str(score), True, WHITE)
    window.blit(value, [0, 0])

def snake(snake_block, snake_lst):
    for x in snake_lst:
        pg.draw.rect(window, GREEN, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    msg = font.render(msg, 1, color)
    window.blit(msg, [width / 6, height / 3])


# №4
pac_wall = 40

# 0-Пустое место, 1-стена, 2-Поинт
pac_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 2, 1],
    [1, 2, 1, 0, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 0, 1, 2, 1],
    [1, 2, 1, 1, 1, 2, 1, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 2, 1, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1],
    [1, 0, 0, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 0, 0, 1],
    [1, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

pac_pos = [4, 16]
pac_speed = 1

def can_move(x, y):
    if 0 <= x < len(pac_map[0]) and 0 <= y < len(pac_map) and pac_map[y][x] != 1:
        return True
    return False

def eat_dot(x, y):
    if pac_map[y][x] == 2:
        pac_map[y][x] = 0

def check_win():
    for row in pac_map:
        if 2 in row:
            return False
    return True

pg.display.set_caption("MiniGames")
window = pg.display.set_mode((width, height))

icon = pg.image.load("Images/icon_logo.png")
icon = pg.transform.scale(icon, (40, 40))

background = pg.image.load("Images/bg_main.jpg")
background = pg.transform.scale(background, (1280, 720))

background_puzzle = pg.image.load("Images/bg_puzzle.jpg")





pg.display.set_icon(icon)

btn_image = pg.image.load("Images/btn_img.png")

exit_img = pg.image.load("Images/exit.png")
exit_img = pg.transform.scale(exit_img, (64, 64))

name_text = pg.image.load("Images/name_text.png")

class Start:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pg.image.load(image)
        self.rect = pg.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())


start_lst = [Start(144, 280, "Images/btn_images/start_btn.png")]

class Name:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pg.image.load("Images/name_text.png")
        self.rect = pg.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())


name_lst = [Name(64, 60, "Images/name_text.png")]

class Button:

    def __init__(self, x, y, index, image_path):
        self.x = x
        self.y = y
        self.index = index
        self.image = pg.image.load(image_path)
        self.rect = pg.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

class Exit:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pg.image.load(image)
        self.rect = pg.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())


exit_lst = [Exit(1200, 16, "Images/exit.png")]


button_lst = [Button(16, 16, 1, "Images/btn_images/btn_image1.png"),
              Button(331, 16, 2, "Images/btn_images/btn_image2.png"),
              Button(646, 16, 3, "Images/btn_images/btn_image3.png"),
              Button(961, 16, 4, "Images/btn_images/btn_image4.png")]

class Completed:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pg.image.load(image)
        self.rect = pg.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())


completed_lst = [Completed(286, 183, "Images/completed.png"),]

while state:
    window.blit(background, (0, 0))
    pos = pg.mouse.get_pos()
    font = pg.font.Font("Fonts/ThisAppealFont.otf", 64)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            state = False

    if main:
        pg.time.Clock().tick(60)
        background = pg.image.load("Images/bg_main.jpg")
        for start in start_lst:
            window.blit(start.image, start.rect)
        for name in name_lst:
            window.blit(name.image, name.rect)
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_pos = pg.mouse.get_pos()
                for start in start_lst:
                    if start.rect.collidepoint(click_pos) and main:
                        print("started")
                        main = False
                        menu = True
                        pg.time.delay(200)

    elif menu:
        pg.time.Clock().tick(60)
        background = pg.image.load("Images/bg_main.jpg")
        for btn in button_lst:
            window.blit(btn.image, btn.rect)

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_pos = pg.mouse.get_pos()
                for btn in button_lst:
                    if btn.rect.collidepoint(click_pos) and menu:
                        if btn.index == 1:
                            print("entered 1")
                            menu = False
                            lvl1 = True
                            pg.time.delay(60)
                        elif btn.index == 2:
                            print("entered 2")
                            menu = False
                            lvl2 = True
                            pg.time.delay(60)
                        elif btn.index == 3:
                            print("entered 3")
                            menu = False
                            lvl3 = True
                            pg.time.delay(60)
                        elif btn.index == 4:
                            print("entered 4")
                            menu = False
                            lvl4 = True
                            pg.time.delay(60)
                        elif btn.index == 5:
                            print("entered 5")
                            menu = False
                            lvl5 = True
                            pg.time.delay(60)
                        elif btn.index == 6:
                            print("entered 6")
                            menu = False
                            lvl6 = True
                            pg.time.delay(60)

    elif lvl1:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                if maze[player_pos[1] - 1][player_pos[0]] in [0, 2]:
                    player_pos[1] -= 1
            if event.key == pg.K_DOWN:
                if maze[player_pos[1] + 1][player_pos[0]] in [0, 2]:
                    player_pos[1] += 1
            if event.key == pg.K_LEFT:
                if maze[player_pos[1]][player_pos[0] - 1] in [0, 2]:
                    player_pos[0] -= 1
            if event.key == pg.K_RIGHT:
                if maze[player_pos[1]][player_pos[0] + 1] in [0, 2]:
                    player_pos[0] += 1

        window.blit(background_puzzle, (0, 0))
        for y, row in enumerate(maze):
            for x, cell in enumerate(row):
                if cell == 1:
                    pg.draw.rect(window, YELLOW, (x * cell_size, y * cell_size, cell_size, cell_size))
                elif maze[y][x] == 2:
                    pg.draw.rect(window, GREEN, (x * cell_size, y * cell_size, cell_size, cell_size))

        if maze[player_pos[1]][player_pos[0]] == 2:
            lvl1_complete = True

        pg.draw.rect(window, RED, (player_pos[0] * cell_size, player_pos[1] * cell_size, cell_size, cell_size))

        if lvl1_complete:
            for comp in completed_lst:
                window.blit(comp.image, comp.rect)

        for exit in exit_lst:
            window.blit(exit.image, exit.rect)

        pg.time.Clock().tick(30)

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_pos = pg.mouse.get_pos()
                for exit in exit_lst:
                    if exit.rect.collidepoint(click_pos) and lvl1:
                        lvl1 = False
                        menu = True
                        print("left 1")
                        pg.time.delay(200)
        pg.time.delay(50)

    elif lvl2:
        window.blit(background_puzzle, (0, 0))

        # Направления
        if event.type == pg.USEREVENT:
            ball_dx = ball_speed
            ball_dy = ball_speed

        keys = pg.key.get_pressed()

        # Движение платформы
        if keys[pg.K_LEFT] and paddle.left > 0:
            paddle.x -= paddle_speed
        if keys[pg.K_RIGHT] and paddle.right < width:
            paddle.x += paddle_speed

        # Движение мяча
        if ball_dx != 0 and ball_dy != 0:
            ball.x += ball_dx
            ball.y += ball_dy

        # Отскоки
        if ball.left <= 0 or ball.right >= width:
            ball_dx = -ball_dx
        if ball.top <= 0:
            ball_dy = -ball_dy
        if ball.colliderect(paddle):
            ball_dy = -ball_dy

        # Удары по блокам
        hit_index = ball.collidelist(bricks)
        if hit_index >= 0:
            brick = bricks[hit_index]
            if ball.centerx < brick.left or ball.centerx > brick.right:
                ball_dx = -ball_dx
            else:
                ball_dy = -ball_dy
            bricks.pop(hit_index)

        # Сброс мяча
        if ball.bottom >= height:
            reset_ball()
        level2()

        if not bricks:
            for comp in completed_lst:
                window.blit(comp.image, comp.rect)

        for exit in exit_lst:
            window.blit(exit.image, exit.rect)

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_pos = pg.mouse.get_pos()
                for exit in exit_lst:
                    if exit.rect.collidepoint(click_pos) and lvl2:
                        lvl2 = False
                        menu = True
                        print("left 2")
                        pg.time.delay(200)
    elif lvl3:
        game_over = False
        game_close = False
        window.blit(background_puzzle, (0, 0))
        x1 = width / 2
        y1 = height / 2

        x1_change = 0
        y1_change = 0

        snake_lst = []
        snake_len = 1

        applex = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        appley = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

        while not game_over:

            while game_close:
                message("You lost. Reenter to restart", WHITE)
                score(snake_len - 1)
                pg.display.update()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT and x1_change == 0:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pg.K_RIGHT and x1_change == 0:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pg.K_UP and y1_change == 0:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pg.K_DOWN and y1_change == 0:
                        y1_change = snake_block
                        x1_change = 0

            if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            pg.draw.rect(window, RED, [applex, appley, snake_block, snake_block])
            snake_Head = [x1, y1]
            snake_lst.append(snake_Head)

            if len(snake_lst) > snake_len:
                del snake_lst[0]

            for x in snake_lst[:-1]:
                if x == snake_Head:
                    game_close = True

            snake(snake_block, snake_lst)
            score(snake_len - 1)

            pg.display.update()

            if x1 == applex and y1 == appley:
                foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
                snake_len += 1

        for exit in exit_lst:
            window.blit(exit.image, exit.rect)

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_pos = pg.mouse.get_pos()
                for exit in exit_lst:
                    if exit.rect.collidepoint(click_pos) and lvl3:
                        lvl3 = False
                        menu = True
                        print("left 3")
                        pg.time.delay(200)
    elif lvl4:
        keys = pg.key.get_pressed()
        new_x, new_y = pac_pos[0], pac_pos[1]
        if keys[pg.K_LEFT] and can_move(new_x - pac_speed, new_y):
            new_x -= pac_speed
        if keys[pg.K_RIGHT] and can_move(new_x + pac_speed, new_y):
            new_x += pac_speed
        if keys[pg.K_UP] and can_move(new_x, new_y - pac_speed):
            new_y -= pac_speed
        if keys[pg.K_DOWN] and can_move(new_x, new_y + pac_speed):
            new_y += pac_speed

        if [new_x, new_y] != pac_pos:
            pac_pos = [new_x, new_y]
            eat_dot(new_x, new_y)

        if check_win():
            lvl4_complete

        window.blit(background_puzzle, (0, 0))

        if lvl4_complete:
            for comp in completed_lst:
                window.blit(comp.image, comp.rect)

        for y, row in enumerate(pac_map):
            for x, cell in enumerate(row):
                rect = pg.Rect(x * pac_wall, y * pac_wall, pac_wall, pac_wall)
                if cell == 1:
                    pg.draw.rect(window, BLUE, rect)
                elif cell == 2:
                    pg.draw.circle(window, WHITE, rect.center, 5)

        pacman_rect = pg.Rect(pac_pos[0] * pac_wall, pac_pos[1] * pac_wall, pac_wall, pac_wall)
        pg.draw.circle(window, YELLOW, pacman_rect.center, pac_wall // 2)

        for exit in exit_lst:
            window.blit(exit.image, exit.rect)

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_pos = pg.mouse.get_pos()
                for exit in exit_lst:
                    if exit.rect.collidepoint(click_pos) and lvl4:
                        lvl4 = False
                        menu = True
                        print("left 4")
                        pg.time.delay(200)
        pg.time.Clock().tick(12)

    clock.tick(FPS)
    pg.display.update()
