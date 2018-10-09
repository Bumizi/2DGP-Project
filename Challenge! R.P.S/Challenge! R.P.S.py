from pico2d import *
import random


# Game object class here
class MainScreen:
    def __init__(self):
        self.image = load_image('RPS.png')

    def draw(self):
        self.image.draw(300, 300)


class StartButton:
    def __init__(self):
        self.image = load_image('start-exit.jpg')
        self.x, self.y = 100, 100

    def draw(self):
        self.image.clip_draw(0, 225, 950, 450, self.x, self.y)


class ExitButton:
    def __init__(self):
        self.image = load_image('start-exit.jpg')
        self.x, self.y = 500, 100

    def draw(self):
        self.image.clip_draw(0, 450, 950, 225, self.x, self.y)


class Player:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


class Enemy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


class Ball21x21:
    def __init__(self):
        self.x, self.y = random.randint(40, 700), 600
        self.image = load_image('ball21x21.png')
        self.speed = random.randint(5, 20)

    def update(self):
        if self.y > 60:
            self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)


class Ball41x41:
    def __init__(self):
        self.x, self.y = random.randint(40, 700), 600
        self.image = load_image('ball41x41.png')
        self.speed = random.randint(5, 20)

    def update(self):
        if self.y > 70:
            self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN and collision(Draw_Button_Start.x, Draw_Button_Start.y, 500, 400, event.x, event.y):
             Level = True
        elif event.type == SDL_MOUSEBUTTONDOWN and exit_button:
            running = False


def collision(x1, y1, x2, y2, px, py):
    if(x1 < px < x2 & y1 < py < y2):
        return True

# initialization code
main_menu = True
start_button = True
exit_button = True
Level = False
open_canvas(1024, 768)
random_create = random.randint(1, 19)
player = Player()
enemy = Enemy()
team = [Player() for i in range(11)]
balls21 = Ball21x21()
balls41 = Ball41x41()
balls21t = [Ball21x21() for i in range(random_create)]
balls41t = [Ball41x41() for i in range(20 - random_create)]
Draw_MainScreen = MainScreen()
Draw_Button_Start = StartButton()
Draw_Button_Exit = ExitButton()
running = True


# game main loop code
#while main_menu:
#    handle_events()




while running:
    handle_events()
    for Player in team:
        Player.update()
    for balls21 in balls21t:
        balls21.update()
    for balls41 in balls41t:
        balls41.update()
    clear_canvas()
    Draw_MainScreen.draw()
    Draw_Button_Start.draw()
    Draw_Button_Exit.draw()
    for Player in team:
        Player.draw()
    for balls21 in balls21t:
        balls21.draw()
    for balls41 in balls41t:
        balls41.draw()
    update_canvas()
    delay(0.05)


# finalization code
close_canvas()