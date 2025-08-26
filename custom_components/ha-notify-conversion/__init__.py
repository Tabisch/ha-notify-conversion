"""The eventsubscription integration."""

from __future__ import annotations
import logging

from homeassistant.core import HomeAssistant, ServiceCall
import homeassistant.helpers.config_validation as cv
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform

_PLATFORMS: list[Platform] = [Platform.NOTIFY]

from .const import DOMAIN

CONFIG_SCHEMA = cv.empty_config_schema(DOMAIN)

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: ConfigEntry) -> bool:
    """Set up RemoteNow from a config entry."""

    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up RemoteNow from a config entry."""
    await hass.config_entries.async_forward_entry_setups(entry, _PLATFORMS)

    return True


# TODO Update entry annotation
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, _PLATFORMS)
