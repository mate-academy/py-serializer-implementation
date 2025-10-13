import json
from typing import Any, Dict, Union

# Tenta usar o helper da Mate; se não existir localmente, faz o fallback
try:
    import init_django_orm  # type: ignore  # noqa: F401,E402
except ModuleNotFoundError:  # Execução local
    import os  # noqa: E402
    import django  # noqa: E402

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "car_service.settings")
    django.setup()

from car.models import Car  # noqa: E402
from car.serializers import CarSerializer  # noqa: E402


def serialize_car_object(car: Car) -> str:
    data = CarSerializer(car).data
    return json.dumps(data)


def deserialize_car_object(payload: Union[str, Dict[str, Any]]) -> Car:
    data: Dict[str, Any]
    if isinstance(payload, str):
        data = json.loads(payload)
    else:
        data = payload

    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
