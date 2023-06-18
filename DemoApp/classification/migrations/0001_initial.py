# Generated by Django 3.2.19 on 2023-06-18 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='predicted')),
                ('model', models.CharField(choices=[('1', 'Model 1 - ResNetV2 layer, Flatten, Dense 126,64,64,2'), ('2', 'Model 2 -  ResNetV2 layer, Flatten, Dense 264, Dropout 0.3, Dense 128, Dropout 0.1, Dense 2'), ('3', 'Model 3 - Xception layer, Flatten, Dense 264,128,64,2'), ('4', 'Model 4 - Xception layer, Flatten, Dense 128, Dropout 0.3, Dense 64, Dropout 0.1, Dense 2')], max_length=100)),
                ('predicted_value', models.CharField(max_length=10)),
                ('likelihood_indoor', models.FloatField()),
                ('likelihood_outdoor', models.FloatField()),
            ],
        ),
    ]