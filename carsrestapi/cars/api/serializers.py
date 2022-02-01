from rest_framework import serializers
from cars.models import Car, Rating
from cars.api.check_if_car_exist import check_if_car_exist


class CarSerializer(serializers.ModelSerializer):

    avg_rating = serializers.SerializerMethodField(read_only=True)

    def get_avg_rating(self, obj):
        if obj.avg_rating != None:
            return round(obj.avg_rating, 1)
        return obj.avg_rating

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'avg_rating']

    def validate(self, data):
        if check_if_car_exist(data['make'], data['model']) == True:
            return data
        else:
            raise serializers.ValidationError("Car does not exist in the API database.")


class PopularCarSerializer(serializers.ModelSerializer):

    rates_number = serializers.IntegerField(read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'rates_number']

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ['car_id', 'rate']
