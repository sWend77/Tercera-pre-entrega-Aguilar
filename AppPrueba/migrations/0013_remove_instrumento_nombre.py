# Generated by Django 5.0.6 on 2024-06-24 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppPrueba', '0012_rename_tipo_instrumento_modelo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrumento',
            name='nombre',
        ),
    ]
