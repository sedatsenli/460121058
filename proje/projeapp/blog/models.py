from django.db import models

class Coffee (models.Model):
    title = models.CharField(max_length=80)
    image = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    url = models.URLField(blank=True)
