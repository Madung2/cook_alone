# Generated by Django 4.0.5 on 2022-06-10 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diffcate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.CharField(default='', max_length=50)),
            ],
            options={
                'db_table': 'difficulty',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img_url', models.URLField(default='', max_length=300)),
                ('timecost', models.CharField(max_length=10, null=True)),
                ('difficulty', models.CharField(max_length=10)),
                ('ingredient', models.TextField()),
                ('cookstep', models.TextField()),
            ],
            options={
                'db_table': 'recipe',
            },
        ),
        migrations.CreateModel(
            name='Timecate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timecost', models.CharField(default='', max_length=50)),
            ],
            options={
                'db_table': 'timecost',
            },
        ),
    ]
