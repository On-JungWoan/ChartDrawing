from django.db import models

class ChartData(models.Model):
    date = models.DateField("날짜", max_length=10, null=False, unique=True)
    temp = models.FloatField("온도", null=True)
    humidity = models.FloatField("습도", null=True)
    CO2 = models.FloatField("CO2", null=True)

class User(models.Model):
    # 각각의 변수 / 보여지는 단어 로 이루어진 튜플을 가진 dict를 다음과 같이 생성
    GENDER_CHOICES = {
        ('temp', 'Temp'),  # 오른쪽에 있는 것이 화면에 보인다.
        ('humidity', 'Humidity'),
        ('CO2', 'CO2')
    }
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
