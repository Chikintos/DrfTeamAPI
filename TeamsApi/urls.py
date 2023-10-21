
from django.urls import path,include
from rest_framework import routers
from .views import TeamViewSet,PlayerViewSet

router = routers.DefaultRouter()
router.register("team",viewset = TeamViewSet)
router.register("player",viewset = PlayerViewSet)

urlpatterns = [
    path("",include(router.urls))   
]
