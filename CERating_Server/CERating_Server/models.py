from django.db import models


class emailcheck(models.Model):
    email = models.CharField(max_length=32)
    code = models.IntegerField(max_length=11)
    timestamp = models.IntegerField(max_length=11)
