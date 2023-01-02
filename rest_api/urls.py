from django.urls import path

from .views import RecordWeatherView

urlpatterns = [
    path('weather/', RecordWeatherView.as_view()),
    path('weather/<id>/', RecordWeatherView.as_view())
]
