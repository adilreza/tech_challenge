from django.urls import include, path
from rest_framework.routers import DefaultRouter

from src.tech_challenge_app.views import RecordViewSet
from src.tech_challenge_app.views import NoticeSerializer
from src.tech_challenge_app.views import MatchViewSet


router = DefaultRouter()

#router.register("records", RecordViewSet)
router.register("notices", NoticeSerializer)
router.register("matches", MatchViewSet)


urlpatterns = [
    path("", include(router.urls))
]
