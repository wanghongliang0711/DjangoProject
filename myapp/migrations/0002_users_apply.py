# Generated by Django 3.0.4 on 2020-03-16 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='apply',
            field=models.IntegerField(default=1),
        ),
    ]
