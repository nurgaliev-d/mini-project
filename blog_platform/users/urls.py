from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('list/', views.user_list, name='user_list'),
    path('register/', views.register, name='register'),
     path('profile/<int:user_id>/', views.user_profile, name='profile'),
    path('profile/<str:username>/edit/', views.edit_profile, name='edit_profile'),
    path('follow/<str:username>/', views.follow_user, name='follow_user'),
    path('unfollow/<str:username>/', views.unfollow_user, name='unfollow_user'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
