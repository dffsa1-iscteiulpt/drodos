# Generated by Django 2.0.4 on 2018-05-07 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitepr', '0017_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='group',
            name='name',
            field=models.CharField(default='name', max_length=50),
        ),
    ]
