# archivo: authenticacion/apps.py
from django.apps import AppConfig

class AuthenticationConfig(AppConfig):
    name = 'authentication'

    def ready(self):
        import authentication.signals  # Importa las señales al iniciar la aplicación
