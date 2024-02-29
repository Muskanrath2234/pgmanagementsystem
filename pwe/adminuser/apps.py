from django.apps import AppConfig


class AdminuserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'adminuser'


    def ready(self):
        import adminuser.signals