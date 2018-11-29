from pico2d import *
import game_framework
import game_world
import victory_state
import dead_state

#from enemy_block import Enemy_Block

PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 20.0 #km/hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS*PIXEL_PER_METER)

#Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
FRAMES_PER_ACTION = 4


# Enemy Event
#IDLE, SET_SCISSOR, SET_ROCK, SET_PAPER, SET_DAMAGED, SPACE = range(6)
IDLE, SPACE, SET_DAMAGED, SET_ATTACK, SET_VICTORY = range(5)

key_event_table = {
    #(SDL_KEYDOWN, SDLK_1): SET_SCISSOR,
    #(SDL_KEYDOWN, SDLK_2): SET_ROCK,
    #(SDL_KEYDOWN, SDLK_3): SET_PAPER,
    #(SDL_KEYDOWN, SDLK_4): SET_DAMAGED,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_SPACE): SET_ATTACK
}


# Enemy States

# IDLE state functions
class IDLE:
    @staticmethod
    def enter(enemy, event):
        enemy.frame = 0

    @staticmethod
    def exit(enemy, event):
        if event == SPACE:
            enemy.fire_ball()
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
            if i < 5:
                enemy.heart.clip_draw(0, 0, 620, 620, enemy.heart_x + i * enemy.heart_w, enemy.heart_y,
                                      enemy.heart_w - 1, enemy.heart_h)
            else:
                enemy.heart.clip_draw(0, 0, 620, 620, enemy.heart_x + (i-5) * enemy.heart_w,
                                      enemy.heart_y - enemy.heart_h - 5, enemy.heart_w - 1, enemy.heart_h)


# Attack state functions
class ATTACK:
    @staticmethod
    def enter(enemy, event):
        enemy.frame = 0
        enemy.image = load_image('resource_enemy\enemy_attack1.png')

    @staticmethod
    def exit(enemy, event):
        if event == SPACE:
            pass

    @staticmethod
    def do(enemy):
        if enemy.frame < 2.5:
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
            if i < 5:
                enemy.heart.clip_draw(0, 0, 620, 620, enemy.heart_x + i * enemy.heart_w, enemy.heart_y,
                                      enemy.heart_w - 1, enemy.heart_h)
            else:
                enemy.heart.clip_draw(0, 0, 620, 620, enemy.heart_x + (i-5) * enemy.heart_w,
                                      enemy.heart_y - enemy.heart_h - 5, enemy.heart_w - 1, enemy.heart_h)


# DAMAGED state functions
class DAMAGED:
    damaged_timer = 0
    @staticmethod
    def enter(enemy, event):
        enemy.frame = 0
        enemy.heart_count -= 1
        enemy.image = load_image('resource_enemy\enemy_damaged.png')
        enemy.bgm.play()

    @staticmethod
    def exit(enemy, event):
        if event == SPACE:
            enemy.fire_ball()
        pass

    @staticmethod
    def do(enemy):
        if enemy.heart_count != 0:
            if enemy.frame < 1.5:
                enemy.frame = (enemy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
            else:
                enemy.add_event(IDLE)
        else:
            if enemy.frame < 1.5:
                enemy.image = load_image('resource_enemy\enemy_dead.png')
                enemy.frame = (enemy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
            else:
                game_framework.push_state(victory_state)
                pass

    @staticmethod
    def draw(enemy):
        #if enemy.heart_count > 0:
        enemy.image.clip_draw(int(enemy.frame) * int(144 / 2), 0, int(144 / 2), 95, enemy.image_x, enemy.image_y, enemy.image_w, enemy.image_h)
        #else:
            #enemy.image.clip_draw(int(enemy.frame) * int(322 / 4.2), 0, int(322 / 4.2), 90,
                                            #enemy.image_x, enemy.image_y, enemy.image_w, enemy.image_h)
        for i in range(enemy.heart_count):
            if i < 5:
                enemy.heart.clip_draw(0, 0, 620, 620, enemy.heart_x + i * enemy.heart_w, enemy.heart_y, enemy.heart_w - 1, enemy.heart_h)
            else:
                enemy.heart.clip_draw(0, 0, 620, 620, enemy.heart_x + (i-5) * enemy.heart_w, enemy.heart_y - enemy.heart_h - 5, enemy.heart_w - 1, enemy.heart_h)


# VICTORY state functions
class VICTORY:
    @staticmethod
    def enter(enemy, event):
        enemy.frame = 0
        enemy.image = load_image('resource_enemy\enemy_victory.png')

    @staticmethod
    def exit(enemy, event):
        pass

    @staticmethod
    def do(enemy):
        if enemy.frame < 1.5:
            enemy.frame = (enemy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        else:
            game_framework.push_state(dead_state)

    @staticmethod
    def draw(enemy):
        enemy.image.clip_composite_draw(int(enemy.frame) * int(296 / 4), 0, int(296 / 4), 96, 0, 'h', enemy.image_x, enemy.image_y, enemy.image_w, enemy.image_h)



next_state_table = {
    IDLE: {SET_ATTACK: ATTACK, SET_DAMAGED: DAMAGED, SPACE: IDLE, SET_VICTORY: VICTORY},
    ATTACK: {SET_ATTACK: ATTACK, SET_DAMAGED: DAMAGED, SPACE: ATTACK, SET_VICTORY: VICTORY},
    DAMAGED: {IDLE: IDLE, SET_ATTACK: IDLE, SET_DAMAGED: IDLE, SPACE: IDLE, SET_VICTORY: VICTORY},
    #VICTORY: {IDLE: VICTORY, SET_ATTACK: VICTORY, SET_DAMAGED: VICTORY, SPACE: VICTORY, SET_VICTORY: VICTORY}
}

class Enemy:
    image = None
    heart = None
    heart_count = 10
    event_que = []
    def __init__(self):
        self.image_x, self.image_y, self.image_w, self.image_h = 60, 200, 100, 100
        self.heart_x, self.heart_y, self.heart_w, self.heart_h = 20, 140, 20, 20
        self.image = load_image('resource_enemy\enemy_idle.png')
        self.heart = load_image('resource_enemy\heart.png')
        self.bgm = load_music('sound\EnemyDamaged.mp3')
        self.bgm.set_volume(44)
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def fire_ball(self):
        pass

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


