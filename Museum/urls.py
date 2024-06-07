from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # Class-based views for Poems
    path("poems/", views.PoemListView.as_view(), name="poems"),
    path("poems/<int:pk>/", views.PoemDetailView.as_view(), name="museum-poem-detail"),
    path("poems/new/", views.PoemCreateView.as_view(), name="museum-poem-create"),
    path('poems/<str:category>/', views.PoemCategoryListView.as_view(), name='poems_by_category'),
    path(
        "poems/<int:pk>/update/",
        views.PoemUpdateView.as_view(),
        name="museum-poem-update",
    ),
    path(
        "poems/<int:pk>/delete/",
        views.PoemDeleteView.as_view(),
        name="museum-poem-delete",
    ),
    # Class-based views for the gallery
    path("gallery/", views.GalleryPieceListView.as_view(), name="gallery"),
    path(
        "gallery/new/",
        views.GalleryPieceCreateView.as_view(),
        name="museum-gallerypiece-create",
    ),
    path('gallery/<str:category>/', views.GalleryPieceCategoryListView.as_view(), name='gallerypieces_by_category'),
    path(
        "gallery/<int:pk>/update/",
        views.GalleryPieceUpdateView.as_view(),
        name="museum-gallerypiece-update",
    ),
    path(
        "gallery/<int:pk>/delete/",
        views.GalleryPieceDeleteView.as_view(),
        name="museum-gallerypiece-delete",
    ),
    # Class-based views for essays
    path("essays/", views.EssayListView.as_view(), name="essays"),
    path("essays/new/", views.EssayCreateView.as_view(), name="museum-essay-create"),
    path('essays/<str:category>/', views.EssayCategoryListView.as_view(), name='essays_by_category'),
    path(
        "essays/<int:pk>/update/",
        views.EssayUpdateView.as_view(),
        name="museum-essay-update",
    ),
    path(
        "essays/<int:pk>/delete/",
        views.EssayDeleteView.as_view(),
        name="museum-essay-delete",
    ),
    path("contact/", views.contact, name="contact"),
    path("members/", include("django.contrib.auth.urls")),
    path("members/", include("members.urls"), name="members"),
]
