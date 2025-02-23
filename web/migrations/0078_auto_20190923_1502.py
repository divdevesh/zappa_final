# Generated by Django 2.2.4 on 2019-09-23 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0077_auto_20190922_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='article',
            name='price',
        ),
        migrations.RemoveField(
            model_name='historicalarticle',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='historicalarticle',
            name='price',
        ),
        migrations.AddField(
            model_name='historicalmerchantarticle',
            name='currency',
            field=models.CharField(default='SEK', max_length=5, verbose_name='Currency'),
        ),
        migrations.AddField(
            model_name='historicalmerchantarticle',
            name='price',
            field=models.FloatField(default=0, max_length=10, verbose_name='Price'),
        ),
        migrations.AddField(
            model_name='historicalmerchantarticle',
            name='sales_price',
            field=models.FloatField(default=0, max_length=10, verbose_name='Sales Price'),
        ),
        migrations.AddField(
            model_name='historicalmerchantarticle',
            name='sales_price_valid_from',
            field=models.CharField(blank=True, max_length=20, verbose_name='Sales Price Valid From'),
        ),
        migrations.AddField(
            model_name='historicalmerchantarticle',
            name='sales_price_valid_to',
            field=models.CharField(blank=True, max_length=20, verbose_name='Sales Price Valid To'),
        ),
        migrations.AddField(
            model_name='merchantarticle',
            name='currency',
            field=models.CharField(default='SEK', max_length=5, verbose_name='Currency'),
        ),
        migrations.AddField(
            model_name='merchantarticle',
            name='price',
            field=models.FloatField(default=0, max_length=10, verbose_name='Price'),
        ),
        migrations.AddField(
            model_name='merchantarticle',
            name='sales_price',
            field=models.FloatField(default=0, max_length=10, verbose_name='Sales Price'),
        ),
        migrations.AddField(
            model_name='merchantarticle',
            name='sales_price_valid_from',
            field=models.CharField(blank=True, max_length=20, verbose_name='Sales Price Valid From'),
        ),
        migrations.AddField(
            model_name='merchantarticle',
            name='sales_price_valid_to',
            field=models.CharField(blank=True, max_length=20, verbose_name='Sales Price Valid To'),
        ),
    ]
