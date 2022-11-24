from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensorr(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    # measurements = models.oneToMany('Measurement')

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensorr, on_delete=models.CASCADE)
    temperature = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)