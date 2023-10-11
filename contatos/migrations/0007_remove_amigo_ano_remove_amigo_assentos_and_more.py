# Generated by Django 4.2.5 on 2023-10-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0006_rename_assentos_amigo_assentos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amigo',
            name='ano',
        ),
        migrations.RemoveField(
            model_name='amigo',
            name='assentos',
        ),
        migrations.RemoveField(
            model_name='amigo',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='amigo',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='amigo',
            name='fabricante',
        ),
        migrations.RemoveField(
            model_name='amigo',
            name='modelo',
        ),
        migrations.RemoveField(
            model_name='amigo',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='amigo',
            name='whatsapp',
        ),
        migrations.AddField(
            model_name='amigo',
            name='Artista',
            field=models.CharField(blank=True, max_length=200, verbose_name='Artista'),
        ),
        migrations.AddField(
            model_name='amigo',
            name='Capa',
            field=models.ImageField(blank=True, null=True, upload_to='avatares', verbose_name='Capa'),
        ),
        migrations.AddField(
            model_name='amigo',
            name='Duração',
            field=models.CharField(blank=True, max_length=200, verbose_name='Duração'),
        ),
        migrations.AddField(
            model_name='amigo',
            name='Titulo',
            field=models.CharField(blank=True, max_length=200, verbose_name='Título'),
        ),
        migrations.AddField(
            model_name='amigo',
            name='Ano',
            field=models.DateField(blank=True, null=True, verbose_name='Ano de Lançamento'),
        ),
    ]