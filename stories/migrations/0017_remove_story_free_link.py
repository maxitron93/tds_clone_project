# Generated by Django 3.0.3 on 2020-03-04 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0016_auto_20200304_0231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='free_link',
        ),
    ]