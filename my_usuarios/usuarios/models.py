from django.db import models


class User(models.Model):

    name =  models.CharField(max_length=255)
    age =  models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

