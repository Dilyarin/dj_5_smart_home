# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensorr, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer



class sensor(ListAPIView):
    queryset = Sensorr.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        sensor = request.GET.get("sensor")
        descriptions = request.GET.get("description")
        add_sensor = Sensorr(name = sensor, description = descriptions)
        add_sensor.save
        return Response({'status': 'OK'})


class measure(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        # sensor = request.GET.get("sensor")
        temperature = request.GET.get("temperature")
        created_at = request.GET.get("created_at")
        add_measure = Measurement(temperature = temperature, created_at = created_at)
        add_measure.save
        return Response({'status': 'OK'})

class sensorView(RetrieveAPIView):
    queryset = Sensorr.objects.all()
    serializer_class = SensorDetailSerializer