# Generated by Django 2.0.4 on 2018-05-08 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitepr', '0029_auto_20180508_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='premium',
            field=models.BooleanField(default=False),
        ),
    ]