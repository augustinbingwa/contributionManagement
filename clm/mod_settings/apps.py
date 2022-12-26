from django.apps import AppConfig

class ModSettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mod_settings'

    def ready(self):
        from mod_settings.subviews.globalVariable import GlobalVariable
        GlobalVariable.save_global_variables()
