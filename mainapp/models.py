from django.db import models

class data(models.Model):
    end_year = models.IntegerField(null=True, blank=True)
    intensity = models.IntegerField()
    sector = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    insight = models.TextField()
    url = models.URLField()
    region = models.CharField(max_length=255)
    start_year = models.IntegerField(null=True, blank=True)
    impact = models.IntegerField(null=True, blank=True)
    added = models.DateTimeField()
    published = models.DateTimeField()
    country = models.CharField(max_length=255, blank=True)
    relevance = models.IntegerField()
    pestle = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    title = models.TextField()
    likelihood = models.IntegerField()