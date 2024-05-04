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

background = pg.image.load("Images/background.png")
background = pg.transform.scale(background, (1280, 720))

background_puzzle = pg.image.load("Images/bg_puzzle.jpg")


pg.display.set_icon(icon)

btn_image = pg.image.load("Images/btn_img.png")

exit_img = pg.image.load("Images/exit.png")
exit_img = pg.transform.scale(exit_img, (64, 64))

name_text = pg.image.load("Images/name_text.png")

# class Background:
#     def __init__(self, x, y, image):
#         self.x = x
#         self.y = y
#         self.image = image
#         self.rect = pg.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
#
#     def remove(self):
#         for bg in bg_lst:
#             bg.rect.move_ip(5000, 0)
#
#     def draw(self):
#         for bg in bg_lst:
#             bg.rect.move_ip(-5000, 0)

# bg_lst = [Background(0, 0, "Images/bg_main.jpg"),
#           Background(5000, 0, "Images/bg_puzzle.jpg")]
class Name:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pg.image.load("Images/name_text.png")
        self.rect = pg.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def remove(self):
        for name in name_lst:
            name.rect.move_ip(-5000, 0)

    def draw(self):
        for btn in button_lst:
            btn.rect.move_ip(5000, 0)

name_lst = [Name(168, 48, "Images/name_text.png")]

class Level1:
    def __init__(self, x, y, xx, yy, image_path):
        self.x = x
        self.y = y
        self.xx = xx
        self.yy = yy
        self.image = image_path
        self.rect = pg.Rect(self.x, self.y, self.xx, self.yy)




class Button:

    def __init__(self, x, y, index, image_path):
        self.x = x
        self.y = y
        self.index = index
        self.image = pg.image.load(image_path)
        self.rect = pg.Rect(self.x, self.y, 244, 244)

    def remove(self):
        for btn in button_lst:
            btn.rect.move_ip(5000, 0)

    def draw(self):
        for btn in button_lst:
            btn.rect.move_ip(-5000, 0)



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
    window.blit(background, (0, 0))

    # for bg in bg_lst:
    #     window.blit(bg.image, bg.rect)

    for name in name_lst:
        window.blit(name.image, name.rect)

    for btn in button_lst:
        window.blit(btn.image, btn.rect)

    pos = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            state = False

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_pos = pg.mouse.get_pos()
                for btn in button_lst:
                    if btn.rect.collidepoint(click_pos):
                        background = pg.image.load("Images/bg_puzzle.jpg")
                        # Background.remove(bg)
                        Button.remove(btn)
                        Name.remove(name)
                        # if btn.index == 1:
                        #     1


    clock.tick(FPS)
    pg.display.update()
