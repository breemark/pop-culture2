from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<slug>', views.menu_content, name='menu_content')
]
