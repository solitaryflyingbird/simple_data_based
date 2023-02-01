import pygame as pg

pg.init()

width = 800
height = 500

screen = pg.display.set_mode((width, height))

clock = pg.time.Clock()


down_back = pg.image.load("IMAGE/town_back_dark.png")
def display_town():
    screen.blit(down_back, (0,0))



running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    display_town()
    pg.display.update()
    
    clock.tick(60)

pg.quit()