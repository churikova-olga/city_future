from django.db import models

# Create your models here.
from administrations.models import AdministrationProfile


class UserProfile(models.Model):
    first_name = models.CharField('First Name', max_length=100)
    last_name = models.CharField('Last Name', max_length=100)
    address = models.CharField('Your Address', max_length=300)
    mobile = models.CharField('Mobile Number', max_length=50)
    email = models.CharField('Email', max_length=50)
    password = models.CharField('Password', max_length=50, unique=True)
    rating = models.IntegerField('User Rating', default=0, blank=True)
    city = models.CharField('Your City', max_length=300)


# class Achievement

class Question(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    administration = models.ForeignKey(AdministrationProfile, on_delete=models.CASCADE, blank=True, null=True)
    message_question = models.TextField('Question')
    date_question =  models.DateTimeField('PublicationDate')

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = message_question = models.TextField('Answer')