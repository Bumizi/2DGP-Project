import game_framework
from pico2d import *
import title_state

name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('dustin_photo2.jpg')
    pass


def exit():
    global image
    del(image)
    pass


def update():
    global logo_time

    if(logo_time > 1.0):
        logo_time = 0
        #game_framework.quit()
        game_framework.change_state(title_state)
    delay(0.01)
    logo_time += 0.01
    pass


def draw():
    global image
    clear_canvas()
    image.clip_draw(0, 0, 83, 100, 800//2, 500//2, 83*2, 100*2)
    update_canvas()
    pass




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




