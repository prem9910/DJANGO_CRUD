# Generated by Django 4.2.4 on 2023-08-23 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True)),
                ('email', models.EmailField(max_length=6, null=True)),
                ('password', models.CharField(max_length=12, null=True)),
            ],
        ),
    ]
