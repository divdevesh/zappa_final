# Generated by Django 2.2 on 2019-06-12 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0067_auto_20190611_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmerchantarticle',
            name='prefered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='merchantarticle',
            name='prefered',
            field=models.BooleanField(default=False),
        ),
    ]
