# Generated by Django 4.1.7 on 2023-08-22 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]