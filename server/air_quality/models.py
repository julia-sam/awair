from django.db import models

# Create your models here.
class AwairDataModel(models.Model):
    timestamp = models.CharField(max_length=125)
    score = models.FloatField()
    dew_point = models.FloatField()
    temp = models.FloatField()
    humid = models.FloatField()
    abs_humid = models.FloatField()
    co2 = models.FloatField()
    co2_est = models.FloatField()
    co2_est_baseline = models.FloatField()
    voc = models.FloatField()
    voc_baseline = models.FloatField()
    voc_h2_raw = models.FloatField()
    voc_ethanol_raw = models.FloatField()
    pm25 = models.FloatField()
    pm10_est = models.FloatField()