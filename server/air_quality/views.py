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


    def fetch_and_store_awair_data():
        GET_URL = 'http://192.168.2.17/air-data/latest'
        try:
            response = requests.get(GET_URL)
            response.raise_for_status()
            awair_data = response.json()

            AwairDataModel.objects.create(
                timestamp=awair_data["timestamp"],
                score=awair_data["score"],
                dew_point=awair_data["dew_point"],
                temp=awair_data["temp"],
                humid=awair_data["humid"],
                abs_humid=awair_data["abs_humid"],
                co2=awair_data["co2"],
                co2_est=awair_data["co2_est"],
                co2_est_baseline=awair_data["co2_est_baseline"],
                voc=awair_data["voc"],
                voc_baseline=awair_data["voc_baseline"],
                voc_h2_raw=awair_data["voc_h2_raw"],
                voc_ethanol_raw=awair_data["voc_ethanol_raw"],
                pm25=awair_data["pm25"],
                pm10_est=awair_data["pm10_est"]
            )
            print("Successfully saved Awair data")
        except requests.RequestException as e:
            print(f'Failed to fetch data: {e}')
        except KeyError as e:
            print(f'Missing data in response: {e}')

        while True:
            time.sleep(10)