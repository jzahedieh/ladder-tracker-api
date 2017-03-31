from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from ladder import views

router = DefaultRouter()
router.register(r'season', views.SeasonViewSet)
router.register(r'player', views.PlayerViewSet)
router.register(r'ladder', views.LadderViewSet)
router.register(r'league', views.LeagueViewSet)
router.register(r'result', views.ResultViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
