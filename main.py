from rest_framework.renderers import JSONRenderer
from rest_framework.utils import json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)

    json_data = JSONRenderer().render(serializer.data)

    return json_data


def deserialize_car_object(jsons: bytes) -> Car:
    data_dict = json.loads(jsons)

    serializer = CarSerializer(data=data_dict)

    if serializer.is_valid():
        car_instance = serializer.save()
        return car_instance
    else:
        raise ValueError("Invalid input data for deserialization")
