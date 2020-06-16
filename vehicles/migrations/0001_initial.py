# Generated by Django 3.0.7 on 2020-06-16 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_registration_number', models.CharField(max_length=16)),
                ('vehicle_color', models.CharField(max_length=128)),
                ('vehicle_image', models.ImageField(upload_to='media/')),
                ('vehicle_brand', models.CharField(choices=[('HN', 'Honda'), ('TY', 'Toyota'), ('MD', 'Merecedes'), ('BMW', 'BMW')], max_length=32)),
                ('vehicle_manufactured', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
