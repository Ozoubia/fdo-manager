# Generated by Django 4.1.6 on 2023-05-07 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fdo_app', '0002_creativework_organisation_person_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='provider_type',
            field=models.CharField(choices=[('person', 'Person'), ('organisation', 'Organisation')], max_length=20),
        ),
    ]