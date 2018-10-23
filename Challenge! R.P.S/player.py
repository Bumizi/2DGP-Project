from pico2d import *

# Boy State
IDLE, SCISSOR, ROCK, PAPER = range(4)

# Boy Event
SET_SCISSOR, SET_ROCK, SET_PAPER = range(3)

key_event_table = {
    (SDL_KEYDOWN, SDLK_1): SET_SCISSOR,
    (SDL_KEYDOWN, SDLK_2): SET_ROCK,
    (SDL_KEYDOWN, SDLK_3): SET_PAPER,
}

next_state_table = {
    IDLE: {SET_SCISSOR: SCISSOR, SET_ROCK: ROCK, SET_PAPER: PAPER},
    SCISSOR: {SET_SCISSOR: IDLE, SET_ROCK: ROCK, SET_PAPER: PAPER},
    ROCK: {SET_SCISSOR: SCISSOR, SET_ROCK: IDLE, SET_PAPER: PAPER},
    PAPER: {SET_SCISSOR: SCISSOR, SET_ROCK: ROCK, SET_PAPER: IDLE}
}


class Player:
    image = None
    def __init__(self):
        self.event_que = []
        self.x, self.y = 700, 250
        self.w, self.h = 100, 100
        if Player.image == None:
            Player.image = load_image('player_idle.png')
        self.cur_state = IDLE
        self.dir = 1
        self.velocity = 0
        self.enter_state[IDLE](self)

    # IDLE state functions
    def enter_IDLE(self):
        #self.timer = 1000
        self.frame = 0

    def exit_IDLE(self):
        pass

    def do_IDLE(self):
        self.frame = (self.frame + 1) % 4
        #self.timer -= 1
        pass

    def draw_IDLE(self):
        #if self.dir == 1:
            #self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        #else:
            #self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        self.image.clip_composite_draw(self.frame * int(202/4), 0, int(202/4), 93, 0, 'h', self.x, self. y, self.w, self.h)
        delay(0.05)
        pass

    # ROCK state functions
    def enter_ROCK(self):
        self.frame = 0
        #self.dir = self.velocity
        pass

    def exit_ROCK(self):
        pass

    def do_ROCK(self):
        Player.image = load_image('player_attack1.png')
        self.frame = (self.frame + 1) % 3
        #self.x += self.velocity
        #self.x = clamp(25, self.x, 800 - 25)
        pass

    def draw_ROCK(self):
        #if self.velocity == 1:
            #self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
       #else:
            #self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        self.image.clip_composite_draw(self.frame * int(165 / 3), 0, int(165 / 3), 100, 0, 'h', self.x, self.y, self.w, self.h)
        delay(0.1)

    # SCISSOR state functions
    def enter_SCISSOR(self):
        self.frame = 0
        #self.dir = self.velocity
        pass

    def exit_SCISSOR(self):
        pass

    def do_SCISSOR(self):
        Player.image = load_image('player_attack1.png')
        self.frame = (self.frame + 1) % 3
        #self.x += self.velocity
        #self.x = clamp(25, self.x, 800 - 25)
        pass

    def draw_SCISSOR(self):
        #if self.velocity == 1:
            #self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        #else:
            #self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        self.image.clip_composite_draw(self.frame * int(165 / 3), 0, int(165 / 3), 100, 0, 'h', self.x, self.y, self.w, self.h)
        delay(0.1)

        # PAPER state functions
    def enter_PAPER(self):
        self.frame = 0
        #self.dir = self.velocity
        pass

    def exit_PAPER(self):
        pass

    def do_PAPER(self):
        Player.image = load_image('player_attack1.png')
        self.frame = (self.frame + 1) % 3
        #self.x += self.velocity
        #self.x = clamp(25, self.x, 800 - 25)
        pass

    def draw_PAPER(self):
        #if self.velocity == 1:
            #self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        #else:
            #self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        self.image.clip_composite_draw(self.frame * int(165 / 3), 0, int(165 / 3), 100, 0, 'h', self.x, self.y, self.w, self.h)
        delay(0.1)

    # SLEEP state functions
    def enter_SLEEP(self):
        print('Enter SLEEP')
        self.frame = 0

    def exit_SLEEP(self):
        print('Exit SLEEP')

    def do_SLEEP(self):
        self.frame = (self.frame + 1) % 8

    def draw_SLEEP(self):
        if self.dir == 1:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100, 3.141592/2, '', self.x-25, self.y-25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, -3.141592/2, '', self.x+25, self.y-25, 100, 100)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def change_state(self,  state):
        self.exit_state[self.cur_state](self)
        self.enter_state[state](self)
        self.cur_state = state
        pass

    enter_state = {IDLE: enter_IDLE, ROCK: enter_ROCK, SCISSOR: enter_SCISSOR, PAPER: enter_PAPER}
    exit_state = {IDLE: exit_IDLE, ROCK: exit_ROCK, SCISSOR: exit_SCISSOR, PAPER: exit_PAPER}
    do_state = {IDLE: do_IDLE, ROCK: do_ROCK, SCISSOR: do_SCISSOR, PAPER: do_PAPER}
    draw_state = {IDLE: draw_IDLE, ROCK: draw_ROCK, SCISSOR: draw_SCISSOR, PAPER: draw_PAPER}

    def update(self):
        self.do_state[self.cur_state](self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.change_state(next_state_table[self.cur_state][event])
        pass

    def draw(self):
        self.draw_state[self.cur_state](self)
        pass

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if key_event == SET_SCISSOR:
                self.velocity += 1
            elif key_event == SET_PAPER:
                self.velocity -= 1
            elif key_event == SET_ROCK:
                self.velocity -= 1
            self.add_event(key_event)

