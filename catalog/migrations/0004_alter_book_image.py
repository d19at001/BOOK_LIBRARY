# Generated by Django 4.1.2 on 2022-10-22 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='locallibrary/files/covers'),
        ),
    ]