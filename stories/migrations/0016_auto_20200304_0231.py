# Generated by Django 3.0.3 on 2020-03-04 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0015_auto_20200304_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='seo_title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
