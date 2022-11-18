from django.urls import path

from .views import (
    TodoPlayersApiView,
)

urlpatterns = [
    path('', TodoPlayersApiView.as_view()),
]