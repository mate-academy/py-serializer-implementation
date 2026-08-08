from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(
        min_value=1,
        max_value=1914
    )
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(required=False)

    def __str__(self):
        return f"{self.manufacturer}, {self.model}"

    @staticmethod
    def serialize_car_object(car: Car):
        serializer = CarSerializer(car)
        json_car = JSONRenderer().render(serializer.data)

        return json_car

    @staticmethod
    def deserialize_car_object(json_car):
        stream = io.BytesIO(json_car)
        data = JSONParser().parse(stream)
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        car_instance = serializer.save()

        return car_instance
