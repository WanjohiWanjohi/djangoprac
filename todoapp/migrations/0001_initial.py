# Generated by Django 3.0.7 on 2020-06-17 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(max_length=128)),
                ('is_complete', models.BooleanField(default=False)),
                ('datePublished', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
