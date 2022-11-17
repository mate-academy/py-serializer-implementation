import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            "id", "manufacturer", "model",
            "horse_powers", "is_broken", "problem_description"
        ]

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


def serialize_car_object(car):
    serializer = CarSerializer(car)
    content = JSONRenderer().render(serializer.data)
    return content


def deserialize_car_object(content):
    stream = io.BytesIO(content)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return serializer
