# Generated by Django 3.2.2 on 2021-05-07 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
            ],
        ),
    ]