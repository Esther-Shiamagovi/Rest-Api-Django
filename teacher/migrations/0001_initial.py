# Generated by Django 5.0.7 on 2024-07-14 19:21

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
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('enrollment_date', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('bio', models.TextField()),
                ('teacher_id', models.IntegerField()),
                ('country', models.CharField(max_length=32)),
                ('subject_teaching', models.CharField(max_length=40)),
            ],
        ),
    ]