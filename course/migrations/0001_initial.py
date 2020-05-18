# Generated by Django 3.0.3 on 2020-05-18 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('instructor', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('Udemy', 'Udemy'), ('YouTube', 'YouTube')], max_length=50)),
                ('link', models.URLField()),
                ('image', models.URLField()),
                ('completed', models.IntegerField()),
            ],
        ),
    ]
