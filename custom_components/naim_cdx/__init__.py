"""The Naim CDX component."""

from homeassistant import config_entries, core
from homeassistant.const import Platform
from homeassistant.helpers import issue_registry as ir

from .const import CONF_INFRARED_ENTITY_ID, CONF_REMOTE_ENTITY, DOMAIN
from .remote import CdxRemote

PLATFORMS = [Platform.MEDIA_PLAYER]


def _update_legacy_remote_issue(
    hass: core.HomeAssistant, entry: config_entries.ConfigEntry
) -> None:
    """Create a repair issue for entries that still use a legacy remote."""
    issue_id = f"reselect_ir_emitter_{entry.entry_id}"
    if entry.data.get(CONF_REMOTE_ENTITY) and not entry.data.get(
        CONF_INFRARED_ENTITY_ID
    ):
        ir.async_create_issue(
            hass,
            DOMAIN,
            issue_id,
            is_fixable=True,
            severity=ir.IssueSeverity.WARNING,
            translation_key="reselect_ir_emitter",
            translation_placeholders={"name": entry.title},
            data={"entry_id": entry.entry_id},
        )
    else:
        ir.async_delete_issue(hass, DOMAIN, issue_id)


async def async_setup_entry(
    hass: core.HomeAssistant, entry: config_entries.ConfigEntry
) -> bool:
    """Set up platform from a ConfigEntry."""

    _update_legacy_remote_issue(hass, entry)
    entry.runtime_data = CdxRemote(hass, entry.data.get(CONF_INFRARED_ENTITY_ID))
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(
    hass: core.HomeAssistant, entry: config_entries.ConfigEntry
) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    return unload_ok
