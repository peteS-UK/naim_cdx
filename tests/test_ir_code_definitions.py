"""Verify the Naim CD code definitions and integration mapping."""

import unittest

from infrared_protocols.commands.pronto import ProntoCommand
from infrared_protocols.commands.rc5 import RC5Command

from custom_components.naim_cdx.codes.naim.gen1_cd import NaimGen1CDCode
from custom_components.naim_cdx.ir_codes import COMMANDS


class CDCodeTests(unittest.TestCase):
    """Keep the original CDX commands and captured pause signal."""

    def test_command_mapping(self):
        expected = {
            "play": 0x35,
            "stop": 0x36,
            "next": 0x20,
            "previous": 0x21,
            "repeat": 0x1D,
            "disp": 0x0B,
            "one": 0x01,
            "two": 0x02,
            "three": 0x03,
            "four": 0x04,
            "five": 0x05,
            "six": 0x06,
            "seven": 0x07,
            "eight": 0x08,
            "nine": 0x09,
            "zero": 0x10,
        }
        self.assertEqual(set(COMMANDS), {*expected, "pause"})
        for key, command in expected.items():
            with self.subTest(key=key):
                actual = COMMANDS[key]
                self.assertIsInstance(actual, RC5Command)
                self.assertEqual((actual.address, actual.command), (0x14, command))
                self.assertEqual(actual.repeat_count, 0)

    def test_pause_capture_is_preserved(self):
        expected = ProntoCommand.from_pronto_hex(
            "0000 006d 0017 0000 0007 007e 0024 002a 001e 002c 001f 0029 "
            "0047 004b 0047 0029 0025 0048 0021 002a 0047 0029 0020 0029 "
            "0021 0028 0021 0e86 0021 0028 0021 002a 001f 0029 0047 004d "
            "0048 0025 0023 004d 0021 0028 0046 0029 0021 002a 0020 002c "
            "001e 1040"
        )
        self.assertEqual(
            COMMANDS["pause"].get_raw_timings(), expected.get_raw_timings()
        )
        self.assertEqual(COMMANDS["pause"].modulation, expected.modulation)

    def test_rc5_toggle_and_repeat(self):
        command = NaimGen1CDCode.PLAY.to_command(repeat_count=2, toggle=1)
        self.assertIsInstance(command, RC5Command)
        self.assertEqual((command.address, command.command), (0x14, 0x35))
        self.assertEqual((command.toggle, command.repeat_count), (1, 2))


if __name__ == "__main__":
    unittest.main()
