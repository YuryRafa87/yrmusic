# Generated by Django 4.2.5 on 2023-10-10 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_amigo_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='amigo',
            name='categoria',
            field=models.CharField(blank=True, max_length=200, verbose_name='categoria'),
        ),
    ]