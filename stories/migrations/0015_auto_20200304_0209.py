# Generated by Django 3.0.3 on 2020-03-04 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0014_auto_20200304_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='seo_description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='story',
            name='seo_title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='story',
            name='title',
            field=models.CharField(default='Untitled', max_length=200),
        ),
    ]
