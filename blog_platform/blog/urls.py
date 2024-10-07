from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', post_list, name='post_list'), 
   path('create/', post_form, name='post_form'),
    path('<int:pk>/', post_detail, name='post_detail'), 
]
