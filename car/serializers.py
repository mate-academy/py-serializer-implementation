from typing import Any, Dict

from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers

from car.models import Car  # ajuste o caminho se o app tiver outro nome


class CarSerializer(serializers.Serializer):
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(2000)]
    )
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(
        allow_null=True,
        allow_blank=True,
        required=False,
    )

    def create(self, validated_data: Dict[str, Any]) -> Car:
        # create() é necessário porque estamos usando serializers.Serializer
        return Car.objects.create(**validated_data)

    def update(self, instance: Car, validated_data: Dict[str, Any]) -> Car:
        # Não é usado pelos testes, mas deixa o serializer completo
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
