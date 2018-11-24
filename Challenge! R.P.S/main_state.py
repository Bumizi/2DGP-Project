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
#from enemy import Enemy
from enemy import *
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

attack_time = 0

import time
frame_time = 0.0
current_time = 0.0

class BackGround:
    def __init__(self):
        self.image = load_image('back.jpg')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 612, 357, 400, 250, 800, 500)


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
    global attack_time
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.push_state(pause_state)
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
    global attack_time
    attack_time += 1
    for game_object in game_world.all_objects():
        game_object.update()
    if attack_time > 500:
        attack_time = 0
        character_enemy.add_event(SET_ATTACK)
        #if len(character_enemy.event_que) > 1:
            #character_enemy.event_que.pop()
            #character_enemy.add_event(SET_ATTACK)
        block = Enemy_Block()
        game_world.add_object(block, 1)
    pass


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
    pass