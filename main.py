import init_django_orm  # noqa: F401
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json = JSONRenderer().render(serializer.data)
    return json


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    serializer.is_valid()
    return serializer.save()


if __name__ == "__main__":
    car = Car.objects.create(
        manufacturer="Audi",
        model="A8",
        horse_powers="250",
        is_broken=False,
        problem_description="All is good"
    )
    json_data = serialize_car_object(car)

    print(deserialize_car_object(json_data))
