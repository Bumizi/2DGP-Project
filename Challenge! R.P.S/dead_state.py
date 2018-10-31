import game_framework
import game_world
from pico2d import *
import main_state
import title_state
from player import Player


name = "DeadState"
image_gameover = None
image_restart = None
image_quit = None

class GameOver:
    def __init__(self):
        self.image = load_image('game_over.jpg')
        self.x, self.y, self.w, self.h = 400, 300, 200, 200

    def draw(self):
        self.image.clip_draw(0, 0, 300, 300, self.x, self.y, self.w, self.h)

    def update(self):
        pass


class Restart:
    def __init__(self):
        self.image = load_image('restart.png')
        self.x, self.y, self.w, self.h = 320, 150, 100, 50

    def draw(self):
        self.image.clip_draw(0, 0, 230, 40, self.x, self.y, self.w, self.h)

    def update(self):
        pass


class Quit:
    def __init__(self):
        self.image = load_image('quit.png')
        self.x, self.y, self.w, self.h = 480, 150, 100, 50

    def draw(self):
        self.image.clip_draw(0, 0, 230, 40, self.x, self.y, self.w, self.h)

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
    global image_gameover, image_restart, image_quit
    image_gameover = GameOver()
    image_restart = Restart()
    image_quit = Quit()
    game_world.add_object(image_gameover, 0)
    game_world.add_object(image_restart, 1)
    game_world.add_object(image_quit, 1)
    pass


def exit():
    global image_gameover, image_restart, image_quit
    del image_gameover
    del image_restart
    del image_quit
    game_world.clear()
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
            #elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                #game_framework.pop_state()
                #game_framework.change_state(main_state)
    pass


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
    pass


def update():
    pass


def pause():
    pass


def resume():
    pass






