import pygame as pg

pg.init()

width = 800
height = 500

screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()

town_back = pg.image.load("IMAGE/town_back_dark.png")
wood_board = pg.image.load("IMAGE/wood_board.png")


class Window:
    def __init__(self, x=0, y=0, width=None, height=None, buttons=[], text_windows=[], images=[]):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.buttons = buttons
        self.text_windows = text_windows
        self.images = images

    def blit(self):
        for text_window in self.text_windows:
            text_window.blit()
        for image in self.images:
            screen.blit()
        for button in self.buttons:
            button.blit()

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


class Text_Window:
    def __init__(self, x, y, width, height, string, font_path, font_size, color, bg_color=(255, 255, 255)):
        self.string = string
        self.font_path = font_path
        self.font_size = font_size
        self.color = color
        self.x = x
        self.y = y
        self.rect = pg.Rect(x, y, width, height)
        self.surface = pg.Surface((width, height))
        self.surface.fill(bg_color)
        self.surface.set_alpha(128)

    def blit(self):
        screen.blit(self.surface, self.rect)
        font = pg.font.Font(self.font_path, self.font_size)
        lines = self.string.split("\n")
        y_offset = 0
        for line in lines:
            line_surface = font.render(line, True, self.color)
            line_rect = line_surface.get_rect(topleft=(self.x, self.y + y_offset))
            screen.blit(line_surface, line_rect)
            y_offset += self.font_size

        


b1 = Button(20, 50, "스테이터스를 보다")
b2 = Button(20, 110, "술집에 가다")
b3 = Button(20, 170, "상점에 가다")
b4 = Button(20, 230, "길드에 가다")
TOWN_WINDOW = Window()
TOWN_WINDOW.buttons = [b1,b2,b3,b4]
OPEN_WINDOW = None

tt = Text_Window(300, 300, 200, 200, "Hello Woㅇㄴㄹㅇ\nㄴㄹㄴㄹㅇㄹㄴㅇㄴrld!", "font/NanumGothicBold.otf", 20, (255, 225, 225), (0, 0, 0))
TOWN_WINDOW.text_windows = [tt]

running = True
while running:
    screen.blit(town_back, (0,0))
    TOWN_WINDOW.blit()
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
    
    clock.tick(20)

pg.quit()