from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(min_value=1, max_value=1914)
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(
        allow_blank=True,
        allow_null=True,
        required=False,
    )

    def create(self, validated_data: dict) -> Car:
        return Car(**validated_data)

    def update(self, instance: Car, validated_data: dict) -> Car:
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance
