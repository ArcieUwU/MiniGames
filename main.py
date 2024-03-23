import pygame as pg

pg.init()
width = 1296
height = 720

FPS = 60
clock = pg.time.Clock()

pg.display.set_caption("Puzzle Game")
window = pg.display.set_mode((width, height))

icon = pg.image.load("Images/icon_logo.png")
icon = pg.transform.scale(icon, (40, 40))

background_main = pg.image.load("Images/bg_main.jpg")
background_main = pg.transform.scale(background_main, (1296, 720))

pg.display.set_icon(icon)
state = True

lvl1 = pg.image.load("Images/btn_img.png")
lvl1 = pg.transform.scale(lvl1, (420, 444))

lvl2 = pg.image.load("Images/btn_img.png")
lvl2 = pg.transform.scale(lvl1, (420, 444))

lvl3 = pg.image.load("Images/btn_img.png")
lvl3 = pg.transform.scale(lvl1, (420, 444))

lvl4 = pg.image.load("Images/btn_img.png")
lvl4 = pg.transform.scale(lvl1, (420, 444))

lvl5 = pg.image.load("Images/btn_img.png")
lvl5 = pg.transform.scale(lvl1, (420, 444))

lvl6 = pg.image.load("Images/btn_img.png")
lvl6 = pg.transform.scale(lvl1, (420, 444))

lvl7 = pg.image.load("Images/btn_img.png")
lvl7 = pg.transform.scale(lvl1, (420, 444))

lvl8 = pg.image.load("Images/btn_img.png")
lvl8 = pg.transform.scale(lvl1, (420, 444))

lvl9 = pg.image.load("Images/btn_img.png")
lvl9 = pg.transform.scale(lvl1, (420, 444))

lvl10 = pg.image.load("Images/btn_img.png")
lvl10 = pg.transform.scale(lvl1, (420, 444))

while state:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            state = False

    font = pg.font.Font("Fonts/ThisAppealFont.otf", 128)
    lvl_font = pg.font.SysFont("Arial", 320)
    text = font.render("WORLD'S HARDEST PUZZLE GAME", 1, (255, 255, 255))
    window.blit(background_main, (0, 0))
    window.blit(text, (168, 64))

    btn1_txt = lvl_font.render("1", 1, (255, 255, 255))
    btn2_txt = lvl_font.render("2", 1, (255, 255, 255))
    btn3_txt = lvl_font.render("3", 1, (255, 255, 255))
    btn4_txt = lvl_font.render("4", 1, (255, 255, 255))
    btn5_txt = lvl_font.render("5", 1, (255, 255, 255))
    btn6_txt = lvl_font.render("6", 1, (255, 255, 255))
    btn7_txt = lvl_font.render("7", 1, (255, 255, 255))
    btn8_txt = lvl_font.render("8", 1, (255, 255, 255))
    btn9_txt = lvl_font.render("9", 1, (255, 255, 255))
    btn10_txt = lvl_font.render("10", 1, (255, 255, 255))

    window.blit(lvl1, (8, 256))
    window.blit(btn1_txt, (156, 296))

    window.blit(lvl2, (438, 256))
    window.blit(btn2_txt, (586, 296))

    window.blit(lvl3, (868, 256))
    window.blit(btn3_txt, (1016, 296))

    window.blit(lvl4, (1298, 256))
    window.blit(btn4_txt, (1446, 296))

    window.blit(lvl5, (1728, 256))
    window.blit(btn5_txt, (1876, 296))

    window.blit(lvl6, (2158, 256))
    window.blit(btn6_txt, (2306, 296))

    window.blit(lvl7, (2588, 256))
    window.blit(btn7_txt, (2736, 296))

    window.blit(lvl8, (3018, 256))
    window.blit(btn8_txt, (3166, 296))

    window.blit(lvl9, (3448, 256))
    window.blit(btn9_txt, (3596, 296))

    window.blit(lvl10, (3878, 256))
    window.blit(btn10_txt, (3986, 296))

    clock.tick(FPS)
    pg.display.update()
