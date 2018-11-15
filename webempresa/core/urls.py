from django.urls import path
from . import views

urlpatterns = [
    # Path del core
    path('', views.home, name="home"),
    path('about-us/', views.about, name="about"),
    path('store/', views.store, name="store")
]