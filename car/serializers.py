from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    manufacturer = serializers.CharField(max_length=64, required=True)
    model = serializers.CharField(max_length=64, required=True)
    horse_powers = serializers.IntegerField(
        min_value=1,
        max_value=1914,
        required=True
    )
    is_broken = serializers.BooleanField(required=True)
    problem_description = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True
    )

    def create(self, validated_data):
        return Car(**validated_data)
