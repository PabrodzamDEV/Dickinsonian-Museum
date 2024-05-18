from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('poems/', views.PoemListView.as_view(), name="poems"),
    path('poems/new/', views.PoemCreateView.as_view(), name='museum-poem-create'),
    path('poems/<int:pk>/update/', views.PoemUpdateView.as_view(), name='museum-poem-update'),
    path('poems/<int:pk>/delete/', views.PoemDeleteView.as_view(), name='museum-poem-delete'),
    path('gallery/', views.GalleryPieceListView.as_view(), name="gallery"),
    path('gallery/new/', views.GalleryPieceCreateView.as_view(), name="museum-gallerypiece-create"),
    path('gallery/<int:pk>/update/', views.GalleryPieceUpdateView.as_view(), name="museum-gallerypiece-update"),
    path('gallery/<int:pk>/delete/', views.GalleryPieceDeleteView.as_view(), name="museum-gallerypiece-delete"),
    # path('essays/', views.essays, name="essays"),
    path('contact/', views.contact, name="contact"),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls'), name="members"),
]
