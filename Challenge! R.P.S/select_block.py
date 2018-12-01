from pico2d import *
import game_world
from my_block import MY_Block


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
        Select_Block.rock, Select_Block.scissor, Select_Block.paper= load_image(
            'resource_select\select_rock.png'), load_image('resource_select\select_scissor.png'), load_image(
            'resource_select\select_paper.png')
        pass

    @staticmethod
    def exit(block, event):
        pass

    @staticmethod
    def do(block):
        pass

    @staticmethod
    def draw(block):
        block.scissor.clip_draw(0, 0, 130, 150, block.scissor_x, block.scissor_y, block.scissor_w, block.scissor_h)
        block.rock.clip_draw(0, 0, 130, 150, block.rock_x, block.rock_y, block.rock_w, block.rock_h)
        block.paper.clip_draw(0, 0, 160, 150, block.paper_x, block.paper_y, block.paper_w, block.paper_h)


# ROCK state functions
class ROCK:
    @staticmethod
    def enter(block, event):
        Select_Block.rock, Select_Block.scissor, Select_Block.paper, Select_Block.border = load_image(
            'resource_select\select_rock.png'), load_image('resource_select\select_scissor.png'), load_image(
            'resource_select\select_paper.png'), load_image('resource_select\Red_border.png')
        block.border_x, block.border_y = block.rock_x, block.rock_y
        pass

    @staticmethod
    def exit(block, event):
        pass

    @staticmethod
    def do(block):
        pass

    @staticmethod
    def draw(block):
        block.border.clip_draw(0, 0, 500, 347, block.border_x, block.border_y, block.border_w, block.border_h)
        block.scissor.clip_draw(0, 0, 130, 150, block.scissor_x, block.scissor_y, block.scissor_w, block.scissor_h)
        block.rock.clip_draw(0, 0, 130, 150, block.rock_x, block.rock_y, block.rock_w, block.rock_h)
        block.paper.clip_draw(0, 0, 160, 150, block.paper_x, block.paper_y, block.paper_w, block.paper_h)


# SCISSOR state functions
class SCISSOR:
    @staticmethod
    def enter(block, event):
        Select_Block.rock, Select_Block.scissor, Select_Block.paper, Select_Block.border = load_image(
            'resource_select\select_rock.png'), load_image('resource_select\select_scissor.png'), load_image(
            'resource_select\select_paper.png'), load_image('resource_select\Red_border.png')
        block.border_x, block.border_y = block.scissor_x, block.scissor_y
        pass

    @staticmethod
    def exit(block, event):
        pass

    @staticmethod
    def do(block):
        pass

    @staticmethod
    def draw(block):
        block.border.clip_draw(0, 0, 500, 347, block.border_x, block.border_y, block.border_w, block.border_h)
        block.scissor.clip_draw(0, 0, 130, 150, block.scissor_x, block.scissor_y, block.scissor_w, block.scissor_h)
        block.rock.clip_draw(0, 0, 130, 150, block.rock_x, block.rock_y, block.rock_w, block.rock_h)
        block.paper.clip_draw(0, 0, 160, 150, block.paper_x, block.paper_y, block.paper_w, block.paper_h)

# PAPER state functions
class PAPER:
    @staticmethod
    def enter(block, event):
        Select_Block.rock, Select_Block.scissor, Select_Block.paper, Select_Block.border = load_image('resource_select\select_rock.png'), load_image('resource_select\select_scissor.png'), load_image(
            'resource_select\select_paper.png'), load_image('resource_select\Red_border.png')
        block.border_x, block.border_y = block.paper_x, block.paper_y
        pass

    @staticmethod
    def exit(block, event):
        pass

    @staticmethod
    def do(block):
        pass

    @staticmethod
    def draw(block):
        block.border.clip_draw(0, 0, 500, 347, block.border_x, block.border_y, block.border_w, block.border_h)
        block.scissor.clip_draw(0, 0, 130, 150, block.scissor_x, block.scissor_y, block.scissor_w, block.scissor_h)
        block.rock.clip_draw(0, 0, 130, 150, block.rock_x, block.rock_y, block.rock_w, block.rock_h)
        block.paper.clip_draw(0, 0, 160, 150, block.paper_x, block.paper_y, block.paper_w, block.paper_h)


next_state_table = {
    IDLE: {SET_SCISSOR: SCISSOR, SET_ROCK: ROCK, SET_PAPER: PAPER},
    SCISSOR: {SET_SCISSOR: IDLE, SET_ROCK: ROCK, SET_PAPER: PAPER},
    ROCK: {SET_SCISSOR: SCISSOR, SET_ROCK: IDLE, SET_PAPER: PAPER},
    PAPER: {SET_SCISSOR: SCISSOR, SET_ROCK: ROCK, SET_PAPER: IDLE}
}

class Select_Block:
    rock = None
    scissor = None
    paper = None
    border = None
    def __init__(self):
        self.scissor_x, self.scissor_y, self.scissor_w, self.scissor_h = 200, 80, 80, 80
        self.rock_x, self.rock_y, self.rock_w, self.rock_h = 400, 80, 80, 80
        self.paper_x, self.paper_y, self.paper_w, self.paper_h = 600, 80, 80, 80
        self.border_x, self.border_y, self.border_w, self.border_h = 0, 0, 90, 90
        self.rock, scissor, paper, border = load_image('resource_select\select_rock.png'), load_image('resource_select\select_scissor.png'), load_image('resource_select\select_paper.png'), load_image('resource_select\Red_border.png')
        self.event_que = []
        self.cur_state = IDLE
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

