# Generated by Django 4.2.6 on 2024-09-18 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=50)),
                ('p_code', models.CharField(max_length=20, unique=True)),
                ('p_quantity', models.IntegerField()),
                ('p_exp_data', models.DateField()),
            ],
        ),
    ]
