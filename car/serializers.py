from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField()
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(required=False)

    def validate(self, attrs):
        min_hp = 1
        max_hp = 1914
        if attrs.get("horse_powers") < 1:
            raise serializers.ValidationError(
                f"Horse powers can not be less than {min_hp}"
            )
        if attrs.get("horse_powers") > 1914:
            raise serializers.ValidationError(
                f"Horse powers can not be higher than {max_hp}"
            )
        return super().validate(attrs)

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.manufacturer = validated_data.get(
            "manufacturer", instance.manufacturer
        )
        instance.model = validated_data.get(
            "model", instance.model
        )
        instance.horse_powers = validated_data.get(
            "horse_powers", instance.horse_powers
        )
        instance.is_broken = validated_data.get(
            "is_broken", instance.is_broken
        )
        instance.problem_description = validated_data.get(
            "problem_description", instance.problem_description
        )
        instance.save()
        return instance
