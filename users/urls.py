from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.LoginUser.as_view(), name="login"),
    path("signup/", views.SignUp.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit-profile/<int:pk>/', views.UpdateProfile.as_view(), name='edit_profile'),
]