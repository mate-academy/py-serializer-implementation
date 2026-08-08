from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(required=True, max_length=64)
    model = serializers.CharField(required=True, max_length=64)
    horse_powers = serializers.IntegerField(
        required=True,
        max_value=1914,
        min_value=1
    )
    is_broken = serializers.BooleanField(required=True)
    problem_description = serializers.CharField(required=False)

    def create(self, validated_data):
        return Car.objects.create(**validated_data)
