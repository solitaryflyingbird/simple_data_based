import pygame as pg
import data_process
import window_ui
import battle


pg.init()

width = 800
height = 500

screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()

town_back = pg.image.load("IMAGE/town_back_dark.png")
wood_board = pg.image.load("IMAGE/wood_board.png")
sojo = pg.image.load("IMAGE/sojo.png")
beer = pg.image.load("IMAGE/beer.png")
tobul = pg.image.load("IMAGE/tobul.png")


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
def make_change_function_gold(change_num):
    def change_function():
        data_process.gold.gold += change_num
        gold_box.string= str(data_process.gold.gold)+" 골드"
    return change_function
def make_change_function_day(change_num):
    def change_function():
        data_process.day.day += change_num
    return change_function
def make_change_function_status(attribute, change_num):
    def change_function():
        data_process.status.status_update(attribute, change_num)
        status_text_win_b1.string = "\n".join([f"{key}: {value}" for key, value in data_process.status.data.items()])
        beer_point.string = "취기 : " + str(data_process.status.data["drunk"])
    return change_function
def merge_functions(*functions):
    def merged_function(*args, **kwargs):
        for func in functions:
            func(*args, **kwargs)
    return merged_function



##스테이터스 윈도우
STATUS_WINDOW = Window()
status_text = "\n".join([f"{key}: {value}" for key, value in data_process.status.data.items()])
status_text_win_b1 = Text_Window(400, 200, 300, 140, status_text, "font/NanumGothicBold.otf", 20, (255, 225, 225),screen, (0, 0, 0))
STATUS_WINDOW.text_windows = [status_text_win_b1]



##술집 윈도우
status_text_win_b2 = Text_Window(400, 300, 300, 130, "이곳은 술집이다\n어차피 모험가의 삶은 하루살이\n마음껏 마시자.", "font/NanumGothicBold.otf", 20, (255, 225, 225),screen, (0, 0, 0))
beer_point = Text_Window(460, 270, 130, 25, "취기 : " + str(data_process.status.data["drunk"]), "font/NanumGothicBold.otf", 20, (255, 225, 225),screen, (0, 0, 0))
BEER_WINDOW = Window()
BEER_WINDOW.text_windows = [status_text_win_b2,beer_point]
##술집윈도우 기능
def beer_try():
    if data_process.gold.gold<1:
        status_text_win_b2.string = "돈이 부족하다"
    elif data_process.status.data["drunk"]>9:
        status_text_win_b2.string = "너무 취헀다"
    else:
        beer_drink()
beer_drink = merge_functions(make_change_function_status("drunk", 1),make_change_function_gold(-1))
beer_button = Image_button(beer, 450, 100, screen, callback = beer_try)    
BEER_WINDOW.buttons=[beer_button]


#길드 윈도우
GUILD_WINDOW = Window()
guild_text = Text_Window(400, 300, 300, 130, "이곳은 길드다\n원하는 임무를 클릭해보자.", "font/NanumGothicBold.otf", 20, (255, 225, 225),screen, (0, 0, 0))
GUILD_WINDOW.text_windows = [guild_text]
import quest_maker

def battle_click_function_maker(quest, quest_manager, random_quest_window_button_1, random_quest_window_button_2):
    def battle_function():
        my_char = battle.my_character(data_process.name.name, data_process.status.data, data_process.status.skill_data)
        monsters = battle.make_monsters(quest.monster_name, quest.status, quest.monster_num)
        xx= battle.Combat(my_char,monsters,quest.gold_reward)
        xx.simulate()
        result = xx.return_result()
        quest_manager.quest_load()
        random_quest_window_button_1.load(quest_manager.quest1.quest_name)
        random_quest_window_button_2.load(quest_manager.quest2.quest_name)
        print(result)
        print(quest_manager.quest1.quest_name)
        return result
    return battle_function



quest_manager = quest_maker.quest_manager('./MONSTER/D')
random_quest_window_button_1 = Text_Window(400, 100, 300, 50, quest_manager.quest1.quest_name, "font/NanumGothicBold.otf", 20, (255, 225, 225),screen, (0, 0, 0))
random_quest_window_button_2 = Text_Window(400, 200, 300, 50, quest_manager.quest2.quest_name, "font/NanumGothicBold.otf", 20, (255, 225, 225),screen, (0, 0, 0))
GUILD_WINDOW.text_windows.append(random_quest_window_button_1)
GUILD_WINDOW.text_windows.append(random_quest_window_button_2)

guild_b1_function = battle_click_function_maker(quest_manager.quest1, quest_manager, random_quest_window_button_1, random_quest_window_button_2)
guild_b2_function = battle_click_function_maker(quest_manager.quest2, quest_manager, random_quest_window_button_1, random_quest_window_button_2)

guild_b1 = Image_button(tobul, 400, 150, screen, guild_b1_function)
guild_b2 = Image_button(tobul, 400, 250, screen, guild_b2_function)
GUILD_WINDOW.buttons.append(guild_b1)
print(STATUS_WINDOW.buttons)
GUILD_WINDOW.buttons.append(guild_b2)



print(STATUS_WINDOW.buttons == GUILD_WINDOW.buttons)


b1_function = create_open_function(STATUS_WINDOW)
b2_function = create_open_function(BEER_WINDOW)
b4_function = create_open_function(GUILD_WINDOW)
##타운 기본 윈도우
TOWN_WINDOW = Window()
town_b1 = Button(20, 50, "스테이터스를 보다", wood_board, screen,b1_function)
town_b2 = Button(20, 110, "술집에 가다", wood_board, screen, b2_function)
town_b3 = Button(20, 170, "상점에 가다", wood_board, screen)
town_b4 = Button(20, 230, "길드에 가다", wood_board, screen, b4_function)
TOWN_WINDOW.buttons = [town_b1,town_b2,town_b3,town_b4]
town_text = Text_Window(20, 300, 300, 170, "마을이다 ㅇㅅㅇ.\n마을이라구 ㅇㅅㅇ.", "font/NanumGothicBold.otf", 20, (255, 225, 225),screen, (0, 0, 0))
gold_box = Text_Window(650, 20, 200, 50, str(data_process.gold.gold)+" 골드", "font/NanumGothicBold.otf", 20, (255, 225, 225),screen, (0, 0, 0))
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