from pico2d import *
import game_world
import game_framework
import random

class Enemy_Block:
    def __init__(self):
        self.image = None
        self.type = None
        self.x, self.y, self.w, self.h = 150, 220, 80, 80
        #self.exist = False
        #if self.exist is True:
        self.type = random.randint(1, 3)
        if self.type == 1:
            self.image = load_image('resource_enemy\enemy_rock.jpg')
        elif self.type == 2:
            self.image = load_image('resource_enemy\enemy_scissor.jpg')
        elif self.type == 3:
            self.image = load_image('resource_enemy\enemy_paper.jpg')
        self.velocity = 100

    def draw(self):
        self.image.clip_draw(0, 0, 120, 121, self.x, self.y, self.w, self.h)

    def update(self):
        self.x += self.velocity * game_framework.frame_time
        if self.x < 25 or self.x > 800 - 25:
            game_world.remove_object(self)