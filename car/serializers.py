from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(
        max_length=64,
    )
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(
        validators=[
            MaxValueValidator(
                limit_value=1914,
                message="Horse powers must be less than '1914'",
            ),
            MinValueValidator(
                limit_value=1,
                message="Horse powers must be more than '1'",
            )
        ]
    )
    is_broken = serializers.BooleanField(required=True)
    problem_description = serializers.CharField(
        allow_null=True,
        required=False
    )

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.manufacturer = validated_data.get(
            "manufacturer",
            instance.manufacturer
        )
        instance.model = validated_data.get(
            "model", instance.model
        )
        instance.horse_powers = validated_data.get(
            "horse_powers",
            instance.horse_powers
        )
        isinstance.is_broken = validated_data.get(
            "is_broken", validated_data.is_broken
        )
        instance.problem_description = validated_data.get(
            "problem_description",
            instance.problem_description
        )
        instance.save()
        return instance
