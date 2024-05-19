# Import the viewsets module from rest_framework.
# This module provides a set of generic viewset classes.
from rest_framework import viewsets

# Import the UserSerializer and ProfileSerializer from the current directory.
# These serializers convert complex data types, such as querysets and model instances, to native Python datatypes.
from .serializer import UserSerializer, ProfileSerializer, PoemSerializer, GalleryPieceSerializer, EssaySerializer

# Import the models from the different apps.
from members.models import User, Profile
from Museum.models import Poem, GalleryPiece, Essay


# Define a viewset for the  models.
# The ModelViewSet class is a type of viewset that provides complete CRUD operations.
class UserViewSet(viewsets.ModelViewSet):
    # Define the queryset for this viewset.
    # The queryset determines which records are displayed.
    queryset = User.objects.all()

    # Specify the serializer class for this viewset.
    # The serializer class determines how the data is transformed to and from the HTTP request/response.
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class PoemViewSet(viewsets.ModelViewSet):
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer


class GalleryPieceViewSet(viewsets.ModelViewSet):
    queryset = GalleryPiece.objects.all()
    serializer_class = GalleryPieceSerializer


class EssayViewSet(viewsets.ModelViewSet):
    queryset = Essay.objects.all()
    serializer_class = EssaySerializer
