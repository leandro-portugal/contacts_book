from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=154, blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=254, null=False, blank=False)
    last_name = models.CharField(max_length=254, null=False, blank=False)
    telephone = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=254, blank=True)
    creation_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.first_name
