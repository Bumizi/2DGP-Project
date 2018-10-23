import game_framework
from pico2d import *
import level_select_state


name = "TitleState"
main_image = None
start_image = None
exit_image = None


class MainScreen:
    def __init__(self):
        self.image = load_image('RPS.png')

    def draw(self):
        self.image.clip_draw(0, 0, 512, 512, 400, 300, 800, 600)


class StartButton:
    def __init__(self):
        self.image = load_image('start.png')
        self.x, self.y = 100, 50

    def draw(self):
        self.image.clip_draw(0, 0, 900, 180, 300, 50, self.x, self.y)


class ExitButton:
    def __init__(self):
        self.image = load_image('exit.png')
        self.x, self.y = 100, 50

    def draw(self):
        self.image.clip_draw(0, 0, 900, 180, 500, 50, self.x, self.y)


def collision(x1, y1, x2, y2, px, py):
    if(x1 < px < x2 & y1 < py < y2):
        return True


def enter():
    global main_image, start_image, exit_image
    #image = load_image('RPS.png')
    main_image = MainScreen()
    start_image = StartButton()
    exit_image = ExitButton()
    pass


def exit():
    global main_image, start_image, exit_image
    del (main_image)
    del (start_image)
    del (exit_image)
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.push_state(level_select_state)
            #elif event.type == SDL_MOUSEBUTTONDOWN and collision(Draw_Button_Start.x, Draw_Button_Start.y, 500, 400, event.x, event.y):
                #pass
    pass


def draw():
    clear_canvas()
    main_image.draw()
    start_image.draw()
    exit_image.draw()
    update_canvas()
    pass







def update():
    pass


def pause():
    pass


def resume():
    pass






