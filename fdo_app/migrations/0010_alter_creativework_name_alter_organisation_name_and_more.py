# Generated by Django 4.1.7 on 2023-06-24 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fdo_app', '0009_alter_creativework_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creativework',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
