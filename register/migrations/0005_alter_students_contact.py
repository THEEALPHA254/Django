# Generated by Django 4.2.3 on 2023-07-19 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_remove_students_telphone_no_students_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='contact',
            field=models.BigIntegerField(),
        ),
    ]