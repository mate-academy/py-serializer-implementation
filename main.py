from json import dumps, loads

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json_data = dumps(serializer.data, separators=(",", ":"))
    return json_data.encode("utf-8")


def deserialize_car_object(json: bytes) -> Car:
    json_str = json.decode("utf-8")
    data = loads(json_str)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        return serializer.save()
    else:
        raise ValueError("Invalid data for Car serialization")
