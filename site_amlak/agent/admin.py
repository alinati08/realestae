from django.contrib import admin
from .models import Agent

# Register your models here.

# admin.site.register(Agent)

class AgentAdmin(admin.ModelAdmin):
    list_display =('name','email','adress')
    list_filter = ("email",)
    search_fields=("name",)
    ordering=("name",)
    

admin.site.register(Agent,AgentAdmin)
