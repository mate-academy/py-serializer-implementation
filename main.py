import json
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car):
    serializer = CarSerializer(car)
    data = serializer.data
    if hasattr(car, "id"):
        data["id"] = car.id
    return json.dumps(data, separators=(",", ":")).encode("utf-8")


def deserialize_car_object(json_data):
    data = json.loads(json_data.decode("utf-8"))
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        return Car(**serializer.validated_data)
    else:
        raise ValueError("Invalid data for Car object")
