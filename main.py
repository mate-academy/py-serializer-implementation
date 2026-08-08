import json
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return json.dumps(serializer.data, separators=(",", ":")).encode("utf-8")


def deserialize_car_object(json_data_bytes: bytes) -> Car:
    data = json.loads(json_data_bytes)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    car_instance = serializer.save()
    return car_instance


if __name__ == "__main__":
    import os
    import django

    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "car_service.settings")
    django.setup()
