# Generated by Django 3.1.1 on 2020-09-11 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20200911_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='mttd',
            name='department',
            field=models.CharField(default='N/A', max_length=32),
        ),
        migrations.AddField(
            model_name='mttr',
            name='department',
            field=models.CharField(default='N/A', max_length=32),
        ),
        migrations.AlterField(
            model_name='mttd',
            name='ticket_id',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='mttr',
            name='ticket_id',
            field=models.PositiveIntegerField(),
        ),
    ]
