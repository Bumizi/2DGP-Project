from pico2d import *
import game_framework
import dead_state
from block import Block

# Boy State
#IDLE, SCISSOR, ROCK, PAPER = range(4)

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


# Player States

# IDLE state functions
class IDLE:
    @staticmethod
    def enter(player, event):
        player.frame = 0
        #Player.timer = 100

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.image = load_image('resource_player\player_idle.png')
        #player.frame = (player.frame + 1) % 4
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

    @staticmethod
    def draw(player):
        player.image.clip_composite_draw(int(player.frame) * int(202 / 4), 0, int(202 / 4), 93, 0, 'h',
                                         player.image_x, player.image_y, player.image_w, player.image_h)
        for i in range(player.heart_count):
            player.heart.clip_draw(0, 0, 620, 620, player.heart_x - i * player.heart_w, player.heart_y, player.heart_w-1,
                                 player.heart_h)

# ROCK state functions
class ROCK:
    @staticmethod
    def enter(player, event):
        global enter_timer
        player.frame = 0
        enter_timer = get_time()
        player.image = load_image('resource_player\player_attack1.png')
        #player.hand = load_image('my_rock.png')

    @staticmethod
    def exit(player, event):
        #if event == SPACE:
            #boy.fire_ball()
        pass

    @staticmethod
    def do(player):
        global enter_timer
        until_timer = get_time()
        #print("Time: %f" % player.timer)
        #if until_timer - enter_timer < 1:
            #player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        if player.frame < 1.5:
            player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        else:
            if player.image != 'resource_player\player_idle.png':
                player.image = load_image('resource_player\player_idle.png')
            player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        #player.timer -= 1
        #player.x += player.velocity

    @staticmethod
    def draw(player):
        if player.image == 'resource_player\player_attack1.png':
            player.image.clip_composite_draw(int(player.frame) * int(165 / 3), 0, int(165 / 3), 100, 0, 'h', player.image_x, player.image_y, player.image_w, player.image_h)
            #player.hand.clip_draw(0, 0, 120, 120, player.hand_x, player.hand_y, player.hand_w, player.hand_h)
        else:
            player.image.clip_composite_draw(int(player.frame) * int(202 / 4), 0, int(202 / 4), 93, 0, 'h',
                                             player.image_x, player.image_y, player.image_w, player.image_h)
            #player.hand.clip_draw(0, 0, 120, 120, player.hand_x, player.hand_y, player.hand_w, player.hand_h)
        for i in range(player.heart_count):
            player.heart.clip_draw(0, 0, 620, 620, player.heart_x - i * player.heart_w, player.heart_y, player.heart_w-1, player.heart_h)

# SCISSOR state functions
class SCISSOR:
    @staticmethod
    def enter(player, event):
        global enter_timer
        player.frame = 0
        enter_timer = get_time()
        #player.hand = load_image('my_scissor.png')
        player.image = load_image('resource_player\player_attack1.png')

    @staticmethod
    def exit(player, event):
        #if event == SPACE:
            #boy.fire_ball()
        pass

    @staticmethod
    def do(player):
        global enter_timer
        until_timer = get_time()
        # print("Time: %f" % player.timer)
        if player.frame < 1.5:
            player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        else:
            if player.image != 'resource_player\player_idle.png':
                player.image = load_image('resource_player\player_idle.png')
            player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        #boy.x += boy.velocity * 5

    @staticmethod
    def draw(player):
        if player.image == 'resource_player\player_attack1.png':
            player.image.clip_composite_draw(int(player.frame) * int(165 / 3), 0, int(165 / 3), 100, 0, 'h',
                                             player.image_x, player.image_y, player.image_w, player.image_h)
            #player.hand.clip_draw(0, 0, 120, 120, player.hand_x, player.hand_y, player.hand_w, player.hand_h)
        else:
            player.image.clip_composite_draw(int(player.frame) * int(202 / 4), 0, int(202 / 4), 93, 0, 'h',
                                             player.image_x, player.image_y, player.image_w, player.image_h)
            #player.hand.clip_draw(0, 0, 120, 120, player.hand_x, player.hand_y, player.hand_w, player.hand_h)
        for i in range(player.heart_count):
            player.heart.clip_draw(0, 0, 620, 620, player.heart_x - i * player.heart_w, player.heart_y, player.heart_w-1, player.heart_h)

# PAPER state functions
class PAPER:
    @staticmethod
    def enter(player, event):
        player.frame = 0
        #player.hand = load_image('my_paper.png')
        player.image = load_image('resource_player\player_attack1.png')

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        global enter_timer
        until_timer = get_time()
        # print("Time: %f" % player.timer)
        if player.frame < 1.5:
            player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        else:
            if player.image != 'resource_player\player_idle.png':
                player.image = load_image('resource_player\player_idle.png')
            player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        # boy.x += boy.velocity * 5

    @staticmethod
    def draw(player):
        if player.image == 'resource_player\player_attack1.png':
            player.image.clip_composite_draw(int(player.frame) * int(165 / 3), 0, int(165 / 3), 100, 0, 'h',
                                             player.image_x, player.image_y, player.image_w, player.image_h)
            #player.hand.clip_draw(0, 0, 120, 120, player.hand_x, player.hand_y, player.hand_w, player.hand_h)
        else:
            player.image.clip_composite_draw(int(player.frame) * int(202 / 4), 0, int(202 / 4), 93, 0, 'h',
                                             player.image_x, player.image_y, player.image_w, player.image_h)
            #player.hand.clip_draw(0, 0, 120, 120, player.hand_x, player.hand_y, player.hand_w, player.hand_h)
        for i in range(player.heart_count):
            player.heart.clip_draw(0, 0, 620, 620, player.heart_x - i * player.heart_w, player.heart_y, player.heart_w-1, player.heart_h)

# DAMAGED state functions
class DAMAGED:
    damaged_timer = 0
    @staticmethod
    def enter(player, event):
        global damaged_timer
        damaged_timer = 0
        player.frame = 0
        player.heart_count -= 1
        player.image = load_image('resource_player\player_damaged.png')

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        global damaged_timer
        until_timer = get_time()
        # print("Time: %f" % player.timer)
        if player.heart_count > 0:
            if player.frame < 1.5:
                player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
            else:
                player.add_event(IDLE)
        else:
            if player.frame < 1.5:
                player.image = load_image('resource_player\player_dead.png')
                player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
            else:
                game_framework.push_state(dead_state)
        # boy.x += boy.velocity * 5

    @staticmethod
    def draw(player):
        if player.heart_count > 0:
            player.image.clip_composite_draw(int(player.frame) * int(208 / 4), 0, int(208 / 4), 100, 0, 'h', player.image_x, player.image_y, player.image_w, player.image_h)
        else:
            player.image.clip_composite_draw(int(player.frame) * int(365 / 6), 0, int(365 / 6), 100, 0, 'h',
                                             player.image_x, player.image_y, player.image_w, player.image_h)
        for i in range(player.heart_count):
            player.heart.clip_draw(0, 0, 620, 620, player.heart_x - i * player.heart_w, player.heart_y,
                                       player.heart_w - 1, player.heart_h)


next_state_table = {
    IDLE: {SET_SCISSOR: SCISSOR, SET_ROCK: ROCK, SET_PAPER: PAPER, SET_DAMAGED: DAMAGED},
    SCISSOR: {SET_SCISSOR: IDLE, SET_ROCK: ROCK, SET_PAPER: PAPER, SET_DAMAGED: DAMAGED},
    ROCK: {SET_SCISSOR: SCISSOR, SET_ROCK: IDLE, SET_PAPER: PAPER, SET_DAMAGED: DAMAGED},
    PAPER: {SET_SCISSOR: SCISSOR, SET_ROCK: ROCK, SET_PAPER: IDLE, SET_DAMAGED: DAMAGED},
    DAMAGED: {IDLE: IDLE, SET_SCISSOR: DAMAGED, SET_ROCK: DAMAGED, SET_PAPER: DAMAGED, SET_DAMAGED: DAMAGED, }
}

class Player:
    image = None
    #hand = None
    heart = None
    def __init__(self):
        self.image_x, self.image_y, self.image_w, self.image_h = 730, 200, 100, 100
        #self.hand_x, self.hand_y, self.hand_w, self.hand_h = self.image_x-100, self.image_y, 80, 80
        self.heart_x, self.heart_y, self.heart_w, self.heart_h = 770, 140, 20, 20
        self.image = load_image('resource_player\player_idle.png')
        self.heart = load_image('resource_player\heart.png')
        self.event_que = []
        self.cur_state = IDLE
        self.heart_count = 5
        #self.enter_state[IDLE](self)
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.event_que.insert(0, event)

    #def change_state(self,  state):
        #self.exit_state[self.cur_state](self)
        #self.enter_state[state](self)
        #self.cur_state = state
        #pass

    #enter_state = {IDLE: enter_IDLE, ROCK: enter_ROCK, SCISSOR: enter_SCISSOR, PAPER: enter_PAPER}
    #exit_state = {IDLE: exit_IDLE, ROCK: exit_ROCK, SCISSOR: exit_SCISSOR, PAPER: exit_PAPER}
    #do_state = {IDLE: do_IDLE, ROCK: do_ROCK, SCISSOR: do_SCISSOR, PAPER: do_PAPER}
    #draw_state = {IDLE: draw_IDLE, ROCK: draw_ROCK, SCISSOR: draw_SCISSOR, PAPER: draw_PAPER}

    def update(self):
        #self.do_state[self.cur_state](self)
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            #self.change_state(next_state_table[self.cur_state][event])
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        pass

    def draw(self):
        #self.draw_state[self.cur_state](self)
        self.cur_state.draw(self)
        pass

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if key_event == SET_SCISSOR:
                pass
            elif key_event == SET_PAPER:
                pass
            elif key_event == SET_ROCK:
                pass
            self.add_event(key_event)

