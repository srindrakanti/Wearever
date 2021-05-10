# Generated by Django 3.2.2 on 2021-05-10 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('temp', models.FloatField()),
                ('humidity', models.IntegerField()),
                ('windspeed', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('rec', models.JSONField()),
            ],
        ),
    ]