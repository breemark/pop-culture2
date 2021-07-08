from django.contrib import admin
from .models import Post, Menu

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'active', )

admin.site.register(Post, PostAdmin)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'active', )

admin.site.register(Menu, MenuAdmin)
