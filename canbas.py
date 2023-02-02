import pygame as pg

pg.init()

width = 800
height = 500

screen = pg.display.set_mode((width, height))

clock = pg.time.Clock()


town_back = pg.image.load("IMAGE/town_back_dark.png")
wood_board = pg.image.load("IMAGE/wood_board.png")


def board_and_write(x, y, string):
    screen.blit(wood_board, (x,y))
    font = font = pg.font.Font("font/NanumGothicBold.otf", 20)
    write = font.render((string), True, (0,0,0))
    screen.blit(write,(x+20, y+15))
    return 0

def display_town():
    screen.blit(town_back, (0,0))
    board_and_write(100, 0, "레후")



running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    display_town()
    pg.display.update()
    
    clock.tick(60)

pg.quit()