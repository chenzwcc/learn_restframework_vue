# Generated by Django 2.0.2 on 2019-06-04 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='商品名称'),
        ),
    ]
