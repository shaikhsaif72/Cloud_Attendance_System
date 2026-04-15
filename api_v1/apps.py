from django.apps import AppConfig


class ApiV1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_v1'

    def ready(self):
        from django.contrib.auth.models import User

        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@gmail.com',
                password='admin123'
            )