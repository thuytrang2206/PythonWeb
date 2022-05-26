import imp
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('',views.index),
    path('contact/',views.contact,name= 'contact'),
    path('register/', views.register, name="register"),
    path(r'login/',auth_views.LoginView.as_view(template_name="pages/login.html"), name="login"),
    path(r'logout/',auth_views.LogoutView.as_view(next_page="/"), name="logout"),
]