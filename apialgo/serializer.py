from rest_framework import serializers
from apialgo.models import Measurements


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = '__all__'
