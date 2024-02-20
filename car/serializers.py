from django.core.validators import (
    MaxLengthValidator,
    MinValueValidator,
    MaxValueValidator,
)
from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(validators=[MaxLengthValidator(64)])
    model = serializers.CharField(validators=[MaxLengthValidator(64)])
    horsepower = serializers.FloatField(
        validators=[MaxValueValidator(1000), MinValueValidator(0)]
    )
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(required=False)

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.manufacturer = validated_data.get(
            "manufacturer", instance.manufacturer
        )
        instance.model = validated_data.get("model", instance.model)
        instance.horsepower = validated_data.get(
            "horsepower", instance.horsepower)
        instance.is_broken = validated_data.get(
            "is_broken", instance.is_broken)
        instance.problem_description = validated_data.get(
            "problem_description", instance
        )

        instance.save()
        return instance
