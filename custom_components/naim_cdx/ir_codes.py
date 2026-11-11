"""Naim CDX infrared commands."""

from .codes.naim.gen1_cd import NaimGen1CDCode as Code

COMMANDS = {
    "play": Code.PLAY.to_command(),
    "pause": Code.PAUSE.to_command(),
    "stop": Code.STOP.to_command(),
    "next": Code.NEXT.to_command(),
    "previous": Code.PREVIOUS.to_command(),
    "repeat": Code.REPEAT.to_command(),
    "disp": Code.DISPLAY.to_command(),
    "one": Code.ONE.to_command(),
    "two": Code.TWO.to_command(),
    "three": Code.THREE.to_command(),
    "four": Code.FOUR.to_command(),
    "five": Code.FIVE.to_command(),
    "six": Code.SIX.to_command(),
    "seven": Code.SEVEN.to_command(),
    "eight": Code.EIGHT.to_command(),
    "nine": Code.NINE.to_command(),
    "zero": Code.ZERO.to_command(),
}
