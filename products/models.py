from django.db import models


class Products(models.Model):
    img = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    rate = models.FloatField()

