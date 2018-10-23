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
        self.x, self.y, self.w, self.h = 300, 50, 100, 50

    def draw(self):
        self.image.clip_draw(0, 0, 900, 180, self.x, self.y, self.w, self.h)


class ExitButton:
    def __init__(self):
        self.image = load_image('exit.png')
        self.x, self.y, self.w, self.h = 500, 50, 100, 50

    def draw(self):
        self.image.clip_draw(0, 0, 900, 180, self.x, self.y, self.w, self.h)


def collision(x1, y1, x2, y2, px, py):
    new_x1 = x1-x2/2
    new_y1 = y1+y2/2
    new_x2 = x1+x2/2
    new_y2 = y1-y2/2
    if(new_x1 < px and px < new_x2 and new_y1 > py and py > new_y2):
        return True


def enter():
    global main_image, start_image, exit_image
    main_image = MainScreen()
    start_image = StartButton()
    exit_image = ExitButton()
    pass


def exit():
    global main_image, start_image, exit_image
    del main_image
    del start_image
    del exit_image
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
            elif event.type == SDL_MOUSEBUTTONDOWN:
                if collision(start_image.x, start_image.y, start_image.w, start_image.h, event.x, -(event.y-600)):
                    game_framework.push_state(level_select_state)
                elif collision(exit_image.x, exit_image.y, exit_image.w, exit_image.h, event.x, -(event.y - 600)):
                    game_framework.quit()
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






