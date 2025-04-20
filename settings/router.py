from django.urls import path, include

urlpatterns = [
    path("", include("apps.hotels.urls")),
    path("", include("apps.users.urls")),
]
