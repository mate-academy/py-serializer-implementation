import json

from car.serializers import CarSerializer


def serialize_car_object(car):
    serializer = CarSerializer(car)
    return json.dumps(
        serializer.data,
        separators=(",", ":")
    ).encode("utf-8")


def deserialize_car_object(json_data):
    data = json.loads(json_data)

    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    return serializer.save()
