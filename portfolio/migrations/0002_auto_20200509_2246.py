# Generated by Django 3.0.3 on 2020-05-09 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]
