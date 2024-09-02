from django.contrib import admin
from .models import House , Property_Type , ContactAgent
# Register your models here.
admin.site.register(House)
admin.site.register(Property_Type)

class ContactAgentAdmin(admin.ModelAdmin):
    fields = ['name', 'house', 'email', 'message', 'agent', 'date']
    readonly_fields = ( 'name', 'house', 'email', 'message', 'agent', 'date')
    
admin.site.register(ContactAgent , ContactAgentAdmin)
