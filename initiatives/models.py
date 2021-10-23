from django.db import models

from django.utils import timezone
# Create your models here.
# from administrations.models import AdministrationProfile
from users.models import UserProfile


class Initiative(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField('InitiativeName', max_length=300, blank=False)
    description = models.TextField('InitiativeAbout', max_length=10000, blank=False)
    address = models.CharField('InitiativeAddress', max_length=300)
    pub_date = models.DateTimeField('PublicationDate')
    category_name = models.CharField('CategoryName', max_length=50, blank=False)
    rating = models.IntegerField('InitiativeRating', default=0, blank=True)
    status = models.CharField('Status', max_length=50)
    # image добавить место у инициативы

    def save(self, *args, **kwargs):
        self.pub_date = timezone.now()
        return super(Initiative, self).save(*args, **kwargs)

class Comment(models.Model):
    initiative_comment = models.ForeignKey(Initiative, on_delete=models.CASCADE)
    user_comment = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # administration_comment = models.ForeignKey(AdministrationProfile, on_delete=models.CASCADE, blank=True, null=True)
    date_comment = models.DateTimeField('PublicationDate')
    message_comment = models.TextField('Message')

class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    initiative = models.ForeignKey(Initiative, on_delete=models.CASCADE)




