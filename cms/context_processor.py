from django.conf import settings
from .models import Menu

def menus_processor(request):
    language = request.LANGUAGE_CODE
    menus = Menu.objects.all().filter(language=language, active=True,).exclude(slug='main').exclude(slug='main-chinese')
    return {'menus': menus, 'language': language}