# Generated by Django 4.1.7 on 2023-06-24 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fdo_app', '0006_alter_creativework_creator_org_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creativework',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='person',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
