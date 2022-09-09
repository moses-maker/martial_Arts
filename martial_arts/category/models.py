from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Athlete(models.Model):
    class Martial_Arts_Category(models.TextChoices):
        JUDO = 'JU', _('Judo')
        JIU_JITSU = 'JS', _()



    martial_arts_category = [

    ]
    name = models.CharField(max_length=250)
    category = models.ChoiceField()
    weight = models.TextField()
    hours = models.DateTimeField()



