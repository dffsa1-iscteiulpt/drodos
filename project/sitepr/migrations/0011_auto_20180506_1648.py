# Generated by Django 2.0.4 on 2018-05-06 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitepr', '0010_auto_20180506_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeditem',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
