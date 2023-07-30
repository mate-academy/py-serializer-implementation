from rest_framework import routers
from django.urls import path, include

from car.views import CarViewSet

router = routers.DefaultRouter()

router.register("cars", CarViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "car"
