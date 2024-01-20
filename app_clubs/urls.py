from django.urls import path
from . import views

app_name = "app_clubs"

urlpatterns = [
    path('create-club/', views.CreateClub.as_view(), name='create_club'),
    path('join-club/<slug:club_slug>/', views.JoinClub.as_view(), name='join_club'),
    path('list-clubs/', views.ListClubs.as_view(), name='list_clubs'),

]
