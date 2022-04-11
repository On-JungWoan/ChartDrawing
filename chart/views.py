from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import View
from django.shortcuts import render
import numpy as np

from .models import ChartData, User

from time import mktime, strptime

class ChartDataAPIView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        chart_datas = ChartData.objects.all().order_by('date')

        data_dict = {
            'temp_list': [],
            'humi_list': [],
            'co2_list': []
        }
        for i in range(1, len(chart_datas) + 1, 1):
            data_ = chart_datas.get(id=i)
            data_dict['temp_list'].append(data_.temp)
            data_dict['humi_list'].append(data_.humidity)
            data_dict['co2_list'].append(data_.CO2)

        mean_list = []
        std_list = []
        for data_list in data_dict.values():
            mean_list.append(np.mean(data_list))
            std_list.append(np.std(data_list))

        temperatrue_list = []
        humidity_list = []
        co2_list = []

        for chart_data in chart_datas:
            time_tuple = strptime(str(chart_data.date), '%Y-%m-%d')
            utc_now = mktime(time_tuple) * 1000
            temperatrue_list.append([utc_now, chart_data. temp])
            humidity_list.append([utc_now, chart_data.humidity])
            co2_list.append([utc_now, chart_data.CO2])

        data = {
            'temperature': temperatrue_list,
            'humidity': humidity_list,
            'co2': co2_list,
            'avg':mean_list,
            'std':std_list
        }

        return Response(data)


def ChartView(request):
    chartdata = ChartData.objects.order_by('date')
    context = {
        'chartdatas': chartdata,
    }
    return render(request, 'chart/chart.html', context)