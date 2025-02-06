from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # This makes "/" return something
    path('faith/', views.faith, name='faith'),
    path('hope/', views.hope, name='hope'),
    path('love/', views.love, name='love'),
    path('purpose/', views.purpose, name='purpose'),
    path('truthtalknature/', views.truthtalknature, name='truthtalknature'),
]

