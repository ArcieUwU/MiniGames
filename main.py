import pygame as pg

pg.init()
width = 1280
height = 720

FPS = 60
clock = pg.time.Clock()

pg.display.set_caption("Puzzle Game")
window = pg.display.set_mode((width, height))

icon = pg.image.load("Images/icon_logo.png")
icon = pg.transform.scale(icon, (40, 40))

background_main = pg.image.load("Images/bg_main.jpg")

pg.display.set_icon(icon)
state = True

while state:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            state = False

    font = pg.font.Font("Fonts/ThisAppealFont.otf", 128)
    text = font.render("WORLD'S HARDEST PUZZLE GAME", 1, (255, 255, 255))
    window.blit(background_main, (0, 0))
    window.blit(text, (168, 64))

    clock.tick(FPS)
    pg.display.update()
