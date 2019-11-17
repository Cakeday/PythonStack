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

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['title'])==0:
            errors['title'] = "Needs to have a title"
        if len(postData['description'])<5:
            errors['description'] = "Needs to have a longer description"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    hashpw = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()

class Book(models.Model):
    title = models. CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded")
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    objects=BookManager()







