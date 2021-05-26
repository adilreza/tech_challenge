from django.urls import path, include

app_name = "api"

urlpatterns = [
    path("v1/", include("src.api.v1.urls")),
]
