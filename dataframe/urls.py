from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.add_animation, name='add_animation'),
]
