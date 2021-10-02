from django.db import models

# Create your models here.

class User(models.Model):
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15) 
    email = models.CharField(max_length=20) 
    password = models.CharField(max_length=20)
    postal_address =  models.CharField(max_length=100)
    studioname =  models.CharField(max_length=50)
    price =  models.BigIntegerField()
    instagram_id =  models.CharField(max_length=50)
    facebook_id =  models.CharField(max_length=50)

    def __str__(self):
        return self.email