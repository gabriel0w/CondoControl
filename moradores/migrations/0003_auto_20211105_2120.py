# Generated by Django 3.2.9 on 2021-11-05 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moradores', '0002_apto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apto',
            name='id_pessoa',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='apto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='moradores.apto'),
        ),
    ]
