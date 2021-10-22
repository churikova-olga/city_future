from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class UserProfile(AbstractUser):
    # first_name = models.CharField('First Name', max_length=100)
    # last_name = models.CharField('Last Name', max_length=100)
    address = models.CharField('Your Address', max_length=300)
    mobile = models.CharField('Mobile Number', max_length=50, blank=True)
    # email = models.CharField('Email', max_length=50)
    # password = models.CharField('Password', max_length=50, unique=True)
    rating = models.IntegerField('User Rating', default=0)
    city = models.CharField('Your City', max_length=300)
    is_administration = models.BooleanField(default=False,  verbose_name='administration status')
    role = models.CharField('Role', max_length=100, blank=True)
    organization = models.CharField('Organization', max_length=100, blank=True)
# class AdministrationProfile(models.Model):
#     first_name = models.CharField('First Name', max_length=100, blank=False)
#     last_name = models.CharField('Last Name', max_length=100, blank=False)
#     role = models.CharField('Role', max_length=100)
#     password = models.CharField('Password', max_length=100)
#     email = models.CharField('Email', max_length=100, unique=True)
#     organization = models.CharField('Organization', max_length=100)
#     address = models.CharField('Address', max_length=100)
#     city = models.CharField('city', max_length=100)

# class Achievement

class Question(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # administration = models.ForeignKey(AdministrationProfile, on_delete=models.CASCADE, blank=True, null=True)
    message_question = models.TextField('Question')
    date_question = models.DateTimeField('PublicationDate')

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField('Answer')