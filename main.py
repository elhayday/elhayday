loud_harah = 0
ball_sleep = 0
ball_roll = 0
ball: game.LedSprite = None
ball2: game.LedSprite = None
AB = 0
b = 0
shake = 0
chorzeh = 0

def on_pin_pressed_p0():
    global loud_harah
    loud_harah = randint(3, 3)
    if loud_harah == 1:
        loud_1()
    elif loud_harah == 2:
        loud_2()
    else:
        loud_3()
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def _2():
    global ball_sleep, ball_roll, ball, ball2
    basic.show_icon(IconNames.DIAMOND)
    basic.pause(100)
    ball_sleep = 0
    ball_roll = randint(1, 2)
    if 1 == ball_roll:
        ball = game.create_sprite(randint(0, 4), 0)
    if 2 == ball_roll:
        ball2 = game.create_sprite(randint(0, 4), 4)
    if ball.is_touching_edge():
        ball.delete()
        ball_sleep += 1
    if ball2.is_touching_edge():
        ball2.delete()
        ball_sleep += 1
    if 3 == ball_sleep:
        basic.show_string("zzz")

def on_button_pressed_a():
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_logo_up():
    for index in range(4):
        ball2.change(LedSpriteProperty.Y, -1)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def loud_2():
    music.play_melody("A - - - - - - - ", 120)
    basic.show_string("I WANT OUT")
def _3():
    basic.show_leds("""
        # # # # #
                # . . . #
                . # . # .
                # . . . #
                # # # # #
    """)

def on_button_pressed_ab():
    global AB
    AB += 1
    while AB == 3:
        basic.show_icon(IconNames.GHOST)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global b
    b += 1
    while b == 2:
        basic.show_icon(IconNames.YES)
        basic.pause(200)
        basic.show_string("num of steps")
        basic.show_number(shake)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global shake
    shake += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_logo_down():
    for index2 in range(4):
        ball.change(LedSpriteProperty.Y, 1)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def loud_3():
    global chorzeh
    music.play_melody("C - - - - - - - ", 120)
    chorzeh = randint(2, 2)
    if chorzeh == 1:
        _1()
    elif chorzeh == 2:
        _2()
    else:
        _3()

def on_logo_pressed():
    basic.show_string("ZZZ")
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def loud_1():
    music.play_melody("C5 - - - - - - - ", 120)
    basic.show_string("I AM HUNGRY")
def _1():
    basic.show_icon(IconNames.SKULL)
    led.set_brightness(255)
    basic.pause(100)
    led.set_brightness(200)
    basic.pause(100)
    led.set_brightness(130)
    basic.pause(100)
    led.set_brightness(50)
    basic.pause(100)
    led.set_brightness(0)