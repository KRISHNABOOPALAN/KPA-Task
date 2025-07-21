from rest_framework import serializers
from .models import BogieChecksheet, WheelSpec

class BogieChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieChecksheet
        fields = '__all__'

class WheelSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelSpec
        fields = '__all__'
