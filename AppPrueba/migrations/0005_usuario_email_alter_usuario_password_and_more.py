# Generated by Django 5.0.6 on 2024-06-05 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPrueba', '0004_artista_instrumento'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user',
            field=models.CharField(max_length=20),
        ),
    ]
