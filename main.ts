let shake = 0
let loud_harah = 0
let AB = 0
let b = 0
let chorzeh = 0
input.onPinPressed(TouchPin.P0, function () {
    shake = 0
    loud_harah = randint(3, 3)
    if (loud_harah == 1) {
        loud_1()
    } else if (loud_harah == 2) {
        loud_2()
    } else {
        loud_3()
    }
})
function _2 () {
    basic.showIcon(IconNames.Diamond)
}
input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Happy)
})
function loud_2 () {
    music.playMelody("A - - - - - - - ", 120)
    basic.showString("I WANT OUT")
}
function _3 () {
    basic.showLeds(`
        # # # # #
        # . . . #
        . # . # .
        # . . . #
        # # # # #
        `)
}
input.onButtonPressed(Button.AB, function () {
    AB += 1
    while (AB == 3) {
        basic.showIcon(IconNames.Ghost)
    }
})
input.onButtonPressed(Button.B, function () {
    b += 1
    while (b == 2) {
        basic.showIcon(IconNames.Yes)
        basic.pause(200)
        basic.showString("num of steps")
        basic.showNumber(shake)
    }
})
input.onGesture(Gesture.Shake, function () {
    shake += 1
})
function loud_3 () {
    music.playMelody("C - - - - - - - ", 120)
    chorzeh = randint(1, 1)
    if (chorzeh == 1) {
        _1()
    } else if (chorzeh == 2) {
        _2()
    } else {
        _3()
    }
}
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showString("ZZZ")
})
function loud_1 () {
    music.playMelody("C5 - - - - - - - ", 120)
    basic.showString("I AM HUNGRY")
}
function _1 () {
    basic.showIcon(IconNames.Skull)
    led.setBrightness(255)
    basic.pause(100)
    led.setBrightness(200)
    basic.pause(100)
    led.setBrightness(130)
    basic.pause(100)
    led.setBrightness(50)
    basic.pause(100)
    led.setBrightness(0)
}
