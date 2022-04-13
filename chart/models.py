from django.db import models

class ChartData(models.Model):
    date = models.CharField("날짜", max_length=20, null=False)
    inner_temp = models.FloatField("내부 온도", null=True)
    outside_temp = models.FloatField("외부 온도", null=True)
    inner_humidity = models.FloatField("내부 습도", null=True)
    co2 = models.FloatField("co2", null=True)
    cumulative_radiation = models.FloatField("자외선", null=True)