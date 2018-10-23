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

    def draw(self):
        self.image.draw(300, 300)


class Level_Normal:
    def __init__(self):
        self.image = load_image('level_normal.jpg')
        self.x, self.y = 100, 100

    def draw(self):
        self.image.clip_draw(0, 225, 950, 450, self.x, self.y)


class Level_Hard:
    def __init__(self):
        self.image = load_image('level_hard.jpg')
        self.x, self.y = 500, 100

    def draw(self):
        self.image.clip_draw(0, 450, 950, 225, self.x, self.y)


def collision(x1, y1, x2, y2, px, py):
    if(x1 < px < x2 & y1 < py < y2):
        return True


def enter():
    global image_easy, image_normal, image_hard
    image_easy = load_image('level_easy.png')
    image_normal = load_image('level_normal.png')
    image_hard = load_image('level_hard.png')
    pass


def exit():
    global image_easy, image_normal, image_hard
    del (image_easy)
    del (image_normal)
    del (image_hard)
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.pop_state()
            #elif event.type == SDL_MOUSEBUTTONDOWN and collision(Draw_Button_Start.x, Draw_Button_Start.y, 500, 400, event.x, event.y):
                #pass
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.pop_state()
                game_framework.change_state(main_state)
    pass


def draw():
    clear_canvas()
    title_state.main_image.draw()
    title_state.start_image.draw()
    title_state.exit_image.draw()
    image_easy.draw(200, 300)
    image_normal.draw(400, 300)
    image_hard.draw(600, 300)
    update_canvas()
    pass







def update():
    pass


def pause():
    pass


def resume():
    pass






