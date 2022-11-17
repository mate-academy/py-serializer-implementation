from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField()
    model = serializers.CharField()
    horse_powers = serializers.IntegerField()
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField()

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get(
            "manufacturer", instance.title
        )
        instance.description = validated_data.get(
            "model", instance.description
        )
        instance.duration = validated_data.get(
            "horse_powers", instance.duration
        )
        instance.duration = validated_data.get(
            "is_broken", instance.duration
        )
        instance.duration = validated_data.get(
            "problem_description", instance.duration
        )
        instance.save()
        return instance
