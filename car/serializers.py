from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.Serializer):

    MIN_HORSE_POWERS = 1
    MAX_HORSE_POWERS = 1914

    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(max_length=64, required=True)
    model = serializers.CharField(max_length=64, required=True)
    horse_powers = serializers.IntegerField(
        validators=[
            MinValueValidator(MIN_HORSE_POWERS),
            MaxValueValidator(MAX_HORSE_POWERS)
        ],
        required=True
    )
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(
        max_length=255,
        allow_null=True,
        required=False
    )

    def create(self, validated_data: dict) -> Car:
        return Car.objects.create(**validated_data)

    def update(self, instance: Car, validated_data: dict) -> Car:
        instance.manufacturer = validated_data.get(
            "manufacturer",
            instance.manufacturer
        )
        instance.model = validated_data.get("model", instance.model)
        instance.horse_powers = validated_data.get(
            "horse_powers",
            instance.horse_powers
        )
        instance.is_broken = validated_data.get(
            "is_broken",
            instance.is_broken
        )
        instance.problem_description = validated_data.get(
            "problem_description",
            instance.problem_description
        )
        return instance
