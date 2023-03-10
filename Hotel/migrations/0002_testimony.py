# Generated by Django 4.0.5 on 2022-07-28 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('author', models.CharField(max_length=200, verbose_name='Autor')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimoniales',
                'ordering': ['-created'],
            },
        ),
    ]
