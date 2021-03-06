# Generated by Django 2.1.3 on 2018-11-07 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={},
        ),
        migrations.AlterField(
            model_name='event',
            name='day',
            field=models.DateField(verbose_name='Day of the event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(verbose_name='Final time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Textual Notes'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(verbose_name='Starting time'),
        ),
    ]
