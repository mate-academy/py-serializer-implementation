import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(max_length=255)
    model = serializers.CharField(max_length=255)

    horse_powers = serializers.IntegerField(min_value=1, max_value=1900)
    is_broken = serializers.BooleanField(required=False, default=False)

    problem_description = serializers.CharField(
        allow_null=True,
        allow_blank=True,
        required=False
    )

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.manufacturer = validated_data.get("manufacturer", instance.manufacturer)
        instance.model = validated_data.get("model", instance.model)
        instance.horse_powers = validated_data.get("horse_powers", instance.horse_powers)
        instance.is_broken = validated_data.get("is_broken", instance.is_broken)
        instance.problem_description = validated_data.get("problem_description", instance.problem_description)
        instance.save()
        return instance


def serialize_car_object(car_instance):
    serializer = CarSerializer(car_instance)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json_data):
    if isinstance(json_data, dict):
        data = json_data
    else:
        if isinstance(json_data, str):
            json_data = json_data.encode("utf-8")

        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)

    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
