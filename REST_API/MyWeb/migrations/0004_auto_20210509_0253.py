# Generated by Django 3.2.2 on 2021-05-08 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyWeb', '0003_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='il',
            new_name='Faculty',
        ),
        migrations.RenameField(
            model_name='details',
            old_name='course',
            new_name='Stud_Name',
        ),
        migrations.RemoveField(
            model_name='details',
            name='sp',
        ),
    ]
