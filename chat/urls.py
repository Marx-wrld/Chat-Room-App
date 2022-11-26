from django.urls import path
from . import views

#when a user wants to go to the home directory, he hould go to the views.home 
#so it will take him to the views.py file and will look for a function named home.
#so whatever we are doing to this function is what will happen our url 
urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]