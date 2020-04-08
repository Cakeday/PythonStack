from django.db import models
import re

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name'])<=2:
            errors['first_name'] = "ur first name is def not that short"
        if len(postData['last_name'])<=2:
            errors['last_name'] = "ur last name is def not that short"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Please enter a valid email address"
        if len(postData['password'])<8:
            errors['password'] = "password is too short"
        if postData['password'] != postData['password_confirm']:
            errors['password_mismatch'] = "passwords dont match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    hashpw = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()

# Create your models here.
