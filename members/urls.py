from django.urls import path, include
from . import views

urlpatterns = [
    path('login_user/', views.login_member, name="login"),
    path('logout_user/', views.logout_member, name="logout"),
    path('create_profile/', views.create_profile, name="create_profile"),
]