from pico2d import *
import game_world
from block import Block

# Boy State
#IDLE, SCISSOR, ROCK, PAPER = range(4)

# Boy Event
IDLE, SET_SCISSOR, SET_ROCK, SET_PAPER = range(4)

key_event_table = {
    (SDL_KEYDOWN, SDLK_1): SET_SCISSOR,
    (SDL_KEYDOWN, SDLK_2): SET_ROCK,
    (SDL_KEYDOWN, SDLK_3): SET_PAPER,
}


# Player States

# IDLE state functions
class IDLE:
    @staticmethod
    def enter(player, event):
        if event == SET_PAPER:
            pass
        elif event == SET_ROCK:
            pass
        elif event == SET_SCISSOR:
            pass
        player.frame = 0
        #Player.timer = 100

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.image = load_image('player_idle.png')
        player.frame = (player.frame + 1) % 4
        #boy.timer -= 1
        #if player.timer == 0:
            #player.add_event(SLEEP_TIMER)
            #pass

    @staticmethod
    def draw(player):
        player.image.clip_composite_draw(player.frame * int(202 / 4), 0, int(202 / 4), 93, 0, 'h',
                                         player.image_x, player.image_y, player.image_w, player.image_h)
        for i in range(player.heart_count):
            player.heart.clip_draw(0, 0, 620, 620, player.heart_x - i * player.heart_w, player.heart_y, player.heart_w,
                                 player.heart_h)
        delay(0.05)
        #if boy.dir == 1:
            #boy.image.clip_draw(boy.frame * 100, 300, 100, 100, boy.x, boy.y)
        #else:
            #boy.image.clip_draw(boy.frame * 100, 200, 100, 100, boy.x, boy.y)

# ROCK state functions
class ROCK:
    @staticmethod
    def enter(player, event):
        if event == SET_PAPER:
            pass
        elif event == SET_ROCK:
            pass
        elif event == SET_SCISSOR:
            pass
        player.frame = 0
        player.hand = player.hand = load_image('my_rock.png')

    @staticmethod
    def exit(player, event):
        #if event == SPACE:
            #boy.fire_ball()
        pass

    @staticmethod
    def do(player):
        player.image = load_image('player_attack1.png')
        player.frame = (player.frame + 1) % 3
        #player.timer -= 1
        #player.x += player.velocity
        #player.x = clamp(25, player.x, 1600 - 25)

    @staticmethod
    def draw(player):
        player.image.clip_composite_draw(player.frame * int(165 / 3), 0, int(165 / 3), 100, 0, 'h', player.image_x, player.image_y, player.image_w, player.image_h)
        player.hand.clip_draw(0, 0, 120, 120, player.hand_x, player.hand_y, player.hand_w, player.hand_h)
        for i in range(player.heart_count):
            player.heart.clip_draw(0, 0, 620, 620, player.heart_x - i * player.heart_w, player.heart_y, player.heart_w, player.heart_h)
        delay(0.05)

# SCISSOR state functions
class SCISSOR:
    @staticmethod
    def enter(player, event):
        if event == SET_PAPER:
            pass
        elif event == SET_ROCK:
            pass
        elif event == SET_SCISSOR:
            pass
        player.frame = 0
        player.hand = load_image('my_scissor.png')
        #boy.timer = 50

    @staticmethod
    def exit(player, event):
        #if event == SPACE:
            #boy.fire_ball()
        pass

    @staticmethod
    def do(player):
        player.image = load_image('player_attack1.png')
        player.frame = (player.frame + 1) % 3
        #boy.timer -= 1
        #boy.x += boy.velocity * 5
        #boy.x = clamp(25, boy.x, 1600 - 25)
            #boy.add_event(DASH_TIMER)

    @staticmethod
    def draw(player):
        player.image.clip_composite_draw(player.frame * int(165 / 3), 0, int(165 / 3), 100, 0, 'h', player.image_x, player.image_y, player.image_w, player.image_h)
        player.hand.clip_draw(0, 0, 120, 120, player.hand_x, player.hand_y, player.hand_w, player.hand_h)
        for i in range(player.heart_count):
            player.heart.clip_draw(0, 0, 620, 620, player.heart_x - i * player.heart_w, player.heart_y, player.heart_w, player.heart_h)
        delay(0.05)
        #if boy.velocity == 1:
            #boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        #else:
            #boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)

# PAPER state functions
class PAPER:
    @staticmethod
    def enter(player, event):
        player.frame = 0
        player.hand = load_image('my_paper.png')

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.image = load_image('player_attack1.png')
        player.frame = (player.frame + 1) % 3

    @staticmethod
    def draw(player):
        player.image.clip_composite_draw(player.frame * int(165 / 3), 0, int(165 / 3), 100, 0, 'h', player.image_x, player.image_y, player.image_w, player.image_h)
        player.hand.clip_draw(0, 0, 120, 120, player.hand_x, player.hand_y, player.hand_w, player.hand_h)
        for i in range(player.heart_count):
            player.heart.clip_draw(0, 0, 620, 620, player.heart_x - i * player.heart_w, player.heart_y, player.heart_w, player.heart_h)
        delay(0.05)
        #if boy.dir == 1:
            #boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100, 3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
        #else:
            #boy.image.clip_composite_draw(boy.frame * 100, 200, 100, 100, -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)
        pass


next_state_table = {
    IDLE: {SET_SCISSOR: SCISSOR, SET_ROCK: ROCK, SET_PAPER: PAPER},
    SCISSOR: {SET_SCISSOR: IDLE, SET_ROCK: ROCK, SET_PAPER: PAPER},
    ROCK: {SET_SCISSOR: SCISSOR, SET_ROCK: IDLE, SET_PAPER: PAPER},
    PAPER: {SET_SCISSOR: SCISSOR, SET_ROCK: ROCK, SET_PAPER: IDLE}
}

class Player:
    image = None
    hand = None
    heart = None
    def __init__(self):
        self.event_que = []
        self.image_x, self.image_y, self.image_w, self.image_h = 730, 200, 100, 100
        self.hand_x, self.hand_y, self.hand_w, self.hand_h = self.image_x-100, self.image_y, 80, 80
        self.heart_x, self.heart_y, self.heart_w, self.heart_h = 730, 150, 20, 20
        self.image = load_image('player_idle.png')
        self.heart = load_image('heart.png')
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

