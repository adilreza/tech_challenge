from django.urls import include, path
from rest_framework.routers import DefaultRouter

from src.tech_challenge_app.rest_api import RecordViewSet
from src.tech_challenge_app.rest_api import NoticeSerializer
from src.tech_challenge_app.rest_api import MatchViewSet


router = DefaultRouter()

router.register("record", RecordViewSet)
router.register("notice", NoticeSerializer)
router.register("match", MatchViewSet)


urlpatterns = [
    path("", include(router.urls))
]
