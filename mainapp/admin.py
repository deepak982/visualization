from django.contrib import admin
from .models import *

class DataAdmin(admin.ModelAdmin):
    list_display = ('intensity', 'topic' ,'region', 'start_year', 'end_year',)  # Note the comma at the end

admin.site.register(data, DataAdmin)