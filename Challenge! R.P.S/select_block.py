from pico2d import *
import game_world
from block import Block


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
    def enter(player, event):
        Select_Block.rock, Select_Block.scissor, Select_Block.paper= load_image(
            'select_rock.png'), load_image('select_scissor.png'), load_image(
            'select_paper.png')
        pass

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        #player.image = load_image('player_idle.png')
        pass

    @staticmethod
    def draw(player):
        player.scissor.clip_draw(0, 0, 130, 150, player.scissor_x, player.scissor_y, player.scissor_w, player.scissor_h)
        player.rock.clip_draw(0, 0, 130, 150, player.rock_x, player.rock_y, player.rock_w, player.rock_h)
        player.paper.clip_draw(0, 0, 160, 150, player.paper_x, player.paper_y, player.paper_w, player.paper_h)


# ROCK state functions
class ROCK:
    @staticmethod
    def enter(player, event):
        Select_Block.rock, Select_Block.scissor, Select_Block.paper, Select_Block.border = load_image(
            'select_rock.png'), load_image('select_scissor.png'), load_image(
            'select_paper.png'), load_image('red_border.png')
        player.border_x, player.border_y = player.rock_x, player.rock_y
        pass

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        pass

    @staticmethod
    def draw(player):
        player.border.clip_draw(0, 0, 500, 347, player.border_x, player.border_y, player.border_w, player.border_h)
        player.scissor.clip_draw(0, 0, 130, 150, player.scissor_x, player.scissor_y, player.scissor_w, player.scissor_h)
        player.rock.clip_draw(0, 0, 130, 150, player.rock_x, player.rock_y, player.rock_w, player.rock_h)
        player.paper.clip_draw(0, 0, 160, 150, player.paper_x, player.paper_y, player.paper_w, player.paper_h)


# SCISSOR state functions
class SCISSOR:
    @staticmethod
    def enter(player, event):
        Select_Block.rock, Select_Block.scissor, Select_Block.paper, Select_Block.border = load_image(
            'select_rock.png'), load_image('select_scissor.png'), load_image(
            'select_paper.png'), load_image('red_border.png')
        player.border_x, player.border_y = player.scissor_x, player.scissor_y
        pass

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        pass

    @staticmethod
    def draw(player):
        player.border.clip_draw(0, 0, 500, 347, player.border_x, player.border_y, player.border_w, player.border_h)
        player.scissor.clip_draw(0, 0, 130, 150, player.scissor_x, player.scissor_y, player.scissor_w, player.scissor_h)
        player.rock.clip_draw(0, 0, 130, 150, player.rock_x, player.rock_y, player.rock_w, player.rock_h)
        player.paper.clip_draw(0, 0, 160, 150, player.paper_x, player.paper_y, player.paper_w, player.paper_h)

# PAPER state functions
class PAPER:
    @staticmethod
    def enter(player, event):
        Select_Block.rock, Select_Block.scissor, Select_Block.paper, Select_Block.border = load_image('select_rock.png'), load_image('select_scissor.png'), load_image(
            'select_paper.png'), load_image('red_border.png')
        player.border_x, player.border_y = player.paper_x, player.paper_y
        pass

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        pass

    @staticmethod
    def draw(player):
        player.border.clip_draw(0, 0, 500, 347, player.border_x, player.border_y, player.border_w, player.border_h)
        player.scissor.clip_draw(0, 0, 130, 150, player.scissor_x, player.scissor_y, player.scissor_w, player.scissor_h)
        player.rock.clip_draw(0, 0, 130, 150, player.rock_x, player.rock_y, player.rock_w, player.rock_h)
        player.paper.clip_draw(0, 0, 160, 150, player.paper_x, player.paper_y, player.paper_w, player.paper_h)


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
        self.rock, scissor, paper, border = load_image('select_rock.png'), load_image('select_scissor.png'), load_image('select_paper.png'), load_image('red_border.png')
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

