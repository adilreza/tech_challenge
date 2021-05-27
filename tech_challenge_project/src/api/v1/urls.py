from django.urls import include, path
from rest_framework.routers import DefaultRouter

from src.tech_challenge_app.views import RecordViewSet
from src.tech_challenge_app.views import NoticeSerializer
from src.tech_challenge_app.views import MatchViewSet


router = DefaultRouter()

router.register("record", RecordViewSet)
router.register("notice", NoticeSerializer)
router.register("match", MatchViewSet)


urlpatterns = [
    path("", include(router.urls))
]
