###오픈함수제작함수
def create_open_function(win):
    def open_function(OPEND_WINDOW):
        if OPEND_WINDOW and OPEND_WINDOW[0] == win:
            OPEND_WINDOW = []
        else:
            OPEND_WINDOW = [win]
    return open_function