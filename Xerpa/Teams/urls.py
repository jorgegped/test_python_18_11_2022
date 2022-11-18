from django.urls import path

from .views import (
    TodoTeamsApiView,
)

urlpatterns = [
    path('', TodoTeamsApiView.as_view()),
]