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
        MY_Block.type = 0
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
        MY_Block.image = load_image('resource_player\my_rock.png')
        MY_Block.type = 1
        pass

    @staticmethod
    def exit(block, event):
        pass

    @staticmethod
    def do(block):
        pass

    @staticmethod
    def draw(block):
        block.image.clip_draw(0, 0, 130, 150, block.x, block.y, block.w, block.h)

# SCISSOR state functions
class SCISSOR:
    @staticmethod
    def enter(block, event):
        MY_Block.image = load_image('resource_player\my_scissor.png')
        MY_Block.type = 2
        pass

    @staticmethod
    def exit(block, event):
        pass

    @staticmethod
    def do(block):
        pass

    @staticmethod
    def draw(block):
        block.image.clip_draw(0, 0, 130, 150, block.x, block.y, block.w, block.h)

# PAPER state functions
class PAPER:
    @staticmethod
    def enter(block, event):
        MY_Block.image = load_image('resource_player\my_paper.png')
        MY_Block.type = 3
        pass

    @staticmethod
    def exit(block, event):
        pass

    @staticmethod
    def do(block):
        pass

    @staticmethod
    def draw(block):
        block.image.clip_draw(0, 0, 160, 150, block.x, block.y, block.w, block.h)


next_state_table = {
    IDLE: {SET_SCISSOR: SCISSOR, SET_ROCK: ROCK, SET_PAPER: PAPER},
    SCISSOR: {SET_SCISSOR: IDLE, SET_ROCK: ROCK, SET_PAPER: PAPER},
    ROCK: {SET_SCISSOR: SCISSOR, SET_ROCK: IDLE, SET_PAPER: PAPER},
    PAPER: {SET_SCISSOR: SCISSOR, SET_ROCK: ROCK, SET_PAPER: IDLE}
}


class MY_Block:
    image = None
    type = None

    def __init__(self):
        self.x, self.y, self.w, self.h = 640, 220, 80, 80
        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def get_bb(self):
        return 640 + 40 - 30, 220 + 40 - 30, 640 + 40 + 30, 220 + 40 + 30

    def draw(self):
        self.cur_state.draw(self)

    def update(self):
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
