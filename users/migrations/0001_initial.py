# Generated by Django 3.2.7 on 2021-09-25 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('address', models.CharField(max_length=300, verbose_name='Your Address')),
                ('mobile', models.CharField(max_length=50, verbose_name='Mobile Number')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
                ('rating', models.IntegerField(default=0, verbose_name='User Rating')),
            ],
        ),
    ]