# Generated by Django 2.1.4 on 2019-02-14 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('uni_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('fullname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
                ('cgpa', models.FloatField(default=0.0)),
                ('credits', models.IntegerField(default=0)),
                ('cat1ptr', models.IntegerField(default=0)),
                ('cat2ptr', models.IntegerField(default=0)),
                ('cat3ptr', models.IntegerField(default=0)),
                ('cat4ptr', models.IntegerField(default=0)),
            ],
        ),
    ]
