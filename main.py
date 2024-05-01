import pygame as pg

pg.init()
width = 1280
height = 720

FPS = 60
clock = pg.time.Clock()

state = True

pg.display.set_caption("Puzzle Game")
window = pg.display.set_mode((width, height))

icon = pg.image.load("Images/icon_logo.png")
icon = pg.transform.scale(icon, (40, 40))

background = pg.image.load("Images/bg_main.jpg")
background = pg.transform.scale(background, (1280, 720))

background_puzzle = pg.image.load("Images/bg_puzzle.jpg")

pos = pg.mouse.get_pos()

pg.display.set_icon(icon)

btn_image = pg.image.load("Images/btn_img.png")

background_img = pg.image.load("Images/bg_main.jpg")

exit_img = pg.image.load("Images/exit.png")
exit_img = pg.transform.scale(exit_img, (64, 64))

class Button:

    def __init__(self, x, y, index, image_path):
        self.x = x
        self.y = y
        self.index = index
        self.image = pg.image.load(image_path)
        self.rect = pg.Rect(self.x, self.y, 244, 244)


button_lst = [Button(10, 212, 1, "Images/btn_images/btn_icon1.png"),
              Button(264, 212, 2, "Images/btn_images/btn_icon2.png"),
              Button(518, 212, 3, "Images/btn_images/btn_icon3.png"),
              Button(772, 212, 4, "Images/btn_images/btn_icon4.png"),
              Button(1026, 212, 5, "Images/btn_images/btn_icon5.png"),
              Button(10, 466, 6, "Images/btn_images/btn_icon6.png"),
              Button(264, 466, 7, "Images/btn_images/btn_icon7.png"),
              Button(518, 466, 8, "Images/btn_images/btn_icon8.png"),
              Button(772, 466, 9, "Images/btn_images/btn_icon9.png"),
              Button(1026, 466, 10, "Images/btn_images/btn_icon10.png")]

while state:

    font = pg.font.Font("Fonts/ThisAppealFont.otf", 128)
    lvl_font = pg.font.SysFont("Arial", 144)
    text = font.render("WORLD'S HARDEST PUZZLE GAME", 1, (255, 255, 255))
    window.blit(background, (0, 0))
    window.blit(text, (168, 48))

    for btn in button_lst:
        window.blit(btn.image, btn.rect)

    pos = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            state = False

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if pg.Rect.collidepoint(event.pos):
                    background = pg.image.load("Images/bg_puzzle.jpg")
                    for index in button_lst:
                        if index == 1:
                            window.blit(exit_img, (1192, 24))

                        elif index == 2:
                            window.blit(exit_img, (1192, 24))

                        elif index == 3:
                            window.blit(exit_img, (1192, 24))

                        elif index == 4:
                            window.blit(exit_img, (1192, 24))

                        elif index == 5:
                            window.blit(exit_img, (1192, 24))

                        elif index == 6:
                            window.blit(exit_img, (1192, 24))

                        elif index == 7:
                            window.blit(exit_img, (1192, 24))

                        elif index == 8:
                            window.blit(exit_img, (1192, 24))

                        elif index == 9:
                            window.blit(exit_img, (1192, 24))

                        elif index == 10:
                            window.blit(exit_img, (1192, 24))

    clock.tick(FPS)
    pg.display.update()
