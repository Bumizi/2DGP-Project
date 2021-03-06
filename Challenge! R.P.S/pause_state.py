import game_framework
import game_world
from pico2d import *
import main_state
import title_state

name = "PauseState"
image_pause = None
image_continue = None
image_quit = None
image_restart = None

class Pause:
    def __init__(self):
        self.image = load_image('resource_pause\pause.png')
        self.x, self.y, self.w, self.h = 400, 300, 150, 150

    def draw(self):
        self.image.clip_draw(0, 0, 225, 225, self.x, self.y, self.w, self.h)

    def update(self):
        pass


class Restart:
    def __init__(self):
        self.image = load_image('resource_pause\Restart.png')
        self.x, self.y, self.w, self.h = 400, 150, 100, 50

    def draw(self):
        self.image.clip_draw(0, 0, 230, 40, self.x, self.y, self.w, self.h)

    def update(self):
        pass


class Quit:
    def __init__(self):
        self.image = load_image('resource_pause\quit.png')
        self.x, self.y, self.w, self.h = 600, 150, 100, 50

    def draw(self):
        self.image.clip_draw(0, 0, 230, 40, self.x, self.y, self.w, self.h)

    def update(self):
        pass


class Continue:
    def __init__(self):
        self.image = load_image('resource_pause\continue.png')
        self.x, self.y, self.w, self.h = 210, 150, 100, 50

    def draw(self):
        self.image.clip_draw(0, 0, 687, 172, self.x, self.y, self.w, self.h)

    def update(self):
        pass


def collision(x1, y1, x2, y2, px, py):
    new_x1 = x1-x2/2
    new_y1 = y1+y2/2
    new_x2 = x1+x2/2
    new_y2 = y1-y2/2
    if (new_x1 < px < new_x2 and new_y1 > py > new_y2):
        return True


def enter():
    global image_pause, image_restart, image_quit, image_continue
    image_pause = Pause()
    image_restart = Restart()
    image_quit = Quit()
    image_continue = Continue()
    pass


def exit():
    global image_pause, image_restart, image_quit, image_continue
    del image_pause
    del image_restart
    del image_quit
    del image_continue
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.pop_state()
            elif event.type == SDL_MOUSEBUTTONDOWN:
                if collision(image_restart.x, image_restart.y, image_restart.w, image_restart.h, event.x, -(event.y - 500)):
                    game_framework.pop_state()
                    game_framework.change_state(main_state)
                elif collision(image_quit.x, image_quit.y, image_quit.w, image_quit.h, event.x, -(event.y - 500)):
                    game_framework.pop_state()
                    game_framework.change_state(title_state)
                elif collision(image_continue.x, image_continue.y, image_continue.w, image_continue.h, event.x, -(event.y - 500)):
                    game_framework.pop_state()
    pass


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    image_pause.draw()
    image_continue.draw()
    image_quit.draw()
    image_restart.draw()
    update_canvas()
    pass


def update():
    pass


def pause():
    pass


def resume():
    pass






