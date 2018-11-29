from pico2d import *
import game_framework
import dead_state
import victory_state
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
IDLE, SET_SCISSOR, SET_ROCK, SET_PAPER, SET_DAMAGED, SET_VICTORY = range(6)

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
            player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        else:
            if player.image != 'resource_player\player_idle.png':
                player.image = load_image('resource_player\player_idle.png')
            player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
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
            player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        else:
            if player.image != 'resource_player\player_idle.png':
                player.image = load_image('resource_player\player_idle.png')
            player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
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
            player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        else:
            if player.image != 'resource_player\player_idle.png':
                player.image = load_image('resource_player\player_idle.png')
            player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
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
        player.bgm.play()

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
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

    @staticmethod
    def draw(player):
        #if player.heart_count > 0:
        player.image.clip_composite_draw(int(player.frame) * int(208 / 4), 0, int(208 / 4), 100, 0, 'h', player.image_x, player.image_y, player.image_w, player.image_h)
        #else:
            #player.image.clip_composite_draw(int(player.frame) * int(365 / 6), 0, int(365 / 6), 100, 0, 'h',
                                             #player.image_x, player.image_y, player.image_w, player.image_h)
        for i in range(player.heart_count):
            player.heart.clip_draw(0, 0, 620, 620, player.heart_x - i * player.heart_w, player.heart_y,
                                       player.heart_w - 1, player.heart_h)


# VICTORY state functions
class VICTORY:
    @staticmethod
    def enter(player, event):
        player.frame = 0
        player.image = load_image('resource_player\player_victory.png')

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        if player.frame < 1.5:
            player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        else:
            game_framework.push_state(victory_state)

    @staticmethod
    def draw(player):
        player.image.clip_composite_draw(int(player.frame) * int(156 / 3), 0, int(156 / 3), 125, 0, 'h', player.image_x, player.image_y, player.image_w, player.image_h)


next_state_table = {
    IDLE: {SET_SCISSOR: SCISSOR, SET_ROCK: ROCK, SET_PAPER: PAPER, SET_DAMAGED: DAMAGED, SET_VICTORY: VICTORY},
    SCISSOR: {SET_SCISSOR: IDLE, SET_ROCK: ROCK, SET_PAPER: PAPER, SET_DAMAGED: DAMAGED, SET_VICTORY: VICTORY},
    ROCK: {SET_SCISSOR: SCISSOR, SET_ROCK: IDLE, SET_PAPER: PAPER, SET_DAMAGED: DAMAGED, SET_VICTORY: VICTORY},
    PAPER: {SET_SCISSOR: SCISSOR, SET_ROCK: ROCK, SET_PAPER: IDLE, SET_DAMAGED: DAMAGED, SET_VICTORY: VICTORY},
    DAMAGED: {IDLE: IDLE, SET_SCISSOR: DAMAGED, SET_ROCK: DAMAGED, SET_PAPER: DAMAGED, SET_DAMAGED: DAMAGED, SET_VICTORY: VICTORY },
    #VICTORY: {IDLE: VICTORY, SET_SCISSOR: VICTORY, SET_ROCK: VICTORY, SET_PAPER: VICTORY, SET_DAMAGED: VICTORY, SET_VICTORY: VICTORY}
}

class Player:
    image = None
    heart = None
    heart_count = 5
    event_que = []
    def __init__(self):
        self.image_x, self.image_y, self.image_w, self.image_h = 730, 200, 100, 100
        self.heart_x, self.heart_y, self.heart_w, self.heart_h = 770, 140, 20, 20
        self.image = load_image('resource_player\player_idle.png')
        self.heart = load_image('resource_player\heart.png')
        self.bgm = load_music('sound\PlayerDamaged.mp3')
        self.bgm.set_volume(64)
        self.cur_state = IDLE
        #self.enter_state[IDLE](self)
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def get_bb(self):
        return 730 + 30, 200 - 30, 730 + 40, 200 + 30

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
            self.add_event(key_event)

