from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('profile/', views.profile_user, name="profile"),
    path('teachers/', views.teacher_listing, name="teacher_listing"), # TODO We may want to change this for 'employees'

]


