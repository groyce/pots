# Generated by Django 2.1.2 on 2018-12-02 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20181129_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale',
            field=models.BooleanField(default=False),
        ),
    ]