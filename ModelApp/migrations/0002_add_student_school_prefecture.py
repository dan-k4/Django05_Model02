# Generated by Django 4.0 on 2022-01-16 09:27

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ModelApp', '0001_add_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prefectures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'prefectures',
            },
        ),
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('prefecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelApp.prefectures')),
            ],
            options={
                'db_table': 'schools',
            },
        ),
        migrations.AlterField(
            model_name='person',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 16, 9, 27, 10, 967130, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='person',
            name='update_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 16, 9, 27, 10, 967212, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('major', models.CharField(max_length=20)),
                ('prefecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelApp.prefectures')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='ModelApp.schools')),
            ],
            options={
                'db_table': 'students',
            },
        ),
    ]