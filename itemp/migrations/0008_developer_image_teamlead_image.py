# Generated by Django 4.1.7 on 2023-08-25 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemp', '0007_teamlead'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='image',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='teamlead',
            name='image',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]
