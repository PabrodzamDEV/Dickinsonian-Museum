from django.urls import path
from . import views

app_name = "my_members"

urlpatterns = [
    path('', views.login_member, name="login"),
    path('login_user/', views.login_member, name="login"),
    path('logout_user/', views.logout_member, name="logout"),
    path('update_profile/', views.update_profile, name="update_profile"),
    path('register/', views.register_member, name="register"),
    path('my_profile/', views.my_profile, name="my_profile"),

]
