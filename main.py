import pygame as pg

pg.init()
width = 1280
height = 720

FPS = 60
clock = pg.time.Clock()

WHITE = (255, 255, 255)

state = True

pg.display.set_caption("Puzzle Game")
window = pg.display.set_mode((width, height))

icon = pg.image.load("Images/icon_logo.png")
icon = pg.transform.scale(icon, (40, 40))

background_main = pg.image.load("Images/bg_main.jpg")
background_main = pg.transform.scale(background_main, (1280, 720))

background_puzzle = pg.image.load("Images/bg_puzzle.jpg")

pos = pg.mouse.get_pos()

pg.display.set_icon(icon)

lvl1 = pg.image.load("Images/btn_img.png")
lvl1 = pg.transform.scale(lvl1, (244, 244))
lvl1_rect = pg.Rect(10, 212, 244, 244)

lvl2 = pg.image.load("Images/btn_img.png")
lvl2 = pg.transform.scale(lvl2, (244, 244))
lvl2_rect = pg.Rect(264, 212, 244, 244)

lvl3 = pg.image.load("Images/btn_img.png")
lvl3 = pg.transform.scale(lvl3, (244, 244))
lvl3_rect = pg.Rect(518, 212, 244, 244)

lvl4 = pg.image.load("Images/btn_img.png")
lvl4 = pg.transform.scale(lvl4, (244, 244))
lvl4_rect = pg.Rect(772, 212, 244, 244)

lvl5 = pg.image.load("Images/btn_img.png")
lvl5 = pg.transform.scale(lvl5, (244, 244))
lvl5_rect = pg.Rect(1026, 212, 244, 244)

lvl6 = pg.image.load("Images/btn_img.png")
lvl6 = pg.transform.scale(lvl6, (244, 244))
lvl6_rect = pg.Rect(10, 466, 244, 244)

lvl7 = pg.image.load("Images/btn_img.png")
lvl7 = pg.transform.scale(lvl7, (244, 244))
lvl7_rect = pg.Rect(264, 466, 244, 244)

lvl8 = pg.image.load("Images/btn_img.png")
lvl8 = pg.transform.scale(lvl8, (244, 244))
lvl8_rect = pg.Rect(518, 466, 244, 244)

lvl9 = pg.image.load("Images/btn_img.png")
lvl9 = pg.transform.scale(lvl9, (244, 244))
lvl9_rect = pg.Rect(772, 466, 244, 244)

lvl10 = pg.image.load("Images/btn_img.png")
lvl10 = pg.transform.scale(lvl10, (244, 244))
lvl10_rect = pg.Rect(1026, 466, 244, 244)

while state:

    font = pg.font.Font("Fonts/ThisAppealFont.otf", 128)
    lvl_font = pg.font.SysFont("Arial", 144)
    text = font.render("WORLD'S HARDEST PUZZLE GAME", 1, (255, 255, 255))
    window.blit(background_main, (0, 0))
    window.blit(text, (168, 48))

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

    window.blit(lvl1, (10, 212))
    window.blit(btn1_txt, (100, 254))

    window.blit(lvl2, (264, 212))
    window.blit(btn2_txt, (356, 254))

    window.blit(lvl3, (518, 212))
    window.blit(btn3_txt, (610, 254))

    window.blit(lvl4, (772, 212))
    window.blit(btn4_txt, (864, 254))

    window.blit(lvl5, (1026, 212))
    window.blit(btn5_txt, (1118, 254))

    window.blit(lvl6, (10, 466))
    window.blit(btn6_txt, (100, 506))

    window.blit(lvl7, (264, 466))
    window.blit(btn7_txt, (356, 506))

    window.blit(lvl8, (518, 466))
    window.blit(btn8_txt, (610, 506))

    window.blit(lvl9, (772, 466))
    window.blit(btn9_txt, (864, 506))

    window.blit(lvl10, (1026, 466))
    window.blit(btn10_txt, (1084, 506))

    pos = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            state = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if lvl1_rect.collidepoint(pos):
                    window.blit(background_puzzle, (0, 0))

                elif lvl2_rect.collidepoint(pos):
                    window.blit(background_puzzle, (0, 0))

                elif lvl3_rect.collidepoint(pos):
                    window.blit(background_puzzle, (0, 0))

                elif lvl4_rect.collidepoint(pos):
                    window.blit(background_puzzle, (0, 0))

                elif lvl5_rect.collidepoint(pos):
                    window.blit(background_puzzle, (0, 0))

                elif lvl6_rect.collidepoint(pos):
                    window.blit(background_puzzle, (0, 0))

                elif lvl7_rect.collidepoint(pos):
                    window.blit(background_puzzle, (0, 0))

                elif lvl8_rect.collidepoint(pos):
                    window.blit(background_puzzle, (0, 0))

                elif lvl9_rect.collidepoint(pos):
                    window.blit(background_puzzle, (0, 0))

                elif lvl10_rect.collidepoint(pos):
                    window.blit(background_puzzle, (0, 0))

    clock.tick(FPS)
    pg.display.update()
