import game_framework
from pico2d import *
import main_state


name = "PauseState"
image = None



def enter():
    global image
    image = load_image('pause.png')
    pass


def exit():
    global image
    del image
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.pop_state()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()
                pass

    pass


def draw():
    clear_canvas()
    image.draw(400, 300)
    main_state.grass.draw()
    main_state.character_player.draw()
    main_state.character_enemy.draw()
    update_canvas()
    pass


def update():
    pass


def pause():
    pass


def resume():
    pass






