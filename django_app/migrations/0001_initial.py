# Generated by Django 3.2.16 on 2022-10-25 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, max_length=30)),
                ('user_first_name', models.CharField(blank=True, max_length=40)),
                ('user_last_name', models.CharField(blank=True, max_length=40)),
                ('user_password', models.CharField(blank=True, max_length=200)),
                ('user_email', models.EmailField(blank=True, max_length=40)),
                ('user_status', models.CharField(blank=True, max_length=30)),
                ('user_phone_number', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'db_table': 'user_table',
            },
        ),
    ]