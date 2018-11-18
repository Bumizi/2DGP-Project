import random
import json
import os

from pico2d import *
import game_world
import game_framework
import title_state
import pause_state
import dead_state
from player import Player
from enemy import Enemy
from select_block import Select_Block
from my_block import MY_Block
from enemy_block import Enemy_Block


name = "MainState"

character_player = None
character_enemy = None
player_block = None
enemy_blocks = None
select = None
background = None
font = None


class BackGround:
    def __init__(self):
        self.image = load_image('back.jpg')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 612, 357, 400, 250, 800, 500)


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
    global background, character_enemy, character_player, select, player_block, enemy_block
    character_player = Player()
    character_enemy = Enemy()
    select = Select_Block()
    player_block = MY_Block()
    enemy_block = Enemy_Block()
    background = BackGround()
    game_world.add_object(background, 0)
    game_world.add_object(player_block, 1)
    game_world.add_object(select, 1)
    game_world.add_object(character_player, 1)
    game_world.add_object(character_enemy, 1)
    #game_world.add_object(enemy_block, 1)
    pass


def exit():
    global background, character_enemy, character_player, select, player_block#, enemy_block
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
            game_framework.push_state(pause_state)
            #game_framework.change_state(title_state)
        #elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
            #game_framework.push_state(pause_state)
        else:
            character_player.handle_event(event)
            character_enemy.handle_event(event)
            select.handle_event(event)
            player_block.handle_event(event)
            if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
                block = Enemy_Block()
                game_world.add_object(block, 1)
            #enemy_block.handle_event(event)


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