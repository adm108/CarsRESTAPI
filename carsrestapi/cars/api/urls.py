from django.urls import include, path
from rest_framework.routers import DefaultRouter

from cars.api import views as qv

router = DefaultRouter()
router.register(r"popular", qv.PopularCarViewSet, basename='popular')
router.register(r"cars", qv.CarViewSet, basename='cars')
router.register(r"rate", qv.RatingViewSet, basename='rate')

urlpatterns = [
    path('', include(router.urls)),
]