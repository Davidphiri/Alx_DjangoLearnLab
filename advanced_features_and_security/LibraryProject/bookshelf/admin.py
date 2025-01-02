from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class CustomUserAdmin(BaseUserAdmin):
    list_display = ['email','username','is_staff']
    
admin.site.register(CustomUserAdmin, CustomUser)

