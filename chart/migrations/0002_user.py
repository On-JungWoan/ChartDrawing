# Generated by Django 3.1.3 on 2022-04-11 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('CO2', 'CO2'), ('temp', 'Temp'), ('humidity', 'Humidity')], max_length=80, null=True)),
            ],
        ),
    ]