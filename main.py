import io
from rest_framework.parsers import JSONParser

from car.models import Car
from car.serializers import CarSerializer
from rest_framework.renderers import JSONRenderer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json_data = JSONRenderer().render(serializer.data)
    return json_data


def deserialize_car_object(json_bytes: bytes) -> Car:
    json_bytes = io.BytesIO(json_bytes)
    data = JSONParser().parse(json_bytes)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()


if __name__ == "__main__":

    car = Car.objects.create(
        manufacturer="Honda",
        model="Civic",
        horse_powers=174,
        is_broken=False,
        problem_description="",
    )
    serialized_car = serialize_car_object(car)
    print(serialized_car)

    deserialized_car = deserialize_car_object(serialized_car)
    print(deserialized_car.manufacturer, deserialized_car.model, deserialized_car.horse_powers)
