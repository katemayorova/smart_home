
from django.urls import path

from measurement.views import AllSensorsView, SingleSensorView, MeasurementView

urlpatterns = [
    path('sensors/', AllSensorsView.as_view()),
    path('sensors/<pk>', SingleSensorView.as_view()),
    path('measurements/', MeasurementView.as_view())
]

