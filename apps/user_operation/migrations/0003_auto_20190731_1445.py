# Generated by Django 2.0.2 on 2019-07-31 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0002_auto_20190724_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='详细地址'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='district',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='区域'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='province',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='省份'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='signer_mobile',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='signer_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='签收人'),
        ),
    ]
