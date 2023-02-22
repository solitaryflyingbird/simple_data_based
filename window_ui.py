import pygame as pg

class Window:
    def __init__(self, x=0, y=0, width=None, height=None, buttons=None, text_windows=None, images=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.buttons = buttons.copy() if buttons is not None else []
        self.text_windows = text_windows.copy() if text_windows is not None else []
        self.images = images.copy() if images is not None else []
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
    def text_window_reset(self):
        for tw in self.text_windows:
            if tw.reset == True:
                tw.string = tw.origin_string




class Text_Window:
    def __init__(self, x, y, width, height, string, font_path, font_size, color,screen, bg_color=(255, 255, 255), reset = False):
        self.reset = reset
        self.screen = screen
        self.origin_string = string
        self.string = self.origin_string
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
        self.screen.blit(self.surface, self.rect)
        font = pg.font.Font(self.font_path, self.font_size)
        lines = self.string.split("\n")
        y_offset = 0
        for line in lines:
            line_surface = font.render(line, True, self.color)
            line_rect = line_surface.get_rect(topleft=(self.x, self.y + y_offset))
            self.screen.blit(line_surface, line_rect)
            y_offset += self.font_size  
    def load(self, string):
        self.string = string

class Image():
    def __init__(self, image, x, y, screen):
        self.screen = screen
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(x, y))
    def blit(self):
        self.screen.blit(self.image, self.rect)

        
class Button:
    def __init__(self, x, y, string, board, screen, callback = lambda: None):
        self.board = board
        self.screen = screen
        self.string = string
        self.wood_board_rect = board.get_rect(topleft=(x, y))
        font = pg.font.Font("font/NanumGothicBold.otf", 20)
        self.write = font.render((string), True, (0,0,0))
        self.text_rect = self.write.get_rect(topleft=(x+20, y+15))
        self.callback = callback
    def blit(self):
        self.screen.blit(self.board, self.wood_board_rect.topleft)
        self.screen.blit(self.write, self.text_rect.topleft)
    def collidepoint(self, point):
        return self.wood_board_rect.collidepoint(point)
    def func_load(self, callback):
        self.callback = callback


class Image_button():
    def __init__(self, image, x, y, screen, callback = lambda: None):
        self.screen = screen
        self.image = image
        self.callback = callback
        self.image_rect = image.get_rect(topleft=(x, y))
        self.rect = self.image.get_rect(topleft=(x, y))
    def blit(self):
        self.screen.blit(self.image, self.image_rect)
    def collidepoint(self, point):
        return self.image_rect.collidepoint(point)
    def func_load(self, callback):
        self.callback = callback

