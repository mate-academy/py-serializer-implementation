import json
from car.serializers import CarSerializer
from car.models import Car


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json_string = json.dumps(serializer.data, separators=(",", ":"))
    return json_string.encode("utf-8")


def deserialize_car_object(json_data: bytes) -> Car:
    json_string = json_data.decode("utf-8")
    data = json.loads(json_string)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
