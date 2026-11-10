"""Config flow for the Naim CDX integration."""

import homeassistant.helpers.config_validation as cv
import probatio
from homeassistant import config_entries, core
from homeassistant.components.infrared import async_get_emitters
from homeassistant.const import CONF_NAME
from homeassistant.helpers.selector import EntitySelector, EntitySelectorConfig

from .const import CONF_INFRARED_ENTITY_ID, DOMAIN


def emitter_schema(emitters: list[str]) -> probatio.Schema:
    """Build the schema for selecting an available infrared emitter."""
    return probatio.Schema(
        {
            probatio.Required(CONF_INFRARED_ENTITY_ID): EntitySelector(
                EntitySelectorConfig(domain="infrared", include_entities=emitters)
            )
        }
    )


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_PUSH

    @staticmethod
    @core.callback
    def async_get_options_flow(config_entry: config_entries.ConfigEntry):
        """Return the options flow for an existing CDX."""
        return CdxOptionsFlow()

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
                    **emitter_schema(emitters).schema,
                }
            ),
            errors=errors,
        )


class CdxOptionsFlow(config_entries.OptionsFlowWithReload):
    """Change the configured infrared emitter."""

    async def async_step_init(self, user_input: dict | None = None):
        """Select an emitter and reload the integration when it changes."""
        entry = self.config_entry
        if not entry.data.get(CONF_INFRARED_ENTITY_ID):
            return self.async_abort(reason="migration_required")

        emitters = async_get_emitters(self.hass)
        if not emitters:
            return self.async_abort(reason="no_emitters")

        errors: dict[str, str] = {}
        if user_input is not None:
            if user_input.get(CONF_INFRARED_ENTITY_ID) not in emitters:
                errors["base"] = "invalid_emitter"
            else:
                return self.async_create_entry(title="", data=user_input)

        current = (
            user_input if user_input is not None else {**entry.data, **entry.options}
        )
        return self.async_show_form(
            step_id="init",
            data_schema=self.add_suggested_values_to_schema(
                emitter_schema(emitters), current
            ),
            errors=errors,
        )
