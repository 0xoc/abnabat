# Generated by Django 2.0.7 on 2018-07-17 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_auto_20180710_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliver',
            name='deliver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_management.Person'),
        ),
        migrations.AlterField(
            model_name='package',
            name='products',
            field=models.ManyToManyField(to='inventory.Product'),
        ),
    ]
