# Generated by Django 5.0.6 on 2024-06-05 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppPrueba', '0002_musica'),
    ]

    operations = [
        migrations.RenameField(
            model_name='musica',
            old_name='title',
            new_name='name_song',
        ),
    ]
