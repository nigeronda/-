from django.db import models
from django.conf import settings
from django.utils import timezone


class homework(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    memo = models.TextField()
    pocket_money = models.IntegerField(default = 500)
    is_completed = models.BooleanField(default = False)
    created_date = models.DateTimeField(
            default=timezone.now)
    date = models.DateTimeField()

    def __str__(self):
        return self.title

# Create your models here.
