# Generated by Django 4.2.4 on 2023-08-31 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aprendiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('year_birth', models.PositiveIntegerField()),
                ('document_num', models.PositiveIntegerField()),
                ('document_type', models.PositiveIntegerField()),
                ('ficha_num', models.PositiveIntegerField()),
            ],
        ),
    ]
