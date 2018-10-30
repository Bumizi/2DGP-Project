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
        #player.scissor.clip_draw(0, 0, 130, 150, player.scissor_x, player.scissor_y, player.scissor_w, player.scissor_h)
        #player.rock.clip_draw(0, 0, 130, 150, player.rock_x, player.rock_y, player.rock_w, player.rock_h)
        #player.paper.clip_draw(0, 0, 160, 150, player.paper_x, player.paper_y, player.paper_w, player.paper_h)


# ROCK state functions
class ROCK:
    @staticmethod
    def enter(block, event):
        MY_Block.rock = load_image('my_rock.png')
        pass

    @staticmethod
    def exit(block, event):
        pass

    @staticmethod
    def do(block):
        pass

    @staticmethod
    def draw(block):
        block.rock.clip_draw(0, 0, 130, 150, block.x, block.y, block.w, block.h)

# SCISSOR state functions
class SCISSOR:
    @staticmethod
    def enter(block, event):
        MY_Block.scissor = load_image('my_scissor.png')
        pass

    @staticmethod
    def exit(block, event):
        pass

    @staticmethod
    def do(block):
        pass

    @staticmethod
    def draw(block):
        block.scissor.clip_draw(0, 0, 130, 150, block.x, block.y, block.w, block.h)

# PAPER state functions
class PAPER:
    @staticmethod
    def enter(block, event):
        MY_Block.paper = load_image('my_paper.png')
        pass

    @staticmethod
    def exit(block, event):
        pass

    @staticmethod
    def do(block):
        pass

    @staticmethod
    def draw(block):
        block.paper.clip_draw(0, 0, 160, 150, block.x, block.y, block.w, block.h)


next_state_table = {
    IDLE: {SET_SCISSOR: SCISSOR, SET_ROCK: ROCK, SET_PAPER: PAPER},
    SCISSOR: {SET_SCISSOR: IDLE, SET_ROCK: ROCK, SET_PAPER: PAPER},
    ROCK: {SET_SCISSOR: SCISSOR, SET_ROCK: IDLE, SET_PAPER: PAPER},
    PAPER: {SET_SCISSOR: SCISSOR, SET_ROCK: ROCK, SET_PAPER: IDLE}
}


class MY_Block:
    image = None
    rock = None
    scissor = None
    paper = None

    def __init__(self):
        self.x, self.y, self.w, self.h = 640, 220, 80, 80
        self.rock, scissor, paper = load_image('my_rock.png'), load_image('my_scissor.png'), load_image('my_paper.png')
        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

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
