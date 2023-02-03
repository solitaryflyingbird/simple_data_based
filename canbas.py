import pygame as pg

pg.init()

width = 800
height = 500

screen = pg.display.set_mode((width, height))

clock = pg.time.Clock()


town_back = pg.image.load("IMAGE/town_back_dark.png")
wood_board = pg.image.load("IMAGE/wood_board.png")


class BoardAndWrite:
    def __init__(self, x, y, string):
        self.wood_board_rect = wood_board.get_rect(topleft=(x, y))
        screen.blit(wood_board, self.wood_board_rect.topleft)
        font = pg.font.Font("font/NanumGothicBold.otf", 20)
        self.write = font.render((string), True, (0,0,0))
        self.text_rect = self.write.get_rect(topleft=(x+20, y+15))
        screen.blit(self.write, self.text_rect.topleft)
    def board_blit(self):
        screen.blit(wood_board, self.wood_board_rect.topleft)
        screen.blit(self.write, self.text_rect.topleft)

def display_town_button():   
    b1 = BoardAndWrite(100, 50, "스테이터스를 보다")
    b2 = BoardAndWrite(100, 110, "술집에 가다")
    b3 = BoardAndWrite(100, 170, "상점에 가다")
    b4 = BoardAndWrite(100, 170, "길드에 가다")
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
            pressed = button_cog
            if pressed:
                print(pressed, 111)
        if event.type == pg.QUIT:
            running = False
    
    
    pg.display.update()
    
    clock.tick(60)

pg.quit()