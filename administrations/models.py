from django.db import models

# Create your models here.


class AdministrationProfile(models.Model):
    first_name = models.CharField('First Name', max_length=100, blank=False)
    last_name = models.CharField('Last Name', max_length=100, blank=False)
    role = models.CharField('Role', max_length=100)
    password = models.CharField('Password', max_length=100)
    email = models.CharField('Email', max_length=100, unique=True)
    organization = models.CharField('Organization', max_length=100)
    address = models.CharField('Address', max_length=100)
    city = models.CharField('city', max_length=100)

# class Achievement