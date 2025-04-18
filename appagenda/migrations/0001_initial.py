# Generated by Django 5.1.7 on 2025-03-13 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidadao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField()),
                ('cpf', models.CharField(max_length=14, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('data_nascimento', models.DateField()),
                ('celular', models.CharField(max_length=14)),
                ('cep', models.CharField(max_length=9)),
                ('endereco', models.TextField()),
                ('endereco_numero', models.CharField(max_length=20)),
                ('data_info', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
