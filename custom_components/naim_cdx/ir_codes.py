"""Naim CDX infrared commands."""

from infrared_protocols.commands.pronto import ProntoCommand
from infrared_protocols.commands.rc5 import RC5Command

CDX_ADDRESS = 0x14

COMMANDS = {
    "play": RC5Command(address=CDX_ADDRESS, command=0x35),
    # The captured pause signal is not represented by the available RC5 mapping.
    "pause": ProntoCommand.from_pronto_hex(
        "0000 006d 0017 0000 0007 007e 0024 002a 001e 002c 001f 0029 "
        "0047 004b 0047 0029 0025 0048 0021 002a 0047 0029 0020 0029 "
        "0021 0028 0021 0e86 0021 0028 0021 002a 001f 0029 0047 004d "
        "0048 0025 0023 004d 0021 0028 0046 0029 0021 002a 0020 002c "
        "001e 1040"
    ),
    "stop": RC5Command(address=CDX_ADDRESS, command=0x36),
    "next": RC5Command(address=CDX_ADDRESS, command=0x20),
    "previous": RC5Command(address=CDX_ADDRESS, command=0x21),
    "repeat": RC5Command(address=CDX_ADDRESS, command=0x1D),
    "disp": RC5Command(address=CDX_ADDRESS, command=0x0B),
    "one": RC5Command(address=CDX_ADDRESS, command=0x01),
    "two": RC5Command(address=CDX_ADDRESS, command=0x02),
    "three": RC5Command(address=CDX_ADDRESS, command=0x03),
    "four": RC5Command(address=CDX_ADDRESS, command=0x04),
    "five": RC5Command(address=CDX_ADDRESS, command=0x05),
    "six": RC5Command(address=CDX_ADDRESS, command=0x06),
    "seven": RC5Command(address=CDX_ADDRESS, command=0x07),
    "eight": RC5Command(address=CDX_ADDRESS, command=0x08),
    "nine": RC5Command(address=CDX_ADDRESS, command=0x09),
    "zero": RC5Command(address=CDX_ADDRESS, command=0x10),
}
