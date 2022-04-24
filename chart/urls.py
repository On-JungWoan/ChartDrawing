from django.urls import path
from . import views

app_name = 'chart'

urlpatterns = [
    path('', views.ChartView, name="chart"),
    path('api/', views.ChartDataAPIView.as_view(), name="chart_data_api"),
]
