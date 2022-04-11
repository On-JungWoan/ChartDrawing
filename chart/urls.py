from django.urls import path
from . import views

app_name = 'chart'

urlpatterns = [
    path('api/', views.ChartDataAPIView.as_view(), name="chart_data_api"),
    path('', views.ChartView, name="chart"),
]
