# Generated by Django 5.0.3 on 2024-04-27 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_verification1'),
    ]

    operations = [
        migrations.AddField(
            model_name='verification',
            name='certificateNumber',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='verification',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
