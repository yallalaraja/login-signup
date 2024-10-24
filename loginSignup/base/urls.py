from django.urls import path,include
from . views import *

urlpatterns = [
    path('home/',home,name='home'),
    path('signup/',regView,name='signup'),
    path('login/',loginView,name='login'),
    path('logout/',logoutView,name='logout')
]