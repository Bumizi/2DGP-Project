from pico2d import *
import game_framework
import dead_state
from block import Block

PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 20.0 #km/hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS*PIXEL_PER_METER)

#Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
FRAMES_PER_ACTION = 3


# Boy Event
IDLE, SET_SCISSOR, SET_ROCK, SET_PAPER, SET_DAMAGED = range(5)

key_event_table = {
    (SDL_KEYDOWN, SDLK_1): SET_SCISSOR,
    (SDL_KEYDOWN, SDLK_2): SET_ROCK,
    (SDL_KEYDOWN, SDLK_3): SET_PAPER,
    (SDL_KEYDOWN, SDLK_4): SET_DAMAGED,
}


# Enemy States

# IDLE state functions
class IDLE:
    @staticmethod
    def enter(enemy, event):
        enemy.frame = 0

    @staticmethod
    def exit(enemy, event):
        pass

    @staticmethod
    def do(enemy):
        enemy.image = load_image('resource_enemy\enemy_idle.png')
        enemy.frame = (enemy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

    @staticmethod
    def draw(enemy):
        enemy.image.clip_draw(int(enemy.frame) * int(210 / 3), 0, int(210 / 3), 100,
                                        enemy.image_x, enemy.image_y, enemy.image_w, enemy.image_h)
        for i in range(enemy.heart_count):
            enemy.heart.clip_draw(0, 0, 620, 620, enemy.heart_x - i * enemy.heart_w, enemy.heart_y, enemy.heart_w-1,
                                   enemy.heart_h)


# ROCK state functions
class ROCK:
    @staticmethod
    def enter(enemy, event):
        global enter_timer
        enemy.frame = 0
        enemy.image = load_image('resource_enemy\enemy_attack1.png')

    @staticmethod
    def exit(enemy, event):
        pass

    @staticmethod
    def do(enemy):
        if enemy.frame < 3:
            enemy.frame = (enemy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        else:
            if enemy.image != 'resource_enemy\enemy_idle.png':
                enemy.image = load_image('resource_enemy\enemy_idle.png')
            enemy.frame = (enemy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

    @staticmethod
    def draw(enemy):
        if enemy.image == 'resource_enemy\enemy_attack1.png':
            enemy.image.clip_draw(int(enemy.frame) * int(300 / 4), 0, int(300 / 4), 90, enemy.image_x, enemy.image_y, enemy.image_w, enemy.image_h)
        else:
            enemy.image.clip_draw(int(enemy.frame) * int(210 / 3), 0, int(210 / 3), 100,
                                            enemy.image_x, enemy.image_y, enemy.image_w, enemy.image_h)
        for i in range(enemy.heart_count):
            enemy.heart.clip_draw(0, 0, 620, 620, enemy.heart_x - i * enemy.heart_w, enemy.heart_y, enemy.heart_w-1, enemy.heart_h)


# SCISSOR state functions
class SCISSOR:
    @staticmethod
    def enter(enemy, event):
        global enter_timer
        enemy.frame = 0
        enemy.image = load_image('resource_enemy\enemy_attack1.png')

    @staticmethod
    def exit(enemy, event):
        pass

    @staticmethod
    def do(enemy):
        if enemy.frame < 3:
            enemy.frame = (enemy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        else:
            if enemy.image != 'resource_enemy\enemy_idle.png':
                enemy.image = load_image('resource_enemy\enemy_idle.png')
            enemy.frame = (enemy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

    @staticmethod
    def draw(enemy):
        if enemy.image == 'resource_enemy\enemy_attack1.png':
            enemy.image.clip_draw(int(enemy.frame) * int(300 / 4), 0, int(300 / 4), 90, enemy.image_x, enemy.image_y, enemy.image_w, enemy.image_h)
        else:
            enemy.image.clip_draw(int(enemy.frame) * int(210 / 3), 0, int(210 / 3), 100,
                                            enemy.image_x, enemy.image_y, enemy.image_w, enemy.image_h)
        for i in range(enemy.heart_count):
            enemy.heart.clip_draw(0, 0, 620, 620, enemy.heart_x - i * enemy.heart_w, enemy.heart_y, enemy.heart_w-1, enemy.heart_h)


# PAPER state functions
class PAPER:
    @staticmethod
    def enter(player, event):
        player.frame = 0
        player.image = load_image('resource_enemy\enemy_attack1.png')

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(enemy):
        if enemy.frame < 3:
            enemy.frame = (enemy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        else:
            if enemy.image != 'resource_enemy\enemy_idle.png':
                enemy.image = load_image('resource_enemy\enemy_idle.png')
            enemy.frame = (enemy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

    @staticmethod
    def draw(enemy):
        if enemy.image == 'resource_enemy\enemy_attack1.png':
            enemy.image.clip_draw(int(enemy.frame) * int(300 / 4), 0, int(300 / 4), 90, enemy.image_x, enemy.image_y, enemy.image_w, enemy.image_h)
        else:
            enemy.image.clip_draw(int(enemy.frame) * int(210 / 3), 0, int(210 / 3), 100,
                                            enemy.image_x, enemy.image_y, enemy.image_w, enemy.image_h)
        for i in range(enemy.heart_count):
            enemy.heart.clip_draw(0, 0, 620, 620, enemy.heart_x - i * enemy.heart_w, enemy.heart_y, enemy.heart_w-1, enemy.heart_h)


# DAMAGED state functions
class DAMAGED:
    damaged_timer = 0
    @staticmethod
    def enter(enemy, event):
        enemy.frame = 0
        enemy.heart_count -= 1
        enemy.image = load_image('resource_enemy\enemy_damaged.png')

    @staticmethod
    def exit(enemy, event):
        pass

    @staticmethod
    def do(enemy):
        if enemy.heart_count > 0:
            if enemy.frame < 1.5:
                enemy.frame = (enemy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
            else:
                enemy.add_event(IDLE)
        else:
            if enemy.frame < 1.5:
                enemy.image = load_image('resource_enemy\enemy_dead.png')
                enemy.frame = (enemy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
            else:
                game_framework.push_state(dead_state)

    @staticmethod
    def draw(enemy):
        if enemy.heart_count > 0:
            enemy.image.clip_draw(int(enemy.frame) * int(144 / 2), 0, int(144 / 2), 95, enemy.image_x, enemy.image_y, enemy.image_w, enemy.image_h)
        else:
            enemy.image.clip_draw(int(enemy.frame) * int(322 / 4.2), 0, int(322 / 4.2), 90,
                                            enemy.image_x, enemy.image_y, enemy.image_w, enemy.image_h)
        for i in range(enemy.heart_count):
            enemy.heart.clip_draw(0, 0, 620, 620, enemy.heart_x - i * enemy.heart_w, enemy.heart_y,
                                  enemy.heart_w - 1, enemy.heart_h)


next_state_table = {
    IDLE: {SET_SCISSOR: SCISSOR, SET_ROCK: ROCK, SET_PAPER: PAPER, SET_DAMAGED: DAMAGED},
    SCISSOR: {SET_SCISSOR: IDLE, SET_ROCK: ROCK, SET_PAPER: PAPER, SET_DAMAGED: DAMAGED},
    ROCK: {SET_SCISSOR: SCISSOR, SET_ROCK: IDLE, SET_PAPER: PAPER, SET_DAMAGED: DAMAGED},
    PAPER: {SET_SCISSOR: SCISSOR, SET_ROCK: ROCK, SET_PAPER: IDLE, SET_DAMAGED: DAMAGED},
    DAMAGED: {IDLE: IDLE, SET_SCISSOR: DAMAGED, SET_ROCK: DAMAGED, SET_PAPER: DAMAGED, SET_DAMAGED: DAMAGED, }
}

class Enemy:
    image = None
    heart = None
    def __init__(self):
        self.image_x, self.image_y, self.image_w, self.image_h = 60, 200, 100, 100
        self.heart_x, self.heart_y, self.heart_w, self.heart_h = 100, 140, 20, 20
        self.image = load_image('resource_enemy\enemy_idle.png')
        self.heart = load_image('resource_enemy\heart.png')
        self.event_que = []
        self.cur_state = IDLE
        self.heart_count = 5
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.event_que.insert(0, event)


    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        pass

    def draw(self):
        self.cur_state.draw(self)
        pass

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

