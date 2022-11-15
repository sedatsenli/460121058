from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("index", views.index),
    path("contact", views.contact),
    path("menu", views.menu),
    path("today-special", views.today_special),

]
