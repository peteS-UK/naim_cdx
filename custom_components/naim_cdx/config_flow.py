"""Config flow for the Naim CDX integration."""

import homeassistant.helpers.config_validation as cv
import probatio
from homeassistant import config_entries
from homeassistant.components.infrared import async_get_emitters
from homeassistant.const import CONF_NAME
from homeassistant.helpers.selector import EntitySelector, EntitySelectorConfig

from .const import CONF_INFRARED_ENTITY_ID, DOMAIN


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_PUSH

    async def async_step_user(self, user_input: dict | None = None):
        """Invoked when a user initiates a flow via the user interface."""
        emitters = async_get_emitters(self.hass)
        if not emitters:
            return self.async_abort(reason="no_emitters")

        errors: dict[str, str] = {}
        if user_input is not None:
            if not user_input.get(CONF_NAME, "").strip():
                errors["base"] = "data"
            elif user_input.get(CONF_INFRARED_ENTITY_ID) not in emitters:
                errors["base"] = "invalid_emitter"

            if not errors:
                return self.async_create_entry(
                    title=user_input[CONF_NAME], data=user_input
                )

        return self.async_show_form(
            step_id="user",
            data_schema=probatio.Schema(
                {
                    probatio.Required(CONF_NAME, default="Naim CDX"): cv.string,
                    probatio.Required(CONF_INFRARED_ENTITY_ID): EntitySelector(
                        EntitySelectorConfig(
                            domain="infrared", include_entities=emitters
                        )
                    ),
                }
            ),
            errors=errors,
        )
