# Generated by Django 4.2.6 on 2023-10-17 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True)),
                ('email', models.EmailField(max_length=60, null=True)),
                ('password', models.CharField(max_length=12, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
