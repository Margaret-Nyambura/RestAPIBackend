# Generated by Django 5.0.6 on 2024-08-22 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('work_number', models.PositiveBigIntegerField()),
                ('hire_date', models.DateField()),
                ('office_hours', models.DurationField()),
                ('faculty', models.CharField(max_length=30)),
                ('course', models.CharField(max_length=30)),
                ('nationality', models.CharField(max_length=25)),
                ('bank_account', models.CharField(max_length=20)),
            ],
        ),
    ]
