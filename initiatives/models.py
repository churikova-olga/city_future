from django.db import models

from django.utils import timezone
# Create your models here.


class Initiative(models.Model):
    name = models.CharField('InitiativeName', max_length=300, blank=False)
    description = models.TextField('InitiativeAbout', max_length=10000, blank=False)
    address = models.CharField('InitiativeAddress', max_length=300)
    pub_date = models.DateTimeField('PublicationDate')
    category_name = models.CharField('CategoryName', max_length=50, blank=False)
    rating = models.IntegerField('InitiativeRating', default=0)
    status = models.CharField('Status', max_length=50)

    def save(self, *args, **kwargs):
        self.pub_date = timezone.now()
        return super(Initiative, self).save(*args, **kwargs)





