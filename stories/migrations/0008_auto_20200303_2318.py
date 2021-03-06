# Generated by Django 3.0.3 on 2020-03-03 23:18

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0007_auto_20200303_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='admin_tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=120), size=None),
        ),
        migrations.AlterField(
            model_name='story',
            name='license',
            field=models.CharField(blank=True, choices=[('opn', 'Open Source'), ('mit', 'MIT License')], default='mit', max_length=3),
        ),
        migrations.AlterField(
            model_name='story',
            name='status',
            field=models.CharField(blank=True, choices=[('dft', 'Draft'), ('pub', 'Published')], default='dft', max_length=3),
        ),
        migrations.AlterField(
            model_name='story',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=120), size=None),
        ),
    ]
