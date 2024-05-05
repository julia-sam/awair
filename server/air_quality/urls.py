from django.urls import path
from .views import AirQualityData

urlpatterns = [
    path('api/latest-air-quality/', AirQualityData.as_view(), name='latest-air-quality'),
]