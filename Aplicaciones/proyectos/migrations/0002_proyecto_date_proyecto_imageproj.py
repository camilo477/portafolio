# Generated by Django 4.2.5 on 2023-10-19 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='imageproj',
            field=models.FileField(null=True, upload_to='proyectos/'),
        ),
    ]
