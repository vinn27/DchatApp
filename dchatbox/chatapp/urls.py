from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', CreateRoom, name='create-room'),
    path('<str:room_name>/<str:username>/', MessageView, name='room')
]