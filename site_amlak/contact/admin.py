from django.contrib import admin
from .models import Contact

# Register your models here.

# admin.site.register(Contact)

class ContactAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'subject',  'date', 'content']
    readonly_fields = ( 'name',  'email', 'subject',  'date' , 'content')
    
admin.site.register(Contact , ContactAdmin)