from django.urls import path
from django.urls import include
from .views import register,Login,Home
app_name='members'
urlpatterns = [
    path('',register, name='member-list'),
    path('login/',Login, name='mlogin'),

]