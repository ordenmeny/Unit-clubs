from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.LoginUser.as_view(), name="login"),
    path("signup/", views.SignUp.as_view(), name='signup'),
]