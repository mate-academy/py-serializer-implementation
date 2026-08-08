from rest_framework.renderers import JSONRenderer
from car.models import Car
from car.serializers import CarSerializer
import json


def serialize_car_object(car: Car):
    serializer = CarSerializer(instance=car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(data):
    serializer = CarSerializer(data=json.loads(data))
    if serializer.is_valid():
        return serializer.save()
    print("Deserialization failed:", serializer.errors)
    return None
