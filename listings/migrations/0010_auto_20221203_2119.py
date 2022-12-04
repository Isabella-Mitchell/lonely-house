# Generated by Django 3.2.16 on 2022-12-03 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_auto_20221203_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='map_embed',
        ),
        migrations.AlterField(
            model_name='listing',
            name='latitude',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='listing',
            name='longitude',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=12),
        ),
    ]