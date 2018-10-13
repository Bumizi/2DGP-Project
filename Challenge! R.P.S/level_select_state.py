import game_framework
from pico2d import *
import main_state


name = "LevelSelectState"
image = None


class MainScreen:
    def __init__(self):
        self.image = load_image('RPS.png')

    def draw(self):
        self.image.draw(300, 300)


class StartButton:
    def __init__(self):
        self.image = load_image('start-exit.jpg')
        self.x, self.y = 100, 100

    def draw(self):
        self.image.clip_draw(0, 225, 950, 450, self.x, self.y)


class ExitButton:
    def __init__(self):
        self.image = load_image('start-exit.jpg')
        self.x, self.y = 500, 100

    def draw(self):
        self.image.clip_draw(0, 450, 950, 225, self.x, self.y)


def collision(x1, y1, x2, y2, px, py):
    if(x1 < px < x2 & y1 < py < y2):
        return True


def enter():
    global image
    image = load_image('start-exit.jpg')
    pass


def exit():
    global image
    del(image)
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            #elif event.type == SDL_MOUSEBUTTONDOWN and collision(Draw_Button_Start.x, Draw_Button_Start.y, 500, 400, event.x, event.y):
                #pass
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)
    pass


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    pass







def update():
    pass


def pause():
    pass


def resume():
    pass






