from django.contrib import admin
from .models import Event

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_date', 'venue')
    ordering = ('-event_date',) #tuple
    search_fields = ('name', 'venue')