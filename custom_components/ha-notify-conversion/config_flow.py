"""Config flow for the RemoteNow integration."""

from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.core import _hass
from homeassistant.helpers.selector import selector
from .const import *

_LOGGER = logging.getLogger(__name__)


class NotifyConversionFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for NotifyConversion."""

    VERSION = 1

    async def async_step_user(self, user_input=None) -> ConfigFlowResult:
        """Handle the initial step."""

        services = set(_hass.hass.services.async_services()["notify"].keys())

        # remove default
        services.remove("send_message")
        services.remove("persistent_notification")
        services.remove("notify")

        # remove already configured
        for entry in self.hass.config_entries._entries.get_entries_for_domain(
            domain=DOMAIN
        ):
            services.remove(entry.data["notifyServiceName"])

        notifyServicesList = list(services)

        STEP_USER_DATA_SCHEMA = vol.Schema(
            {
                vol.Required("notifyServiceName"): selector(
                    {"select": {"options": notifyServicesList}}
                )
            }
        )

        errors: dict[str, str] = {}
        if user_input is not None:
            return self.async_create_entry(
                title=user_input["notifyServiceName"], data=user_input
            )

        return self.async_show_form(
            step_id="user", data_schema=STEP_USER_DATA_SCHEMA, errors=errors
        )
