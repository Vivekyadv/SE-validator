from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import signup, login, logout


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

]