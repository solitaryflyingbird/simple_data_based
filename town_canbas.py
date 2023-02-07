import pygame as pg
import data_procress

pg.init()

width = 800
height = 500

screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()

town_back = pg.image.load("IMAGE/town_back_dark.png")
wood_board = pg.image.load("IMAGE/wood_board.png")
sojo = pg.image.load("IMAGE/sojo.png")

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
            image.blit()
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
        self.surface.set_alpha(198)

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
class Image:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(x, y))

    def blit(self):
        screen.blit(self.image, self.rect)


OPEND_WINDOW = []


##스테이터스 윈도우
STATUS_WINDOW = Window()
status_text = "\n".join([f"{key}: {value}" for key, value in data_procress.status.data.items()])
status_text_win = Text_Window(400, 200, 300, 130, status_text, "font/NanumGothicBold.otf", 20, (255, 225, 225), (0, 0, 0))
STATUS_WINDOW.text_windows = [status_text_win]

def b1_function():
    global OPEND_WINDOW
    if OPEND_WINDOW== []:
        OPEND_WINDOW.append(STATUS_WINDOW)
        print(OPEND_WINDOW, 111)
    else:
        OPEND_WINDOW = []


##타운 기본 윈도우
TOWN_WINDOW = Window()
b1 = Button(20, 50, "스테이터스를 보다",b1_function)
b2 = Button(20, 110, "술집에 가다")
b3 = Button(20, 170, "상점에 가다")
b4 = Button(20, 230, "길드에 가다")
TOWN_WINDOW.buttons = [b1,b2,b3,b4]
town_text = Text_Window(20, 300, 300, 170, "마을이다 ㅇㅅㅇ.\n마을이라구 ㅇㅅㅇ.", "font/NanumGothicBold.otf", 20, (255, 225, 225), (0, 0, 0))
gold_box = Text_Window(650, 20, 200, 50, str(data_procress.gold.gold)+" 골드", "font/NanumGothicBold.otf", 20, (255, 225, 225), (0, 0, 0))
sojo_image = Image(sojo, 270, 0,)
TOWN_WINDOW.text_windows = [town_text, gold_box]
TOWN_WINDOW.images = [sojo_image]






running = True
while running:
    screen.blit(town_back, (0,0))
    TOWN_WINDOW.blit()
    if OPEND_WINDOW:
        OPEND_WINDOW[0].blit()
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