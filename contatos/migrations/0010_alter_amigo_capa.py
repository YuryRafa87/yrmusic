# Generated by Django 4.2.5 on 2023-10-11 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0009_remove_amigo_avatar_remove_amigo_duração_amigo_capa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amigo',
            name='Capa',
            field=models.ImageField(blank=True, null=True, upload_to='avatares', verbose_name='Capa'),
        ),
    ]
