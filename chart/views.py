from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import View
from django.shortcuts import render
import numpy as np

from .models import ChartData

from time import mktime, strptime

class ChartDataAPIView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        chart_datas = ChartData.objects.all().order_by('id')

        data_dict = {
            'inner_temp_list': [],
            'outside_temp_list': [],
            'humi_list': [],
            'co2_list': [],
            'radiation_list':[]
        }
        for i in range(1, len(chart_datas) + 1, 1):
            data_ = chart_datas.get(id=i)
            data_dict['inner_temp_list'].append(data_.inner_temp)
            data_dict['outside_temp_list'].append(data_.outside_temp)
            data_dict['humi_list'].append(data_.inner_humidity)
            data_dict['co2_list'].append(data_.co2)
            data_dict['radiation_list'].append(data_.cumulative_radiation)

        mean_list = []
        std_list = []
        for data_list in data_dict.values():
            mean_list.append(np.mean(data_list))
            std_list.append(np.std(data_list))

        inner_temp_list = []
        outside_temp_list = []
        inner_humidity_list = []
        co2_list = []
        radiation_list = []

        for chart_data in chart_datas:
            time_tuple = strptime(chart_data.date, '%Y-%m-%d %H:%M')
            utc_now = mktime(time_tuple) * 1000
            inner_temp_list.append([utc_now, chart_data.inner_temp])
            outside_temp_list.append([utc_now, chart_data.outside_temp])
            inner_humidity_list.append([utc_now, chart_data.inner_humidity])
            co2_list.append([utc_now, chart_data.co2])
            radiation_list.append([utc_now, chart_data.cumulative_radiation])

        data = {
            'inner_temp': inner_temp_list,
            'outside_temp': outside_temp_list,
            'inner_humidity': inner_humidity_list,
            'co2': co2_list,
            'radiation': radiation_list,
            'avg':mean_list,
            'std':std_list
        }

        return Response(data)


def ChartView(request):
    chartdata = ChartData.objects.order_by('id')
    context = {
        'chartdatas': chartdata,
    }
    return render(request, 'chart/chart.html', context)