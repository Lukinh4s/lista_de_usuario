from django.db import models


class Users(models.Model):

    name =  models.CharField(max_length=255)
    age =  models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)

    def __str__(self):
        return self.name

