# Generated by Django 4.0.5 on 2022-06-10 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_recipe_author_recipe_created_at_recipe_img_file_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='author',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='img_file',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='updated_at',
        ),
    ]
