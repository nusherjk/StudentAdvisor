# Generated by Django 2.1.4 on 2019-02-19 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0005_auto_20190219_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grades',
            name='crs',
        ),
        migrations.AddField(
            model_name='grades',
            name='Course_name',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='grades',
            name='Student_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='grades',
            name='grdpa',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='grades',
            name='semnum',
            field=models.IntegerField(default=0),
        ),
    ]
