# Generated by Django 5.0.6 on 2024-06-26 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPrueba', '0016_userprofile_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='artista',
            name='biografia',
            field=models.CharField(default=False, max_length=130423952),
        ),
        migrations.AddField(
            model_name='artista',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
