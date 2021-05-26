from django.urls import include, path
from rest_framework.routers import DefaultRouter


from src.tech_challenge_app.rest_api import HelloViewSet

router = DefaultRouter()

router.register("hello", HelloViewSet)

urlpatterns = [
    path("", include(router.urls))
]
