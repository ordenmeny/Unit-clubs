from django.urls import path
from . import views

app_name = "app_clubs"

urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
    path('create-club/', views.CreateClub.as_view(), name='create_club'),
    path('join-club/<slug:club_slug>/', views.JoinClub.as_view(), name='join_club'),
    path('list-clubs/', views.ListClubs.as_view(), name='list_clubs'),
    path('create-post/<slug:club_slug>/', views.CreatePost.as_view(), name='create_post'),
    path('create-event/<slug:club_slug>/', views.CreateEvent.as_view(), name='create_event'),
    # path('dash<slug:club_slug>', views.)
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
