# Import the path and include functions from django.urls module.
# These functions are used for URL routing.
from django.urls import path, include

# Import the routers module from rest_framework.
# This module is used to automatically create the URL conf.
from rest_framework import routers

# Import the views from the current directory.
# These views are used to handle the requests.
from . import views

# Import views from drf_spectacular.
# These views are used to generate the API documentation.
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

# Create a default router object.
# The DefaultRouter class is a feature-rich router for a set of views.
router = routers.DefaultRouter()

# Register the viewsets with the router.
# This will create routes for model related operations (list, create, retrieve, update, destroy)
router.register(r'users', views.UserViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'poems', views.PoemViewSet)
router.register(r'gallerypieces', views.GalleryPieceViewSet)
router.register(r'essays', views.EssayViewSet)

# The include function is used to include the router's URLs.
# The path function is used to route the URL pattern to the viewset.
urlpatterns = [
    path('', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),  # Returns a .yaml file
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # UI to consume
    # the API through a browser
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),  # Documentation
]
