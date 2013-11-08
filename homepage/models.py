# models.py
from django.db import models
from django.contrib import admin


class Style(models.Model):
    name = models.CharField(max_length=30)
    comment = models.TextField()
    contr = models.CharField(max_length=30)
    lolfield = models.CharField(max_length=30)
  
    class Meta:
        ordering = ["-name"]

    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=30)
    comment = models.TextField()
    type = models.ManyToManyField(Style)
    price = models.CharField(max_length=30)

    class Meta:
        ordering = ["name"]

    def __unicode__(self):
        return self.name

admin.site.register(Item)
admin.site.register(Style)
