import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car_service.settings')

import django

django.setup()

from car.models import Car
from car.serializers import CarSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser


def serialize_car_object(car_object: Car) -> bytes:
    serializer = CarSerializer(car_object)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.validated_data


if __name__ == "__main__":
    car = Car.objects.create(
        manufacturer="Tesla",
        model="X",
        horse_powers=800,
        is_broken=False,
        problem_description="NO PROBLEMS"
    )
    print(car)

    serialized_car = serialize_car_object(car)
    print(serialized_car)

    deserialized_car = deserialize_car_object(serialized_car)
    print(deserialized_car)
