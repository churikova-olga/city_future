from initiatives.models import Initiative
import datetime
# Create your models here.


class Statistics:

    def number_of_new_initiatives(self, timedur):
        return Initiative.objects.filter(PublicationDate__level__gte=datetime.datetime.now()-timedur).count()

    # TODO: seaborn implement to show on the screen. Or mb
    template_name = 'base/admin_statistics.html'
# class Achievement