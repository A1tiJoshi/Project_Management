from django.apps import AppConfig

# Define the configuration for the 'core' application
class CoreConfig(AppConfig):
    # Specify the default auto field type for models in this app
    default_auto_field = "django.db.models.BigAutoField"
    # Set the name of the application
    name = "core"
