from django.urls import path
from . import views

app_name = "app_clubs"

urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
    path('create-club/', views.CreateClub.as_view(), name='create_club'),
    path('<slug:club_slug>/join-club/', views.JoinClub.as_view(), name='join_club'),
    path('<slug:cat>/list-clubs/', views.ListClubs.as_view(), name='list_clubs'),

    # URLs for clubs
    path('<slug:club_slug>/create-post/', views.CreatePost.as_view(), name='create_post'),
    path('<slug:club_slug>/create-event/', views.CreateEvent.as_view(), name='create_event'),
    path('<slug:club_slug>/approve-members/', views.ApproveMembers.as_view(), name='approve_members'),
    path('<slug:club_slug>/profile-club/', views.ProfileClub.as_view(), name='profile_club'),

    path('profile-user/', views.ProfileUser.as_view(), name='profile_user'),
]

# club-dashboard:
# Здесь пользователи видят новости, ститьи.
# path('club-dashboard/<slug:club_slug>/', ..., name='club-dashboard'),

# club-dashboard-admin:
# Место для админов клуба. Добавление статей и т.д


# 0) Все активности только для авторизованных пользователей.
# 1) добавление статей и ивентов только для админов конкретного клуба.
# 2) Просмотр статей, ивентов только для членов клуба

# Отвельные модели для пользователей и клубов.
# У одного пользователя может быть несколько клубов. Связь ManyToMany

# В каждом клубе будут админы:
# при создании клуба добавляется в поле admin пользователь, который создал клуб
# При выполнении каких-то view будет проверка, является ли человек админом.

# ---