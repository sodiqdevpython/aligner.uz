from django.contrib import admin
from .models import APIToken

@admin.register(APIToken)
class APITokenAdmin(admin.ModelAdmin):
    list_display = ('name', 'usage_count', 'is_active')
    list_editable = ('is_active',)
