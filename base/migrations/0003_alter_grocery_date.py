# Generated by Django 3.2.5 on 2021-09-23 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_grocery_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocery',
            name='date',
            field=models.DateField(blank=True, verbose_name='YY-MM-DD'),
        ),
    ]
