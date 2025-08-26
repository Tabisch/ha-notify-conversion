import logging

from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.components.notify import NotifyEntity

from .const import *

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    async_add_entities(
        [
            NotifyConverter(entry=entry),
        ],
        update_before_add=True,
    )


class NotifyConverter(NotifyEntity):
    # Implement one of these methods.

    def __init__(
        self,
        entry: ConfigEntry,
    ) -> None:
        super().__init__()
        self._name = f"{entry.data['notifyServiceName']}_convert"
        self._attributename = f"{entry.data['notifyServiceName']}_convert"
        self._servicename = entry.data["notifyServiceName"]

        self._available = True

    def send_message(self, message: str, title: str | None = None) -> None:
        """Send a message."""

        _LOGGER.debug(f"{self._attributename} sending message: {message}")

        service_data = {"message": message}

        if title is not None:
            service_data["title"] = title

        self.hass.services.call(
            domain="notify",
            service=self._servicename,
            service_data=service_data,
        )

    @property
    def name(self) -> str:
        return self._name

    @property
    def unique_id(self) -> str:
        return self._name
