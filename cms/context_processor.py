from .models import Menu

def menus_processor(request):
    menus = Menu.objects.all()
    return {'menus': menus}