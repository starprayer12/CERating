from django.db import models


class emailcheck(models.Model):
    email = models.CharField(max_length=255)
    verification_code = models.CharField(max_length=6)
    c_time = models.IntegerField(max_length=20)