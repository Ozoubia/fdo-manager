# Generated by Django 4.1.6 on 2023-05-07 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fdo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreativeWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=200)),
                ('identifier', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('creativeWorkType', models.CharField(choices=[('dataset', 'Dataset'), ('code', 'Code'), ('article', 'Article')], max_length=100)),
                ('creator_type', models.CharField(choices=[('person', 'Person'), ('organisation', 'Organisation')], max_length=20)),
                ('creator_id', models.PositiveIntegerField()),
                ('keywords', models.CharField(max_length=200)),
                ('dateCreated', models.DateField()),
                ('dateModified', models.DateField()),
                ('licence', models.CharField(max_length=200)),
                ('version', models.IntegerField()),
                ('size', models.CharField(max_length=50)),
                ('usage_info', models.CharField(max_length=200)),
                ('citation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fdo_app.creativework')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=200)),
                ('identifier', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('legalName', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=200)),
                ('identifier', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=100)),
                ('affiliation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fdo_app.organisation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=200)),
                ('identifier', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('provider_type', models.CharField(choices=[('person', 'Person'), ('organisation', 'Organisation')], default=None, max_length=20)),
                ('termsOfService', models.CharField(max_length=200)),
                ('provider_org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fdo_app.organisation')),
                ('provider_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fdo_app.person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='test_t',
        ),
        migrations.CreateModel(
            name='SoftwareApplication',
            fields=[
                ('creativework_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fdo_app.creativework')),
                ('releaseNotes', models.CharField(max_length=200)),
                ('softwareRequirements', models.CharField(max_length=200)),
                ('downloadUrl', models.CharField(max_length=200)),
                ('memoryRequirements', models.CharField(max_length=50)),
                ('operatingSystem', models.CharField(max_length=50)),
                ('processorRequirements', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('fdo_app.creativework',),
        ),
        migrations.CreateModel(
            name='WebAPI',
            fields=[
                ('service_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fdo_app.service')),
                ('documentation', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=('fdo_app.service',),
        ),
        migrations.AddField(
            model_name='creativework',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fdo_app.organisation'),
        ),
    ]
