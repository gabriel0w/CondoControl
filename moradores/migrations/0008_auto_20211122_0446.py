# Generated by Django 3.2.9 on 2021-11-22 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moradores', '0007_alter_prestador_apto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='apto',
        ),
        migrations.RemoveField(
            model_name='prestador',
            name='apto',
        ),
        migrations.DeleteModel(
            name='apto',
        ),
        migrations.DeleteModel(
            name='pessoa',
        ),
        migrations.DeleteModel(
            name='prestador',
        ),
    ]
