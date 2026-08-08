import os
import django
from typing import TYPE_CHECKING


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "car_service.settings")

django.setup()

if TYPE_CHECKING:
    from car.models import Car


def serialize_car_object(car: "Car") -> bytes:
    from rest_framework.renderers import JSONRenderer
    from car.serializers import CarSerializer
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json: bytes) -> "Car":
    from rest_framework.parsers import JSONParser
    from car.serializers import CarSerializer
    import io
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    car = serializer.save()
    return car
