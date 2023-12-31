# Generated by Django 4.2.7 on 2023-12-18 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('mail', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('ipadress', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='user_session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_session', models.CharField(max_length=30)),
                ('exp_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
