# Generated by Django 4.2.3 on 2023-07-19 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0012_hostelallocation_date_of_allocation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostelallocation',
            name='date_of_allocation',
        ),
    ]
