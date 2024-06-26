from django.urls import path
from . import views

app_name = "app_clubs"

urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
    path('create-club/', views.CreateClub.as_view(), name='create_club'),
    path('<slug:cat>/list-clubs/', views.ListClubs.as_view(), name='list_clubs'),

    path('profile-user/', views.ProfileUser.as_view(), name='profile_user'),
    path('<slug:club_slug>/profile-user/<int:pk>/', views.ProfileUserClub.as_view(), name='profile_user_club'),

    path('page-error/<slug:type_error>/', views.PageError.as_view(), name='page_error'),
    path('<slug:club_slug>/delete-post/<slug:post_slug>', views.DeletePost.as_view(), name='delete_post'),
    path('<slug:club_slug>/edit-post/<slug:post_slug>', views.UpdatePost.as_view(), name='edit_post'),
    path('<slug:club_slug>/edit-club/', views.UpdateClubProfile.as_view(), name='edit_club_profile'),
    path('<slug:club_slug>/join-club/', views.JoinClub.as_view(), name='join_club'),
    path('<slug:club_slug>/create-post/', views.CreatePost.as_view(), name='create_post'),
    path('<slug:club_slug>/create-event/', views.CreateEvent.as_view(), name='create_event'),
    path('<slug:club_slug>/approve-members/', views.ApproveMembers.as_view(), name='approve_members'),
    path('<slug:club_slug>/profile-club/', views.ProfileClub.as_view(), name='profile_club'),
    path('<slug:club_slug>/show-content/<slug:content>/', views.ShowContent.as_view(), name='show_content'),
    path('<slug:club_slug>/detail-post/<slug:post_slug>/', views.DetailPost.as_view(), name='detail_post'),
    path('<slug:club_slug>/send-msg/<int:pk>/', views.SendMsg.as_view(), name='send_msg'),
    path('my-notifs/', views.MyNotifs.as_view(), name='my_notifs'),
    path('<slug:club_slug>/delete-notifs/<int:pk>', views.DeleteNotifs.as_view(), name='delete_notifs'),

    path('<slug:club_slug>/detail-event/<int:pk>/', views.DetailEvent.as_view(), name='detail_event'),
]
