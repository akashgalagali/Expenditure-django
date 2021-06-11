# Generated by Django 3.2.4 on 2021-06-11 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('particular', models.CharField(max_length=50)),
                ('amount', models.FloatField(max_length=100)),
                ('mode_of_payment', models.CharField(max_length=50)),
            ],
        ),
    ]