# Generated by Django 4.1.7 on 2023-02-16 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TranlastionObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InputText', models.CharField(max_length=100)),
                ('OutputText', models.CharField(max_length=100)),
                ('FromUser', models.CharField(max_length=100)),
            ],
        ),
    ]