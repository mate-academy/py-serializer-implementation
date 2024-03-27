from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    if serializer.is_valid():
        return serializer.data


def deserialize_car_object(json: bytes) -> Car:
    serializer = CarSerializer(data=bytes)
    return Car.objects.create(**serializer.data)
