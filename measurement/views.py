from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SingleSensorSerializer, \
    CreateMeasurementSerializer


class AllSensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SingleSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SingleSensorSerializer


class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = CreateMeasurementSerializer



