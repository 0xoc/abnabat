# Generated by Django 2.0.7 on 2018-07-18 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_imagefield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefield',
            name='img',
            field=models.ImageField(upload_to='%y/%m/%d/%s'),
        ),
    ]