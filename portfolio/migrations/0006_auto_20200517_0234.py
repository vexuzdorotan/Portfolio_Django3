# Generated by Django 3.0.3 on 2020-05-16 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20200517_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='fa_icon',
            field=models.CharField(max_length=50),
        ),
    ]
