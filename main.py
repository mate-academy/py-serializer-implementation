from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
import io

from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json = JSONRenderer().render(serializer.data)
    return json


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    return Car(
        id=data.get("id"),
        manufacturer=data.get("manufacturer"),
        model=data.get("model"),
        horse_powers=data.get("horse_powers"),
        is_broken=data.get("is_broken"),
        problem_description=data.get("problem_description")
    )
