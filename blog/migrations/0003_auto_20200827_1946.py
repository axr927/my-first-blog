# Generated by Django 2.2.15 on 2020-08-27 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='address',
            field=models.CharField(default='N/A', max_length=300),
        ),
        migrations.AddField(
            model_name='cv',
            name='phone_number',
            field=models.CharField(default='N/A', max_length=20),
        ),
    ]
