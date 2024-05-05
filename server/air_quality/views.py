from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AwairDataModel
from .serializers import AwairDataSerializer
import requests, time

class AirQualityData(APIView):
    def get(self, request):
        try:
            latest_data = AwairDataModel.objects.all()
            serializer = AwairDataSerializer(latest_data, many=True)
            return Response(serializer.data)
        except AwairDataModel.DoesNotExist:
            return Response({'error': 'No data available'}, status=404)
