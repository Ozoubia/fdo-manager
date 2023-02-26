# Generated by Django 4.1.7 on 2023-02-19 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fdo_app', '0002_remove_test_t_created_test_t_last_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FDO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PID', models.IntegerField()),
                ('metadata_ID', models.IntegerField()),
                ('PID_bit_seq', models.CharField(max_length=200)),
                ('PID_record_ID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PID_metadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licence', models.CharField(max_length=10)),
                ('publisher', models.CharField(max_length=100)),
                ('creator', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PID_records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metadata_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fdo_app.pid_metadata')),
            ],
        ),
        migrations.CreateModel(
            name='profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute1', models.CharField(max_length=50)),
                ('attribute2', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='test_t',
        ),
        migrations.AddField(
            model_name='pid_records',
            name='profile_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fdo_app.profiles'),
        ),
    ]