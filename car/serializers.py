from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(min_value=1, max_value=300)
    is_broken = serializers.BooleanField(default=False)
    problem_description = serializers.CharField(max_length=1024,
                                                allow_null=True,
                                                allow_blank=True,
                                                required=False)
