from django.db import models
from datetime import datetime


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title'])<2:
            errors['title'] = "Yo put a longer title ya dingus"
        if len(postData['network'])<3:
            errors['network'] = "Yo put a longer network ya dingbat"
        if postData['release_date']>datetime.now().strftime("%Y-%m-%d"):
            errors['release_date'] = "what is this, back to the future?"
        if len(postData['description'])<10:
            errors['description'] = "dude just put a longer description (or no description)"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()