# Generated by Django 4.2.7 on 2023-12-19 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_userdata_delete_userpermission'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='colorRotation',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
