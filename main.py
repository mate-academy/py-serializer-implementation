import json
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return json.dumps(serializer.data, separators=(",", ":")).encode("utf-8")


def deserialize_car_object(json_bytes: bytes) -> Car:
    data = json.loads(json_bytes.decode("utf-8"))

    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    validated = serializer.validated_data

    car = Car(**validated)

    if "id" in data:
        car.id = data["id"]

    return car
