from pico2d import *
import game_world
from player import Player

# Event
IDLE, SET_SCISSOR, SET_ROCK, SET_PAPER = range(4)

key_event_table = {
    (SDL_KEYDOWN, SDLK_1): SET_SCISSOR,
    (SDL_KEYDOWN, SDLK_2): SET_ROCK,
    (SDL_KEYDOWN, SDLK_3): SET_PAPER,
}


# Select Block

# IDLE state functions
class IDLE:
    @staticmethod
    def enter(block, event):
        pass

    @staticmethod
    def exit(block, event):
        pass

    @staticmethod
    def do(block):
        pass

    @staticmethod
    def draw(block):
        pass


# ROCK state functions
class ROCK:
    @staticmethod
    def enter(block, event):
        Enemy_Block.rock = load_image('resource_enemy\enemy_rock.jpg')
        pass

    @staticmethod
    def exit(block, event):
        pass

    @staticmethod
    def do(block):
        pass

    @staticmethod
    def draw(block):
        block.rock.clip_draw(0, 0, 120, 121, block.x, block.y, block.w, block.h)

# SCISSOR state functions
class SCISSOR:
    @staticmethod
    def enter(block, event):
        Enemy_Block.scissor = load_image('resource_enemy\enemy_scissor.jpg')
        pass

    @staticmethod
    def exit(block, event):
        pass

    @staticmethod
    def do(block):
        pass

    @staticmethod
    def draw(block):
        block.scissor.clip_draw(0, 0, 120, 120, block.x, block.y, block.w, block.h)

# PAPER state functions
class PAPER:
    @staticmethod
    def enter(block, event):
        Enemy_Block.paper = load_image('resource_enemy\enemy_paper.jpg')
        pass

    @staticmethod
    def exit(block, event):
        pass

    @staticmethod
    def do(block):
        pass

    @staticmethod
    def draw(block):
        block.paper.clip_draw(0, 0, 120, 120, block.x, block.y, block.w, block.h)


next_state_table = {
    IDLE: {SET_SCISSOR: SCISSOR, SET_ROCK: ROCK, SET_PAPER: PAPER},
    SCISSOR: {SET_SCISSOR: IDLE, SET_ROCK: ROCK, SET_PAPER: PAPER},
    ROCK: {SET_SCISSOR: SCISSOR, SET_ROCK: IDLE, SET_PAPER: PAPER},
    PAPER: {SET_SCISSOR: SCISSOR, SET_ROCK: ROCK, SET_PAPER: IDLE}
}


class Enemy_Block:
    image = None
    rock = None
    scissor = None
    paper = None
    block = None

    def __init__(self):
        self.x, self.y, self.w, self.h = 150, 220, 80, 80
        self.rock, scissor, paper = load_image('resource_enemy\enemy_rock.jpg'), load_image('resource_enemy\enemy_scissor.jpg'), load_image('resource_enemy\enemy_paper.jpg')
        self.velocity = 2
        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def fire_ball(self):
        global block
        block = Enemy_Block()
        game_world.add_object(block, 1)

    def draw(self):
        self.cur_state.draw(self)

    def update(self):
        global block
        self.x += self.velocity
        if self.x < 25 or self.x > 800 - 25:
            game_world.remove_object(self)
            block = None
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)