from django.urls import path
from . import views

app_name = "app_clubs"

urlpatterns = [
    path('create-club/', views.CreateClub.as_view(), name='create_club'),
    path('join-club/<slug:club_slug>/', views.JoinClub.as_view(), name='join_club'),
    path('list-clubs/', views.ListClubs.as_view(), name='list_clubs'),
    path('create-post/', views.CreatePost.as_view(), name='create_post')

    # club-dashboard:
    # Здесь пользователи видят новости, ститьи.
    # path('club-dashboard/<slug:club_slug>/', ..., name='club-dashboard'),

    # club-dashboard-admin:
    # Место для админов клуба. Добавление статей и т.д
    # Здесь происходит создание нового объекта в БД(создается проект, который связан с клубом)

    # project-dashboard:
    # Видны задачи проекта и т.д.
    # !! Возможно сделать отдельным приложением!
]
