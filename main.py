import json

from car.models import Car


def serialize_car_object(car: Car) -> bytes:
    data = {
        "id": car.id,
        "manufacturer": car.manufacturer,
        "model": car.model,
        "horse_powers": car.horse_powers,
        "is_broken": car.is_broken,
        "problem_description": car.problem_description,
    }
    return json.dumps(
        data,
        separators=(",", ":"),
    ).encode("utf-8")


def deserialize_car_object(car_bytes: bytes) -> Car:
    json_str = car_bytes.decode("utf-8")
    data = json.loads(json_str)

    car = Car(
        manufacturer=data["manufacturer"],
        model=data["model"],
        horse_powers=data["horse_powers"],
        is_broken=data["is_broken"],
        problem_description=data["problem_description"],
    )
    car.id = data["id"]
    return car
