# Generated by Django 4.1.7 on 2023-08-23 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itemp', '0006_developer_password_developer_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teamlead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('username', models.CharField(max_length=100, null=True)),
                ('number', models.IntegerField(max_length=10, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('dob', models.DateField(null=True)),
                ('address1', models.CharField(max_length=255, null=True)),
                ('address2', models.CharField(max_length=255, null=True)),
                ('address3', models.CharField(max_length=255, null=True)),
                ('pincode', models.IntegerField(max_length=6, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('attachment', models.FileField(null=True, upload_to='')),
                ('status', models.IntegerField(default=0)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='itemp.course')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='itemp.department')),
            ],
        ),
    ]