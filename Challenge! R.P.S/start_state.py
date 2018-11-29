import game_framework
from pico2d import *
import title_state

name = "StartState"
image1 = None
image2 = None
logo_time = 0.0


def enter():
    global image1, image2
    image1 = load_image('resource_start\dustin_photo2.jpg')
    image2 = load_image('resource_start\kpu_credit.png')
    pass


def exit():
    global image1, image2
    del image1
    del image2
    pass


def update():
    global logo_time

    if(logo_time > 1.0):
        logo_time = 0
        game_framework.change_state(title_state)
    delay(0.01)
    logo_time += 0.01
    pass


def draw():
    global image1, image2
    clear_canvas()
    image2.clip_draw(0, 0, 800, 600, 800 // 2, 500 // 2, 800, 600)
    image1.clip_draw(0, 0, 83, 100, 800//2 + 170, 500//2 + 20, 83, 100)
    update_canvas()
    pass




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




