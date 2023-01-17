from rest_framework import serializers
from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(max_length=64, required=False)
    model = serializers.CharField(max_length=64, required=False)
    horse_powers = serializers.IntegerField(
        required=True, min_value=5, max_value=300)
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(
        allow_null=True, required=False)

    def create(self, validated_data):
        return Car.objects.create(**validated_data)
