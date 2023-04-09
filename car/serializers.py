from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(max_value=1914, min_value=1)
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(required=False)

    def create(self, validated_data: dict) -> Car:
        return Car.objects.create(**validated_data)

    def update(
            self,
            instance: Car,
            validated_data: dict
    ) -> Car:
        instance.manufacturer = validated_data.get(
            "manufacturer",
            instance.manufacturer
        )
        instance.model = validated_data.get(
            "model",
            instance.model
        )
        instance.horse_power = validated_data.get(
            "horse_power",
            instance.horse_power
        )
        instance.is_broken = validated_data.get(
            "is_broken",
            instance.is_broken
        )
        instance.problem_description = validated_data.get(
            "problem_description",
            instance.problem_description
        )
        instance.save()
        return instance
