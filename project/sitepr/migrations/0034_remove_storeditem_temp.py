# Generated by Django 2.0.4 on 2018-05-08 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitepr', '0033_auto_20180508_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storeditem',
            name='temp',
        ),
    ]