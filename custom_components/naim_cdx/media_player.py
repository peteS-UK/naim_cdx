from __future__ import annotations

import logging

import voluptuous as vol
from homeassistant import config_entries, core
from homeassistant.components.media_player import (
    PLATFORM_SCHEMA,
    MediaPlayerEntity,
    MediaPlayerEntityFeature,
    MediaPlayerState,
    RepeatMode,
)
from homeassistant.const import CONF_NAME
from homeassistant.helpers import (
    config_validation as cv,
)
from homeassistant.helpers.device_registry import DeviceInfo

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_NAME, default=None): cv.string,
    }
)

COMMANDS = {
    "play": "JgAoABsfOTw5PTgfHD0aIDk8OjsdAAuEHR46Ozs4PB4bPR0eOTw5PB0ADQU=",
    "pause": "JgAwABweHB8bHzk9OCAcOB8fOR8cHxweHAALohwgGx8bHzk9OR4cPBwfOh4cHhwfHAANBQAAAAAAAAAA",
    "stop": "JgAUABwfOTw4PTkfGz0bHzo7HR45AA0FAAAAAA==",
    "next": "JgAWABweHB8bHzk9OB8cPBwfOTw5HxwADQUAAA==",
    "previous": "JgAUABwfOTk8OjseHTwcHzkeHDw5AA0FAAAAAA==",
    "repeat": "",
}

SUPPORT_CDX = (
    MediaPlayerEntityFeature.PAUSE
    | MediaPlayerEntityFeature.PREVIOUS_TRACK
    | MediaPlayerEntityFeature.NEXT_TRACK
    | MediaPlayerEntityFeature.PLAY_MEDIA
    | MediaPlayerEntityFeature.PLAY
    | MediaPlayerEntityFeature.STOP
    | MediaPlayerEntityFeature.REPEAT_SET
)


async def async_setup_entry(
    hass: core.HomeAssistant,
    config_entry: config_entries.ConfigEntry,
    async_add_entities,
) -> None:
    config = hass.data[DOMAIN][config_entry.entry_id]

    async_add_entities([CDXDevice(hass, config[CONF_NAME])])


class CDXDevice(MediaPlayerEntity):
    # Representation of a Emotiva Processor

    def __init__(self, hass, name):
        self._hass = hass
        self._state = MediaPlayerState.IDLE
        self._entity_id = "media_player.naim_cdx"
        self._unique_id = "naim_cdx_" + name.replace(" ", "_").replace(
            "-", "_"
        ).replace(":", "_")
        self._device_class = "receiver"
        self._name = name

    @property
    def should_poll(self):
        return False

    @property
    def icon(self):
        return "mdi:disc"

    @property
    def state(self) -> MediaPlayerState:
        return self._state

    @property
    def name(self):
        # return self._device.name
        return None

    @property
    def has_entity_name(self):
        return True

    @property
    def device_info(self) -> DeviceInfo:
        """Return the device info."""
        return DeviceInfo(
            identifiers={
                # Serial numbers are unique identifiers within a specific domain
                (DOMAIN, self._unique_id)
            },
            name=self._name,
            manufacturer="Naim",
            model="CDX",
        )

    @property
    def unique_id(self):
        return self._unique_id

    @property
    def entity_id(self):
        return self._entity_id

    @property
    def device_class(self):
        return self._device_class

    @entity_id.setter
    def entity_id(self, entity_id):
        self._entity_id = entity_id

    @property
    def supported_features(self) -> MediaPlayerEntityFeature:
        return SUPPORT_CDX

    @property
    def repeat(self):
        return RepeatMode.ONE

    async def _send_broadlink_command(self, command):
        await self._hass.services.async_call(
            "remote",
            "send_command",
            {
                "entity_id": "remote.rm_mini_3",
                "num_repeats": "1",
                "delay_secs": "0.4",
                "device": "CDX",
                "command": f"b64{COMMANDS[command]}",
            },
        )

    async def async_set_repeat(self, repeat: RepeatMode) -> None:
        """Set the repeat mode."""
        if repeat == RepeatMode.ONE:
            await self._send_broadlink_command("repeat")
            self.async_schedule_update_ha_state()

    async def async_media_stop(self) -> None:
        """Send stop command to media player."""
        await self._send_broadlink_command("stop")
        self._state = MediaPlayerState.IDLE
        self.async_schedule_update_ha_state()

    async def async_media_play(self) -> None:
        """Send play command to media player."""
        await self._send_broadlink_command("play")
        self._state = MediaPlayerState.PLAYING
        self.async_schedule_update_ha_state()

    async def async_media_pause(self) -> None:
        """Send pause command to media player."""
        await self._send_broadlink_command("pause")
        self._state = MediaPlayerState.PAUSED
        self.async_schedule_update_ha_state()

    async def async_media_next_track(self) -> None:
        """Send next track command."""
        await self._send_broadlink_command("next")

    async def async_media_previous_track(self) -> None:
        """Send next track command."""
        await self._send_broadlink_command("previous")

    async def async_update(self):
        pass
