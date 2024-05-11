import pygame as pg

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
lvl5 = False
lvl6 = False

pg.display.set_caption("Puzzle Game")
window = pg.display.set_mode((width, height))

icon = pg.image.load("Images/icon_logo.png")
icon = pg.transform.scale(icon, (40, 40))

background = pg.image.load("Images/background.png")
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


class Background:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pg.image.load(image)
        self.rect = pg.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def remove(self):
        for bg in background_lst:
            bg.rect.move_ip(5000, 0)

    def draw(self):
        for bg in background_lst:
            bg.rect.move_ip(-5000, 0)


background_lst = [Background(0, 0, "Images/bg_main.jpg"), Background(5000, 0, "Images/bg_puzzle.jpg")]

class Name:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pg.image.load("Images/name_text.png")
        self.rect = pg.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def draw(self):
        for btn in button_lst:
            btn.rect.move_ip(5000, 0)


    def remove(self):
        for name in name_lst:
            name.rect.move_ip(-5000, 0)


name_lst = [Name(168, 48, "Images/name_text.png")]

class Level1:
    def __init__(self, x, y, xx, yy, image_path):
        self.x = x
        self.y = y
        self.xx = xx
        self.yy = yy
        self.image = image_path
        self.rect = pg.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())


class Button:

    def __init__(self, x, y, index, image_path):
        self.x = x
        self.y = y
        self.index = index
        self.image = pg.image.load(image_path)
        self.rect = pg.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def draw(self):
        for btn in button_lst:
            btn.rect.move_ip(5000, 0)

    def remove(self):
        for btn in button_lst:
            btn.rect.move_ip(-5000, 0)


class Exit:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pg.image.load(image)
        self.rect = pg.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def draw(self):
        for exit in exit_lst:
            exit.rect.move_ip(-5000, 0)

    def remove(self):
        for exit in exit_lst:
            exit.rect.move_ip(5000, 0)


exit_lst = [Exit(6200, 16, "Images/exit.png")]


button_lst = [Button(12, 12, 1, "Images/btn_images/btn_image1.png"),
              Button(436, 12, 2, "Images/btn_images/btn_image2.png"),
              Button(860, 12, 3, "Images/btn_images/btn_image3.png"),
              Button(12, 366, 4, "Images/btn_images/btn_image4.png"),
              Button(436, 366, 5, "Images/btn_images/btn_image5.png"),
              Button(860, 366, 6, "Images/btn_images/btn_image6.png"),]

while state:
    window.blit(background, (0, 0))
    pos = pg.mouse.get_pos()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            state = False

    if main:
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
                        print("1")
                        main = False
                        menu = True
                        pg.time.delay(60)

    elif menu:
        background = pg.image.load("Images/bg_main.jpg")
        for btn in button_lst:
            window.blit(btn.image, btn.rect)

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_pos = pg.mouse.get_pos()
                for btn in button_lst:
                    if btn.rect.collidepoint(click_pos) and menu:
                        if btn.index == 1:
                            print("1")
                            menu = False
                            lvl1 = True
                            pg.time.delay(60)
                        elif btn.index == 2:
                            print("2")
                            menu = False
                            lvl2 = True
                            pg.time.delay(60)
                        elif btn.index == 3:
                            print("3")
                            menu = False
                            lvl3 = True
                            pg.time.delay(60)
                        elif btn.index == 4:
                            print("4")
                            menu = False
                            lvl4 = True
                            pg.time.delay(60)
                        elif btn.index == 5:
                            print("5")
                            menu = False
                            lvl5 = True
                            pg.time.delay(60)
                        elif btn.index == 6:
                            print("6")
                            menu = False
                            lvl6 = True
                            pg.time.delay(60)

    # elif lvl1:
    # elif lvl2:
    # elif lvl3:
    # elif lvl4:
    # elif lvl5:
    # elif lvl6:



    clock.tick(FPS)
    pg.display.update()
