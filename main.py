from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    return CarSerializer(car).data


def deserialize_car_object(json: bytes) -> Car:
    return CarSerializer(json).data
