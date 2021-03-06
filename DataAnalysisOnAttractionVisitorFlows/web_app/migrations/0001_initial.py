# Generated by Django 3.1.4 on 2020-12-10 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JsonData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('CODE', models.CharField(max_length=20, null=True)),
                ('NAME', models.CharField(max_length=20, null=True)),
                ('ADDRESS', models.CharField(max_length=40, null=True)),
                ('DES', models.CharField(max_length=20, null=True)),
                ('TIME', models.CharField(max_length=20, null=True)),
                ('GRADE', models.CharField(max_length=20, null=True)),
                ('T_TIME', models.CharField(max_length=20, null=True)),
                ('MAX_NUM', models.CharField(max_length=20, null=True)),
                ('SSD', models.CharField(max_length=20, null=True)),
                ('NUM', models.IntegerField(null=True)),
                ('TYPE', models.CharField(max_length=20, null=True)),
                ('T_CODE', models.CharField(max_length=20, null=True)),
                ('INSERT_TIME', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
