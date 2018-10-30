import random
import json
import os

from pico2d import *
import game_world
import game_framework
import title_state
import pause_state
from player import Player
from select_block import Select_Block
from my_block import MY_Block


name = "MainState"

character_player = None
character_enemy = None
player_block = None
select = None
grass = None
font = None


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)


#class Player:
#    def __init__(self):
#        self.x, self.y = random.randint(100, 700), 90
#        self.frame = random.randint(0, 7)
#        self.image = load_image('run_animation.png')

#    def update(self):
#        self.frame = (self.frame + 1) % 8
#        self.x += 5

#    def draw(self):
#        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


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
    global grass, character_enemy, character_player, select, player_block
    character_player = Player()
    character_enemy = Enemy()
    select = Select_Block()
    player_block = MY_Block()
    grass = Grass()
    game_world.add_object(grass, 0)
    game_world.add_object(select, 1)
    game_world.add_object(player_block, 1)
    game_world.add_object(character_player, 1)
    game_world.add_object(character_enemy, 1)
    pass


def exit():
    global grass, character_enemy, character_player, select, player_block
    del character_player
    del grass
    del character_enemy
    del select
    del player_block
    game_world.clear()
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
        else:
            character_player.handle_event(event)
            select.handle_event(event)
            player_block.handle_event(event)



def update():
    for game_object in game_world.all_objects():
        game_object.update()
    pass


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
    pass