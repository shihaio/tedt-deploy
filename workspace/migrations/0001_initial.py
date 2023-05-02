# Generated by Django 4.2 on 2023-05-01 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=75)),
                ('password', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('user_created_date', models.DateTimeField(auto_now_add=True)), 
            ],
        ),
    ]
