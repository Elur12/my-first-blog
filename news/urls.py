from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('newbox/', views.newbox, name='newbox'),
    path('news/', views.news, name='news'),
    path('newzakaz/', views.newzakaz, name='newzakaz'),
]