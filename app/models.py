from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Profile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    Address=models.TextField()
    Profile_photo=models.ImageField()


    def __str__(self):
        return self.username