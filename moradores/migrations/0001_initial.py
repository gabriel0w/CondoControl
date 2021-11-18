# Generated by Django 3.2.9 on 2021-11-05 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, null=True)),
                ('telefone', models.CharField(max_length=11, null=True)),
                ('cpf', models.CharField(max_length=11, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]