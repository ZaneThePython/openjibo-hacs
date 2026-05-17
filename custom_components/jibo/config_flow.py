import voluptuous as vol
from homeassistant import config_entries
from homeassistant.exceptions import HomeAssistantError

from .const import DOMAIN


class JiboConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            ip = user_input["jibo_ip"].strip()

            await self.async_set_unique_id(ip)
            self._abort_if_unique_id_configured()

            name = user_input.get("name", "").strip() or f"Jibo ({ip})"

            return self.async_create_entry(
                title=name,
                data={"jibo_ip": ip, "name": name},
            )

        data_schema = vol.Schema({
            vol.Required("name"): str,
            vol.Required("jibo_ip"): str,
        })

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors,
        )
