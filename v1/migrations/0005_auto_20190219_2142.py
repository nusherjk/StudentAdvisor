# Generated by Django 2.1.4 on 2019-02-19 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0004_auto_20190219_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grades',
            name='course_id',
        ),
        migrations.AddField(
            model_name='grades',
            name='crs',
            field=models.ManyToManyField(to='v1.Courses'),
        ),
    ]
