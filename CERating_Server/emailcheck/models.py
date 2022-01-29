from django.db import models


class emailcheck(models.Model):
    email = models.CharField(max_length=32)
    code = models.IntegerField()
    timestamp = models.IntegerField()
