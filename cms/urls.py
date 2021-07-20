from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<slug>', views.menu_content, name='menu_content'),
    path('posts/', views.job_listing, name='job_listing'),
    path('posts/<job_slug>', views.job_content, name='job_content')
]
