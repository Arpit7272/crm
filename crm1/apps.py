from django.apps import AppConfig


class Crm1Config(AppConfig):
    name = 'crm1'

    def ready(self):
        import crm1.signals
