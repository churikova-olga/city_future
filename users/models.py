from django.db import models

# Create your models here.


class UserProfile(models.Model):
    first_name = models.CharField('First Name', max_length=100, blank=False)
    last_name = models.CharField('Last Name', max_length=100, blank=False)
    address = models.CharField('Your Address', max_length=300)
    mobile = models.CharField('Mobile Number', max_length=50, blank=False)
    email = models.CharField('Email', max_length=50, blank=False)
    password = models.CharField('Password', max_length=50, blank=False)
    rating = models.IntegerField('User Rating', default=0)
    password = models.CharField('Password ', max_length=100)
    email = models.CharField('Email', max_length=100, unique=True)


# class Achievement