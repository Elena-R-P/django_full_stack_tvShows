from django.db import models

class ShowManager(models.Manager):
    def show_validator(self, postData):
        errors = {}
        if len(postData['title']) < 5:
            errors["title"] = "Show title should be at least 5 characters"
        if len(postData['network']) < 2:
            errors["network"] = "Show Network should be at least 2 characters"
        if len(postData['release_date']) < 1:
            errors["release_date"] = "Please fill out the releade date"
        if len(postData['desc']) < 1:
            errors["desc"] = "Please fill out the Description"
        
        return errors


class Show(models.Model):
    show_title = models.CharField(max_length=45)
    show_network = models.CharField(max_length=45)
    show_desc = models.TextField()
    show_release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()