import os

# Default to development settings
settings_module = "config.settings"

# Use production settings if specified
if os.environ.get("DJANGO_SETTINGS_MODULE"):
    settings_module = os.environ.get("DJANGO_SETTINGS_MODULE")

# Export the settings module
__all__ = ["settings_module"]