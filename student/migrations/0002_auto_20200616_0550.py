# Generated by Django 3.0.7 on 2020-06-16 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='studentAge',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentFee',
            field=models.IntegerField(),
        ),
    ]
