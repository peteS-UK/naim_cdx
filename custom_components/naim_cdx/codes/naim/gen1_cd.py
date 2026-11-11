"""Infrared codes for first-generation Naim CD players."""

from enum import Enum, unique

from infrared_protocols.commands import Command
from infrared_protocols.commands.rc5 import RC5Command

CD_ADDRESS = 0x14


@unique
class NaimGen1CDCode(Enum):
    """Commands for first-generation Naim CD players."""

    PLAY = 0x35
    PAUSE = 0x30
    STOP = 0x36
    NEXT = 0x20
    PREVIOUS = 0x21
    REPEAT = 0x1D
    DISPLAY = 0x0B
    ONE = 0x01
    TWO = 0x02
    THREE = 0x03
    FOUR = 0x04
    FIVE = 0x05
    SIX = 0x06
    SEVEN = 0x07
    EIGHT = 0x08
    NINE = 0x09
    ZERO = 0x10

    def to_command(self, repeat_count: int = 0, *, toggle: int = 0) -> Command:
        """Build the infrared command."""
        return RC5Command(
            address=CD_ADDRESS,
            command=self.value,
            toggle=toggle,
            repeat_count=repeat_count,
        )
