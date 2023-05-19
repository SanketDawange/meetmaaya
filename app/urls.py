from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('dashboard', views.dashboard, name='dashboard'),
    
    path('meeting', views.videocall, name='videocall'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('join_room', views.join_room, name='join_room'),
]
