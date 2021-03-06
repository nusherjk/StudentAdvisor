# Generated by Django 2.1.4 on 2019-12-20 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0016_auto_20191212_0121'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluationScripts',
            fields=[
                ('eval_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('faculty_name', models.CharField(max_length=200)),
                ('option1_input', models.CharField(max_length=10)),
                ('option2_input', models.CharField(max_length=10)),
                ('option3_input', models.CharField(max_length=10)),
                ('option4_input', models.CharField(max_length=10)),
                ('option5_input', models.CharField(max_length=10)),
                ('option6_input', models.CharField(max_length=10)),
                ('comment', models.CharField(max_length=1000)),
                ('submitter_id', models.IntegerField()),
            ],
        ),
    ]
