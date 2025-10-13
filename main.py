import json
from typing import Any, Dict, Union

# Tenta helper da Mate; se não houver, faz fallback local
try:
    import init_django_orm  # type: ignore  # noqa: F401,E402
except ModuleNotFoundError:
    import os  # noqa: E402
    import django  # noqa: E402
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "car_service.settings")
    django.setup()

from car.models import Car  # noqa: E402
from car.serializer import CarSerializer  # <-- singular  # noqa: E402


def serialize_car_object(car: Car) -> Dict[str, Any]:
    """
    Retorna um dict com as chaves exatas esperadas pelo teste:
    {"id","manufacturer","model","horse_powers","is_broken","problem_description"}
    """
    # DRF já devolve OrderedDict, mas converter para dict ajuda a evitar ruído de tipo
    return dict(CarSerializer(car).data)


def _to_dict(payload: Union[bytes, str, Dict[str, Any]]) -> Dict[str, Any]:
    """
    Converte bytes/str (JSON) ou dict em um dict válido para o serializer.
    """
    if isinstance(payload, dict):
        return payload
    if isinstance(payload, bytes):
        return json.loads(payload.decode())
    return json.loads(payload)


def deserialize_car_object(payload: Union[bytes, str, Dict[str, Any]]) -> Car:
    """
    Aceita bytes (JSON), str (JSON) ou dict; devolve uma instância Car.
    """
    data = _to_dict(payload)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
