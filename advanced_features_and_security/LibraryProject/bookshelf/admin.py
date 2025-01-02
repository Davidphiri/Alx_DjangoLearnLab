from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    list_display = ['email','username','is_staff']
    
admin.site.register(UserAdmin)

