from rest_framework import serializers
from .models import AwairDataModel

class AwairDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwairDataModel
        fields = '__all__' 