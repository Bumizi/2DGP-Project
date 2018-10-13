import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state
import start_state


name = "MainState"


player = None
enemy = None
grass = None
font = None


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Player:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


class Enemy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


class Ball21x21:
    def __init__(self):
        self.x, self.y = random.randint(40, 700), 600
        self.image = load_image('ball21x21.png')
        self.speed = random.randint(5, 20)

    def update(self):
        if self.y > 60:
            self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)


class Ball41x41:
    def __init__(self):
        self.x, self.y = random.randint(40, 700), 600
        self.image = load_image('ball41x41.png')
        self.speed = random.randint(5, 20)

    def update(self):
        if self.y > 70:
            self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)


def enter():
    global player, grass, enemy
    player = Player()
    enemy = Enemy()
    grass = Grass()
    pass


def exit():
    global player, grass, enemy
    del (player)
    del (grass)
    del (enemy)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
            game_framework.push_state(pause_state)



def update():
    player.update()
    enemy.update()
    pass


def draw():
    clear_canvas()
    grass.draw()
    player.draw()
    enemy.draw()
    update_canvas()
    delay(0.05)
    pass