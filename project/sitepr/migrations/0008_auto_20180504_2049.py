# Generated by Django 2.0.4 on 2018-05-04 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitepr', '0007_auto_20180504_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeditem',
            name='fileUrl',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]