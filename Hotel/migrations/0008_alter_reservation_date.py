# Generated by Django 4.0.5 on 2022-08-10 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0007_alter_reservation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(verbose_name='Fecha'),
        ),
    ]