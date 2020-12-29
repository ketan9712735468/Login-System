from django.urls import path
from .views import (login_page,
        register_page,
        home_page,
        logoutuser)

urlpatterns = [
    path('', home_page,name='home'),
    path('logout',logoutuser,name='logout'),
    path('login', login_page,name='login'),
    path('register', register_page, name='register'),
]