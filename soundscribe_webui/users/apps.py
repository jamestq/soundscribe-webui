from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "soundscribe_webui.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import soundscribe_webui.users.signals  # noqa F401
        except ImportError:
            pass
