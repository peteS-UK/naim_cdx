"""Infrared command sender for a Naim CDX entry."""

import asyncio

from homeassistant.components.infrared import async_send_command
from homeassistant.core import Context, HomeAssistant
from homeassistant.exceptions import ServiceValidationError
from infrared_protocols.commands import Command
from infrared_protocols.commands.rc5 import RC5Command

from .ir_codes import COMMANDS


class CdxRemote:
    """Serialize infrared commands and alternate the RC5 toggle bit."""

    def __init__(self, hass: HomeAssistant, emitter: str | None) -> None:
        self.hass = hass
        self.emitter = emitter
        self._lock = asyncio.Lock()
        self._toggle = 1

    async def send(self, command: str, context: Context | None = None) -> None:
        if command not in COMMANDS:
            raise ServiceValidationError(f"Unknown command: {command}")
        if not self.emitter:
            raise ServiceValidationError("An infrared emitter is required")

        template: Command = COMMANDS[command]
        async with self._lock:
            if isinstance(template, RC5Command):
                self._toggle = 1 - self._toggle
                ir_command: Command = RC5Command(
                    address=template.address,
                    command=template.command,
                    toggle=self._toggle,
                    modulation=template.modulation,
                    repeat_count=template.repeat_count,
                )
            else:
                ir_command = template

            await async_send_command(
                self.hass, self.emitter, ir_command, context=context
            )
