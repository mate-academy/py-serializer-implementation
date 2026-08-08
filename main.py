import json
from typing import Any, Dict, Union

# Tenta o helper da Mate; se não existir localmente, faz fallback
try:
    import init_django_orm  # type: ignore  # noqa: F401,E402
except ModuleNotFoundError:
    import os  # noqa: E402
    import django  # noqa: E402
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "car_service.settings")
    django.setup()

from car.models import Car  # noqa: E402
from car.serializer import CarSerializer  # noqa: E402


def serialize_car_object(car: Car) -> bytes:
    """
    JSON compacto em bytes (UTF-8) na ordem exata:
    id, manufacturer, model, horse_powers, is_broken, problem_description.
    """
    data = {
        "id": car.id,
        "manufacturer": car.manufacturer,
        "model": car.model,
        "horse_powers": car.horse_powers,
        "is_broken": car.is_broken,
        "problem_description": car.problem_description,
    }
    return json.dumps(data, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _to_dict(payload: Union[bytes, str, Dict[str, Any]]) -> Dict[str, Any]:
    """Converte bytes/str JSON ou dict em dict para o serializer."""
    if isinstance(payload, dict):
        return payload
    if isinstance(payload, bytes):
        return json.loads(payload.decode())
    return json.loads(payload)


def deserialize_car_object(payload: Union[bytes, str, Dict[str, Any]]) -> Car:
    """Aceita bytes/str/dict e cria uma instância Car via DRF serializer."""
    data = _to_dict(payload)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
