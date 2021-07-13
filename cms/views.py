from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.conf import settings
from .models import Menu



# Create your views here.
def home(request):
    # Get Language Code
    # If Chinese, send Chinese, otherwise send English 
    if request.LANGUAGE_CODE == 'en-us':
        mainpage = Menu.objects.get(slug='main')
    elif request.LANGUAGE_CODE == 'zh-hans':
        mainpage = Menu.objects.get(slug='main-chinese')

    return render(request, 'cms/home.html', {'mainpage':mainpage})

def menu_content(request, slug):
    menu = get_object_or_404(Menu, slug=slug)
    if menu != 'admin' or menu != 'posts':
        return render(request, 'cms/page.html', {'menu': menu})