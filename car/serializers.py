from rest_framework import serializers
from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=False, required=False)
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(
        # adjust min/max to match your model's validators
        min_value=1,
        max_value=1500
    )
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(
        allow_null=True, required=False, default=None
    )

    def create(self, validated_data: dict) -> Car:
        return Car.objects.create(**validated_data)
