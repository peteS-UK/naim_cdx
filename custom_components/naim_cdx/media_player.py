"""Media player platform for the Naim CDX integration."""

from __future__ import annotations

import probatio
from homeassistant import config_entries, core
from homeassistant.components.media_player import MediaPlayerEntity
from homeassistant.components.media_player.const import (
    MediaPlayerDeviceClass,
    MediaPlayerEntityFeature,
    MediaPlayerState,
    RepeatMode,
)
from homeassistant.const import CONF_NAME
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers import entity_platform
from homeassistant.helpers.device_registry import DeviceInfo

from .const import (
    DOMAIN,
    MANUFACTURER,
    MODEL,
    SERVICE_SEND_COMMAND,
)

SUPPORT = (
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
    async_add_entities(
        [
            Device(
                config_entry.data[CONF_NAME],
                config_entry.runtime_data,
            )
        ]
    )

    # Register entity services
    platform = entity_platform.async_get_current_platform()
    platform.async_register_entity_service(
        SERVICE_SEND_COMMAND,
        {
            probatio.Required("command"): cv.string,
        },
        Device.send_command.__name__,
    )


class Device(MediaPlayerEntity):
    """Represent a Naim CDX."""

    _attr_assumed_state = True
    _attr_device_class = MediaPlayerDeviceClass.RECEIVER
    _attr_has_entity_name = True
    _attr_icon = "mdi:disc"
    _attr_name = None
    _attr_repeat = RepeatMode.ONE
    _attr_should_poll = False
    _attr_supported_features = SUPPORT

    def __init__(self, name, remote):
        self._attr_state = MediaPlayerState.IDLE
        self._attr_unique_id = f"{DOMAIN}_" + name.replace(" ", "_").replace(
            "-", "_"
        ).replace(":", "_")
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._attr_unique_id))},
            name=name,
            manufacturer=MANUFACTURER,
            model=MODEL,
        )
        self._remote = remote

    async def send_command(self, command):
        await self._send_remote_command(command)

    async def _send_remote_command(self, command):
        await self._remote.send(command, self._context)

    async def async_set_repeat(self, repeat: RepeatMode) -> None:
        """Set the repeat mode."""
        if repeat == RepeatMode.ONE:
            await self._send_remote_command("repeat")
            self.async_schedule_update_ha_state()

    async def async_media_stop(self) -> None:
        """Send stop command to media player."""
        await self._send_remote_command("stop")
        self._attr_state = MediaPlayerState.IDLE
        self.async_schedule_update_ha_state()

    async def async_media_play(self) -> None:
        """Send play command to media player."""
        await self._send_remote_command("play")
        self._attr_state = MediaPlayerState.PLAYING
        self.async_schedule_update_ha_state()

    async def async_media_pause(self) -> None:
        """Send pause command to media player."""
        await self._send_remote_command("pause")
        self._attr_state = MediaPlayerState.PAUSED
        self.async_schedule_update_ha_state()

    async def async_media_next_track(self) -> None:
        """Send next track command."""
        await self._send_remote_command("next")

    async def async_media_previous_track(self) -> None:
        """Send next track command."""
        await self._send_remote_command("previous")
