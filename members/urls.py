from django.urls import path
from . import views as my_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', my_views.login_member, name="login"),
    path('login_user/', my_views.login_member, name="login"),
    path('logout_user/', my_views.logout_member, name="logout"),
    path('update_profile/', my_views.update_profile, name="update_profile"),
    path('password_change/', auth_views.PasswordChangeView.as_view()),
    # path('password')

]
