# Generated by Django 3.0.3 on 2020-05-10 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20200509_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='description',
            field=models.TextField(),
        ),
    ]
