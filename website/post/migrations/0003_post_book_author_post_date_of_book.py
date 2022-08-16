# Generated by Django 4.0.5 on 2022-06-11 13:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='book_author',
            field=models.CharField(default="kiarash", max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='date_of_book',
            field=models.IntegerField(default=2022),
            preserve_default=False,
        ),
    ]