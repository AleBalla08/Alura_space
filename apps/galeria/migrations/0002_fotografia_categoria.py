# Generated by Django 3.2.25 on 2024-08-29 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'nebulosa'), ('ESTRELA', 'estrela'), ('GALÁXIA', 'galáxia'), ('PLANETA', 'planeta')], default='', max_length=20),
        ),
    ]
