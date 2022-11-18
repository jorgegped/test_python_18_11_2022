from django.contrib import admin
from django.urls import path, include

from Players import views
from Teams import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('players', include('Players.urls')),
    path('teams', include('Teams.urls')),
]
