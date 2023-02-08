import pygame as pg
import data_procress
import window_ui
import function_maker

pg.init()

width = 800
height = 500

screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()

town_back = pg.image.load("IMAGE/town_back_dark.png")
wood_board = pg.image.load("IMAGE/wood_board.png")
sojo = pg.image.load("IMAGE/sojo.png")
beer = pg.image.load("IMAGE/beer.png")


Window = window_ui.Window
Button = window_ui.Button
Image = window_ui.Image
Text_Window = window_ui.Text_Window
Image_button = window_ui.Image_button

OPEND_WINDOW = []


###오픈함수제작함수
def create_open_function(win):
    def open_function():
        global OPEND_WINDOW
        if OPEND_WINDOW and OPEND_WINDOW[0] == win:
            OPEND_WINDOW = []
        else:
            OPEND_WINDOW = [win]
    return open_function
##데이터 변경 함수 제작 함수
def xxx():
    data_procress.gold.gold-=1
    gold_box.string= str(data_procress.gold.gold)+" 골드"
    print(data_procress.gold.gold)


##스테이터스 윈도우
STATUS_WINDOW = Window()
status_text = "\n".join([f"{key}: {value}" for key, value in data_procress.status.data.items()])
status_text_win_b1 = Text_Window(400, 200, 300, 130, status_text, "font/NanumGothicBold.otf", 20, (255, 225, 225),screen, (0, 0, 0))
STATUS_WINDOW.text_windows = [status_text_win_b1]

##술집 윈도우
status_text_win_b2 = Text_Window(400, 300, 300, 130, "이곳은 술집이다\n어차피 모험가의 삶은 하루살이\n마음껏 마시자.", "font/NanumGothicBold.otf", 20, (255, 225, 225),screen, (0, 0, 0))
BEER_WINDOW = Window()
BEER_WINDOW.text_windows = [status_text_win_b2]
beer_button = Image_button(beer, 450, 100, screen, callback = xxx)
BEER_WINDOW.buttons=[beer_button]



        


b1_function = create_open_function(STATUS_WINDOW)
b2_function = create_open_function(BEER_WINDOW)


##타운 기본 윈도우
TOWN_WINDOW = Window()
b1 = Button(20, 50, "스테이터스를 보다", wood_board, screen,b1_function)
b2 = Button(20, 110, "술집에 가다", wood_board, screen, b2_function)
b3 = Button(20, 170, "상점에 가다", wood_board, screen)
b4 = Button(20, 230, "길드에 가다", wood_board, screen)
TOWN_WINDOW.buttons = [b1,b2,b3,b4]
town_text = Text_Window(20, 300, 300, 170, "마을이다 ㅇㅅㅇ.\n마을이라구 ㅇㅅㅇ.", "font/NanumGothicBold.otf", 20, (255, 225, 225),screen, (0, 0, 0))
gold_box = Text_Window(650, 20, 200, 50, str(data_procress.gold.gold)+" 골드", "font/NanumGothicBold.otf", 20, (255, 225, 225),screen, (0, 0, 0))
sojo_image = Image(sojo, 270, 0,screen)
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
            if OPEND_WINDOW:
                pressed = OPEND_WINDOW[0].handle_click(mouse_pos)
                if pressed:
                    pressed.callback()
        if event.type == pg.QUIT:
            running = False

    
    
    pg.display.update()
    
    clock.tick(20)

pg.quit()