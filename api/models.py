from django.db import models

class ShortLink(models.Model):
    original = models.TextField(null=False, blank=False)
    shortKey = models.CharField(null=False, blank=False, max_length=30)

