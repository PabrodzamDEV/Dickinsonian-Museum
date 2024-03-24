from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('poems/', views.poems, name="poems"),
    path('novels/', views.gallery, name="gallery"),
    path('essays/', views.essays, name="essays"),
    path('contact/', views.contact, name="contact"),
]