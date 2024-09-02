from django.apps import AppConfig
from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    verbose_name=" کاربر ها "
    


class CustomAuthConfig(AppConfig):
    name = 'django.contrib.auth'
    verbose_name = ' کابر ها و دسترسی ها '




    
    
