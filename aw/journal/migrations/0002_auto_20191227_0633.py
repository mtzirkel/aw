# Generated by Django 3.0.1 on 2019-12-27 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentry',
            name='date',
            field=models.DateField(),
        ),
    ]
