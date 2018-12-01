from pico2d import *
import game_world
import game_framework
from my_block import MY_Block
import player
import enemy
from player import Player
from enemy import Enemy
import level_select_state
import random

class Enemy_Block:
    def __init__(self):
        self.image = None
        self.type = None
        self.x, self.y, self.w, self.h = 150, 220, 80, 80
        self.type = random.randint(1, 3)
        if self.type == 1:
            self.image = load_image('resource_enemy\enemy_rock.png')
        elif self.type == 2:
            self.image = load_image('resource_enemy\enemy_scissor.png')
        elif self.type == 3:
            self.image = load_image('resource_enemy\enemy_paper.png')
        self.velocity = 100

    def draw(self):
        self.image.clip_draw(0, 0, 120, 121, self.x, self.y, self.w, self.h)

    def get_bb(self):
        return self.x + 40 - 30, self.y + 40 - 30, self.x + 40 + 30, self.y + 40 + 30

    def collide(self, MY_Block):
        left_self, bottom_self, right_self, top_self = self.get_bb()
        left_MY_Block, bottom_MY_Block, right_MY_Block, top_MY_Block = MY_Block.get_bb(MY_Block)
        if left_self > right_MY_Block: return False
        if right_self < left_MY_Block: return False
        if top_self < bottom_MY_Block: return False
        if bottom_self > top_MY_Block: return False
        return True

    def update(self):
        self.x += self.velocity * game_framework.frame_time * 3 / 2
        if MY_Block.type != 0:
            if self.collide(MY_Block):
                if level_select_state.game_level == 'easy':
                    if self.type == 1: #바위
                        if MY_Block.type == 1: #바위
                            pass
                        elif MY_Block.type == 2: #가위
                            Player.add_event(Player, player.SET_DAMAGED)
                        elif MY_Block.type == 3: #보
                            Enemy.add_event(Enemy, enemy.SET_DAMAGED)
                    elif self.type == 2: #가위
                        if MY_Block.type == 1: #바위
                            Enemy.add_event(Enemy, enemy.SET_DAMAGED)
                        elif MY_Block.type == 2: #가위
                            pass
                        elif MY_Block.type == 3: #보
                            Player.add_event(Player, player.SET_DAMAGED)
                    elif self.type == 3: #보
                        if MY_Block.type == 1: #바위
                            Player.add_event(Player, player.SET_DAMAGED)
                        elif MY_Block.type == 2: #가위
                            Enemy.add_event(Enemy, enemy.SET_DAMAGED)
                        elif MY_Block.type == 3: #보
                            pass
                elif level_select_state.game_level == 'normal':
                    if self.type == 1: #바위
                        if MY_Block.type == 1: #바위
                            Player.add_event(Player, player.SET_DAMAGED)
                        elif MY_Block.type == 2: #가위
                            Player.add_event(Player, player.SET_DAMAGED)
                        elif MY_Block.type == 3: #보
                            Enemy.add_event(Enemy, enemy.SET_DAMAGED)
                    elif self.type == 2: #가위
                        if MY_Block.type == 1: #바위
                            Enemy.add_event(Enemy, enemy.SET_DAMAGED)
                        elif MY_Block.type == 2: #가위
                            Player.add_event(Player, player.SET_DAMAGED)
                        elif MY_Block.type == 3: #보
                            Player.add_event(Player, player.SET_DAMAGED)
                    elif self.type == 3: #보
                        if MY_Block.type == 1: #바위
                            Player.add_event(Player, player.SET_DAMAGED)
                        elif MY_Block.type == 2: #가위
                            Enemy.add_event(Enemy, enemy.SET_DAMAGED)
                        elif MY_Block.type == 3: #보
                            Player.add_event(Player, player.SET_DAMAGED)
                elif level_select_state.game_level == 'hard':
                    if self.type == 1: #바위
                        if MY_Block.type == 1: #바위
                            Player.add_event(Player, player.SET_DAMAGED)
                        elif MY_Block.type == 2: #가위
                            Enemy.add_event(Enemy, enemy.SET_DAMAGED)
                        elif MY_Block.type == 3: #보
                            Player.add_event(Player, player.SET_DAMAGED)
                    elif self.type == 2: #가위
                        if MY_Block.type == 1: #바위
                            Player.add_event(Player, player.SET_DAMAGED)
                        elif MY_Block.type == 2: #가위
                            Player.add_event(Player, player.SET_DAMAGED)
                        elif MY_Block.type == 3: #보
                            Enemy.add_event(Enemy, enemy.SET_DAMAGED)
                    elif self.type == 3: #보
                        if MY_Block.type == 1: #바위
                            Enemy.add_event(Enemy, enemy.SET_DAMAGED)
                        elif MY_Block.type == 2: #가위
                            Player.add_event(Player, player.SET_DAMAGED)
                        elif MY_Block.type == 3: #보
                            Player.add_event(Player, player.SET_DAMAGED)
                game_world.remove_object(self)
        else:
            if self.collide(Player):
                Player.add_event(Player, player.SET_DAMAGED)
                game_world.remove_object(self)
