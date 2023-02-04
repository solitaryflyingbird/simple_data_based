import pygame as pg

pg.init()

width = 800
height = 500

screen = pg.display.set_mode((width, height))

clock = pg.time.Clock()


town_back = pg.image.load("IMAGE/town_back_dark.png")
wood_board = pg.image.load("IMAGE/wood_board.png")


class Window:
    def __init__(self, x=0, y=0, width=None, height=None, buttons=None, text_windows=None, images=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.buttons = buttons
        self.text_windows = text_windows
        self.images = images

    def blit(self, screen):
        for button in self.buttons:
            button.blit(screen, self.x, self.y)
        for text_window in self.text_windows:
            text_window.blit(screen, self.x, self.y)
        for image in self.images:
            screen.blit(image.image, (image.x + self.x, image.y + self.y))

    def handle_click(self, mouse_pos):
        for button in self.buttons:
            button_click = button.collidepoint(mouse_pos)
            if button_click:
                return button


class Button:
    def __init__(self, x, y, string, callback = lambda: None):
        self.string = string
        self.wood_board_rect = wood_board.get_rect(topleft=(x, y))
        font = pg.font.Font("font/NanumGothicBold.otf", 20)
        self.write = font.render((string), True, (0,0,0))
        self.text_rect = self.write.get_rect(topleft=(x+20, y+15))
        self.callback = callback
        screen.blit(wood_board, self.wood_board_rect.topleft)
        screen.blit(self.write, self.text_rect.topleft)


    def blit(self):
        screen.blit(wood_board, self.wood_board_rect.topleft)
        screen.blit(self.write, self.text_rect.topleft)

    def collidepoint(self, point):
        return self.wood_board_rect.collidepoint(point)
b1 = Button(100, 50, "스테이터스를 보다")
b2 = Button(100, 110, "술집에 가다")
b3 = Button(100, 170, "상점에 가다")
b4 = Button(100, 230, "길드에 가다")
TOWN_WINDOW = Window()
TOWN_WINDOW.buttons = [b1,b2,b3,b4]
def xxx():
    print(1)
def display_town_button():   
    b1 = Button(100, 50, "스테이터스를 보다")
    b2 = Button(100, 110, "술집에 가다")
    b3 = Button(100, 170, "상점에 가다")
    b4 = Button(100, 230, "길드에 가다")
    return [b1, b2, b3, b4]
def button_cog(mouse_pos, buttons):
    for bt in buttons:
        if bt.wood_board_rect.collidepoint(mouse_pos):
            return bt
    return False

running = True
while running:
    screen.blit(town_back, (0,0))
    town_buttons = display_town_button()
    for event in pg.event.get():
        mouse_pressed = pg.mouse.get_pressed()[0]
        if mouse_pressed:
            mouse_pos = pg.mouse.get_pos()
            pressed = TOWN_WINDOW.handle_click(mouse_pos)
            if pressed:
                pressed.callback()
                print(pressed.string)
        if event.type == pg.QUIT:
            running = False
    
    
    pg.display.update()
    
    clock.tick(60)

pg.quit()