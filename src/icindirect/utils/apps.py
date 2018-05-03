from django.apps import AppConfig


class UtilsConfig(AppConfig):
    name = 'icindirect.utils'

    def ready(self):
        from . import checks  # noqa
