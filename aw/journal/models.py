from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


RIVERS = [(0, 'list'), (1, 'of'), (2, 'rivers')]
class JournalEntry(models.Model):
    slug = models.SlugField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    river = models.CharField(max_length=50)
    flow = models.FloatField()
    description = models.TextField(max_length=250)
    public = models.BooleanField(default=False)
    # picture = models.ImageField()

    def __str__(self):
        return "{river}: {date}".format(river=self.river, date=self.date)
