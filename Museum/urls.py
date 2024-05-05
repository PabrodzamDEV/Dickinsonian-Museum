from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('poems/', views.PoemListView.as_view(), name="poems"),
    path('poems/new/', views.PoemCreateView.as_view(), name='museum-poem-create'),
    path('gallery/', views.gallery, name="gallery"),
    path('essays/', views.essays, name="essays"),
    path('contact/', views.contact, name="contact"),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls'), name="members"),
]
