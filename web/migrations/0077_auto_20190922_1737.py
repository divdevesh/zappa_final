# Generated by Django 2.2.4 on 2019-09-22 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0076_auto_20190922_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='currency',
            field=models.CharField(default='SEK', max_length=5, verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='article',
            name='price',
            field=models.FloatField(default=0, max_length=10, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='historicalarticle',
            name='currency',
            field=models.CharField(default='SEK', max_length=5, verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='historicalarticle',
            name='price',
            field=models.FloatField(default=0, max_length=10, verbose_name='Price'),
        ),
    ]
