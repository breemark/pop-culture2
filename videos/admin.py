from django.contrib import admin
from .models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'authorized',)
    exclude = ('description',)

admin.site.register(UserProfile, UserProfileAdmin)
