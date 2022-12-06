from django.urls import path

from .views import (
    DanceClassCreateListAPIView,
)


urlpatterns = [
    path("api", DanceClassCreateListAPIView.as_view(), name="dance-class-api"),
]
