from typing import Any, Dict

from rest_framework import serializers

from car.models import Car  # ajuste o caminho se o app tiver outro nome


class CarSerializer(serializers.Serializer):
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(min_value=1)
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(
        allow_null=True,
        allow_blank=True,
        required=False,
    )

    def validate_horse_powers(self, value: int) -> int:
        # Job log: 2000 deve ser inválido
        if value >= 2000:
            raise serializers.ValidationError("Horse powers too high")
        return value

    def create(self, validated_data: Dict[str, Any]) -> Car:
        return Car.objects.create(**validated_data)

    def update(self, instance: Car, validated_data: Dict[str, Any]) -> Car:
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
