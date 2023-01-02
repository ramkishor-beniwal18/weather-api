from rest_framework import serializers

from .models import Record


class RecordSerializer(serializers.ModelSerializer):
    date = serializers.DateField()
    lat = serializers.FloatField()
    lon = serializers.FloatField()
    city = serializers.CharField(max_length=255)
    state = serializers.CharField(max_length=255)
    temperature = serializers.FloatField()

    class Meta:
        model = Record
        fields = '__all__'
