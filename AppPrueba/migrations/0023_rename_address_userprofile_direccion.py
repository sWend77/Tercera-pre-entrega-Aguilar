# Generated by Django 5.0.6 on 2024-07-09 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppPrueba', '0022_alter_instrumento_marca'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='address',
            new_name='direccion',
        ),
    ]
