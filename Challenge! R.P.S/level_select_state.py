import game_framework
from pico2d import *
import main_state
import title_state


name = "LevelSelectState"
image_easy = None
image_normal = None
image_hard = None
game_level = None

class Level_Easy:
    def __init__(self):
        self.image = load_image('level_easy.png')
        self.x, self.y, self.w, self.h = 400, 400, 100, 50

    def draw(self):
        self.image.clip_draw(0, 0, 500, 150, self.x, self.y, self.w, self.h)


class Level_Normal:
    def __init__(self):
        self.image = load_image('level_normal.png')
        self.x, self.y, self.w, self.h = 400, 320, 100, 50

    def draw(self):
        self.image.clip_draw(0, 0, 500, 150, self.x, self.y, self.w, self.h)


class Level_Hard:
    def __init__(self):
        self.image = load_image('level_hard.png')
        self.x, self.y, self.w, self.h = 400, 240, 100, 50

    def draw(self):
        self.image.clip_draw(0, 0, 500, 150, self.x, self.y, self.w, self.h)


def collision(x1, y1, x2, y2, px, py):
    new_x1 = x1-x2/2
    new_y1 = y1+y2/2
    new_x2 = x1+x2/2
    new_y2 = y1-y2/2
    if (new_x1 < px < new_x2 and new_y1 > py > new_y2):
        return True


def enter():
    global image_easy, image_normal, image_hard
    image_easy = Level_Easy()
    image_normal = Level_Normal()
    image_hard = Level_Hard()
    pass


def exit():
    global image_easy, image_normal, image_hard
    del image_easy
    del image_normal
    del image_hard
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
                if collision(image_easy.x, image_easy.y, image_easy.w, image_easy.h, event.x, -(event.y - 500)):
                    game_framework.pop_state()
                    game_framework.change_state(main_state)
                elif collision(image_normal.x, image_normal.y, image_normal.w, image_normal.h, event.x, -(event.y - 500)):
                    game_framework.pop_state()
                    game_framework.change_state(main_state)
                elif collision(image_hard.x, image_hard.y, image_hard.w, image_hard.h, event.x, -(event.y - 500)):
                    game_framework.pop_state()
                    game_framework.change_state(main_state)
            #elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                #game_framework.pop_state()
                #game_framework.change_state(main_state)
    pass


def draw():
    clear_canvas()
    title_state.main_image.draw()
    title_state.start_image.draw()
    title_state.exit_image.draw()
    image_easy.draw()
    image_normal.draw()
    image_hard.draw()
    update_canvas()
    pass







def update():
    pass


def pause():
    pass


def resume():
    pass






