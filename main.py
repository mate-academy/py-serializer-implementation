import json

from rest_framework.renderers import JSONRenderer

from car.serializers import CarSerializer


def serialize_car_object(car):
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(car_json):
    car_data = json.loads(car_json)
    serializer = CarSerializer(data=car_data)
    if serializer.is_valid():
        return serializer.save()
