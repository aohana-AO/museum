# Generated by Django 2.2.26 on 2022-01-31 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, max_length=30, verbose_name='電話番号'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='department',
            field=models.CharField(blank=True, max_length=30, verbose_name='住所'),
        ),
    ]