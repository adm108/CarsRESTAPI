from rest_framework import viewsets
from cars.api.serializers import CarSerializer, PopularCarSerializer, RatingSerializer
from cars.models import Car, Rating
from django.db.models import Count


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    lookup_field = "id"
    serializer_class = CarSerializer

class PopularCarViewSet(viewsets.ModelViewSet):

    queryset = Car.objects.annotate(rates_number=Count('ratings')).order_by('-rates_number')
    lookup_field = "id"
    serializer_class = PopularCarSerializer

class RatingViewSet(viewsets.ModelViewSet):

    queryset = Rating.objects.all()
    lookup_field = "car_id"
    serializer_class = RatingSerializer
