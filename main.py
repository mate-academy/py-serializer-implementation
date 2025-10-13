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


def serialize_car_object(car: Car) -> Dict[str, Any]:
    """
    Retorna um DICT com os campos esperados pelos testes.
    (Se os testes exigirem string JSON, troque o retorno por json.dumps(...).)
    """
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
